from textwrap import dedent

from aoc import read_input


class Submarine:
    def __init__(self):
        self.pos = 0
        self.depth = 0

    def forward(self, x):
        self.pos += x

    def down(self, x):
        self.depth += x

    def up(self, x):
        self.depth -= x


class Submarine2:
    def __init__(self):
        self.pos = 0
        self.depth = 0
        self.aim = 0

    def forward(self, x):
        self.pos += x
        self.depth += (self.aim * x)

    def down(self, x):
        self.aim += x

    def up(self, x):
        self.aim -= x


def solve(data, submarine_type):
    sub = submarine_type()

    for line in data.splitlines():
        command_name, param = line.strip().split()
        command = getattr(sub, command_name)
        command(int(param))

    return sub.pos * sub.depth


def part1(data):
    return solve(data, Submarine)


def part2(data):
    return solve(data, Submarine2)


test_input = dedent("""\
    forward 5
    down 5
    forward 8
    up 3
    down 8
    forward 2
""")


def test_part1():
    assert 150 == part1(test_input)


def test_part2():
    assert 900 == part2(test_input)


if __name__ == '__main__':
    data = read_input(__file__)
    print("Part 1", part1(data))
    print("Part 2", part2(data))
