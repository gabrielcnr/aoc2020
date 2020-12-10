from collections import Counter


def part1(input_):
    numbers = sorted(int(n) for n in input_.splitlines())
    jolt_diffs = Counter()
    last = 0
    for n in numbers:
        diff = n - last
        jolt_diffs[diff] += 1
        last = n

    # account for my adapter (always +3 from the highest)
    jolt_diffs[3] += 1

    return jolt_diffs, jolt_diffs[1] * jolt_diffs[3]


TEST_INPUT = """\
16
10
15
5
1
11
7
19
6
12
4"""


TEST_INPUT_2 = """\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


def test_part1():
    assert ({1: 7, 3: 5}, 35) == part1(TEST_INPUT)

    assert ({1: 22, 3: 10}, 220) == part1(TEST_INPUT_2)


if __name__ == "__main__":
    input_ = open("day10_input.txt").read()
    print("Part 1", part1(input_))
