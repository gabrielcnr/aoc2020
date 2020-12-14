def iter_mask(bitmask, number):
    bin_number = f"{bin(number)[2:]:0>36}"
    for b1, b2 in zip(bin_number, bitmask):
        if b2 == "X":
            yield b1
        else:
            yield b2

def apply_mask(bitmask, number):
    n = "".join(iter_mask(bitmask, number))
    return int(n, 2)


def test_apply_mask():
    bitmask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
    value = 11
    assert 73 == apply_mask(bitmask, value)


def part1(input_):
    class Memory(dict):
        mask = None
        def __setitem__(self, address, value):
            masked_value = apply_mask(self.mask, value)
            super().__setitem__(address, masked_value)

    mem = Memory()

    for line in input_:
        if line.startswith("mask = "):
            _, mask = line.split(" = ")
            line = f"mem.mask = {mask!r}"
        exec(line)

    return mem


def test_part1():
    lines = [
        'mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"',
        'mem[8] = 11',
        'mem[7] = 101',
        'mem[8] = 0',    
    ]

    mem = part1(lines)

    assert 165 == sum(mem.values())


if __name__ == "__main__":
    input_ = open("day14_input.txt").readlines()
    mem_1 = part1(input_)
    print("Part 1", sum(mem_1.values()))
