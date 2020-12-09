import itertools


class CircularBuffer:
    def __init__(self, size):
        self.cb = [None] * size
        self.start = 0
        self.end = 0
        self.size = size
        self.count = 0

    def is_full(self):
        return self.count == self.size

    def add(self, item):
        if self.is_full():
            # when it's full we need to move the pointer to the start
            self.start = (self.start + 1) % self.size
        else:
            self.count += 1

        # always add to the end
        self.cb[self.end] = item
        self.end = (self.end + 1) % self.size

    def __iter__(self):
        idx = self.start
        n = self.count
        while n > 0:
            yield self.cb[idx]
            idx = (idx + 1) % self.size
            n -= 1


def is_valid(cb, value):
    for a, b in itertools.combinations(cb, 2):
        if a + b == value:
            return True
    return False


def part1(cb_size, input_):
    cb = CircularBuffer(cb_size)
    for n in input_.splitlines():
        n = int(n)
        if cb.is_full():
            if not is_valid(cb, n):
                return n
        cb.add(n)


TEST_INPUT_1 = """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def test_part1():
    assert 127 == part1(5, TEST_INPUT_1)


if __name__ == "__main__":
    input_ = open("day09_input.txt").read()
    print("Part 1:", part1(25, input_))