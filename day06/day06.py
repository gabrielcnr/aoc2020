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


if __name__ == "__main__":
    input_ = open("day06_input.txt").read()
    print("Part 1 - sum of the counts:", part1(input_))
