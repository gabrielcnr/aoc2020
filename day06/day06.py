import functools


TEST_INPUT_1 = """\
abc

a
b
c

ab
ac

a
a
a
a

b"""


def count_questions_answered_by_group(group):
    return len(get_unique_questions_answered_by_group(group))


def get_unique_questions_answered_by_group(group):
    return {q for questions in group for q in questions}


def iter_groups(input_):
    group = []
    for line in input_.splitlines():
        if not line:
            yield group
            group = []
        else:
            group.append(line)
    if group:
        yield group


def part1(input_):
    return sum(count_questions_answered_by_group(g) for g in iter_groups(input_))


def test_part1():
    assert [3, 3, 3, 1, 1] == [
        count_questions_answered_by_group(g) for g in iter_groups(TEST_INPUT_1)]

    assert 11 == part1(TEST_INPUT_1)


# ---

def count_common_questions_in_group(group):
    return len(get_common_questions_in_group(group))


def get_common_questions_in_group(group):
    return functools.reduce(set.intersection, (set(g) for g in group))


def part2(input_):
    return sum(count_common_questions_in_group(g) for g in iter_groups(input_))


def test_part2():
    assert [3, 0, 1, 1, 1] == [
        count_common_questions_in_group(g) for g in iter_groups(TEST_INPUT_1)]

    assert 6 == part2(TEST_INPUT_1)


if __name__ == "__main__":
    input_ = open("day06_input.txt").read()
    print("Part 1 - sum of the counts:", part1(input_))
    print("Part 2 - sum of the counts:", part2(input_))
