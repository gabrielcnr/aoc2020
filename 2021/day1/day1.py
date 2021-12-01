import itertools
from collections import deque
from textwrap import dedent

test_input = dedent("""\
    199
    200
    208
    210
    200
    207
    240
    269
    260
    263""")


def get_measurements(data):
    lines = (l.strip() for l in data.strip().splitlines())
    return (int(l) for l in lines)


def part1(data):
    measurements = get_measurements(data)
    last = next(measurements)
    count = 0
    for m in measurements:
        if m > last:
            count += 1
        last = m
    return count


def part2(data):
    measurements = get_measurements(data)
    sums = iter_sums(measurements, 3)
    last_sum = next(sums)
    count = 0
    for sum_ in sums:
        if sum_ > last_sum:
            count += 1
        last_sum = sum_
    return count


def iter_sums(numbers, window_size):
    nums = deque(itertools.islice(numbers, window_size))
    sum_ = sum(nums)
    yield sum_

    for n in numbers:
        discard = nums.popleft()
        nums.append(n)
        sum_ += (n - discard)
        yield sum_


def test_part1():
    assert 7 == part1(test_input)


def test_part2():
    assert 5 == part2(test_input)


if __name__ == '__main__':
    data = open("input.txt").read()
    print("Part 1", part1(data))
    print("Part 2", part2(data))
