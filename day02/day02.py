import re
from collections import Counter

regex = re.compile(r"^(\d+)\-(\d+)\s([a-z])\:\s(\w+)$")

def process(input_lines):
    for line in input_lines:
        m = regex.match(line)

        if not m:
            raise RuntimeError(f"Invalid input line: {line}")

        yield m.groups()


def part1(input_lines):
    count_valid_passwords = 0

    for min_, max_, c, password in process(input_lines):
        counter = Counter(password)

        if int(min_) <= counter[c] <= int(max_):
            count_valid_passwords += 1

    return count_valid_passwords


def part2(input_lines):
    count_valid_passwords = 0

    for idx_on, idx_off, c, password in process(input_lines):
        idx_on, idx_off = int(idx_on), int(idx_off)
        chars = {password[idx_on - 1], password[idx_off - 1]}
        if c in chars and len(chars) == 2:
            count_valid_passwords += 1

    return count_valid_passwords


def test_part1():
    input_lines = ("1-3 a: abcde\n"
                   "1-3 b: cdefg\n"
                   "2-9 c: ccccccccc")

    assert 2 == part1(input_lines.split("\n"))


def test_part2():
    input_lines = ("1-3 a: abcde\n"
                   "1-3 b: cdefg\n"
                   "2-9 c: ccccccccc")

    assert 1 == part2(input_lines.split("\n"))


if __name__ == "__main__":
    input_lines = open("day02_input.txt").readlines()
    print(part1(input_lines))
    print(part2(input_lines))
