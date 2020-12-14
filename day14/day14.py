import itertools


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
        'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
        'mem[8] = 11',
        'mem[7] = 101',
        'mem[8] = 0',    
    ]

    mem = part1(lines)

    assert 165 == sum(mem.values())


def part2(input_):
    class Memory(dict):
        mask = None
        def __setitem__(self, address, value):
            bin_number = f"{bin(address)[2:]:0>36}"
            masked_address = []
            positions_with_x = []
            for i, (b1, b2) in enumerate(zip(bin_number, self.mask)):
                if b2 == "0":
                    masked_address.append(b1)
                elif b2 == "1":
                    masked_address.append("1")
                elif b2 == "X":
                    positions_with_x.append(i)
                    masked_address.append("X")

            if positions_with_x:
                addresses = []
                for combo in itertools.product(*[["0", "1"]] * len(positions_with_x)):
                    for pos, bit in zip(positions_with_x, combo):
                        masked_address[pos] = bit
                    addresses.append(masked_address[:])
            else:
                addresses = masked_address

            for address in addresses:
                address = int("".join(address), 2)
                super().__setitem__(address, value)

    mem = Memory()

    for line in input_:
        if line.startswith("mask = "):
            _, mask = line.split(" = ")
            line = f"mem.mask = {mask!r}"
        exec(line)

    return mem


def test_part2():
    input_ = [
        "mask = 000000000000000000000000000000X1001X",
        "mem[42] = 100",
        "mask = 00000000000000000000000000000000X0XX",
        "mem[26] = 1",
    ]

    mem2 = part2(input_)

    assert 208 == sum(mem2.values())


if __name__ == "__main__":
    input_ = open("day14_input.txt").readlines()
    mem_1 = part1(input_)
    print("Part 1", sum(mem_1.values()))

    mem_2 = part2(input_)
    print("Part 2", sum(mem_2.values()))
