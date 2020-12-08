import pytest

TEST_INPUT = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

class InfiniteLoopException(Exception):
	pass


class Machine:
	def __init__(self):
		self.accumulator = 0

	def run(self, program):
		visited = set()
		program_counter = 0
		while program_counter < len(program):
			instruction = program[program_counter]
			operation, argument = instruction.split()
			op_handler = getattr(self, f"op_{operation}")
			visited.add(program_counter)
			program_counter = op_handler(argument, program_counter)
			if program_counter in visited:
				raise InfiniteLoopException(f"Infinite recursion detected when {program_counter=}")

	def op_acc(self, argument, program_counter):
		self.accumulator += int(argument)
		return program_counter + 1

	def op_jmp(self, argument, program_counter):
		return program_counter + int(argument)

	def op_nop(self, argument, program_counter):
		return program_counter + 1


def test_part1():
	m = Machine()
	with pytest.raises(InfiniteLoopException):
		m.run(TEST_INPUT.splitlines())

	assert 5 == m.accumulator


def part1(input_):
	m = Machine()
	try:
		m.run(input_)
	except InfiniteLoopException:
		pass
	return m.accumulator


def part2(input_):
	def iter_jmp_or_nop_indexes():
		for i, instruction in enumerate(input_):
			operation, _ = instruction.split()
			if operation in ["jmp", "nop"]:
				yield i

	for index_to_change_operation in iter_jmp_or_nop_indexes():
		modified_input = input_[:]
		instruction_to_modify = modified_input[index_to_change_operation]
		if instruction_to_modify.startswith("jmp"):
			modified_input[index_to_change_operation] = instruction_to_modify.replace("jmp", "nop")
		elif instruction_to_modify.startswith("nop"):
			modified_input[index_to_change_operation] = instruction_to_modify.replace("nop", "jmp")
		m = Machine()
		try:
			m.run(modified_input)
		except InfiniteLoopException:
			continue
		else:
			return m.accumulator


def test_part2():
	assert 8 == part2(TEST_INPUT.splitlines())


if __name__ == "__main__":
	program = open("day08_input.txt").readlines()
	part1_accumulator = part1(program)
	print(f"Part 1 - accumulator =", part1_accumulator)

	part2_accumulator = part2(program)
	print(f"Part 2 - accumulator =", part2_accumulator)

