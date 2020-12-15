import pytest
from collections import defaultdict


def game(numbers):
    calls = defaultdict(list)
    i = 1
    last = None
    while True:
        if i < len(numbers) + 1:
            spoken_num = numbers[i - 1]
        else:
            if len(calls[last]) == 1:  # it was the first time
                spoken_num = 0
            else:
                last_calls = calls[last]
                next_to_last_call, last_call = last_calls[-2], last_calls[-1]
                spoken_num = last_call - next_to_last_call

        yield spoken_num
        calls[spoken_num].append(i)
        last = spoken_num
        i += 1


def part1(input_numbers, play_until=2020):
    for i, spoken_num in enumerate(game(input_numbers), 1):
        if i == play_until:
            return spoken_num


def test_game_part1():
    # TODO: could use itertools.takewhile
    g = game([0, 3, 6])
    spoken_numbers = [next(g) for _ in range(10)]
    assert [0, 3, 6, 0, 3, 3, 1, 0, 4, 0] == spoken_numbers


@pytest.mark.parametrize(
    ["input_numbers", "last_spoken_number"],
    [
        ([1, 3, 2], 1),
        ([2, 1, 3], 10),
        ([1, 2, 3], 27),
        ([2, 3, 1], 78),
        ([3, 2, 1], 438),
        ([3, 1, 2], 1836),
    ],
)
def test_part1(input_numbers, last_spoken_number):
    assert last_spoken_number == part1(input_numbers)


if __name__ == "__main__":
    input_numbers = [15, 12, 0, 14, 3, 1]
    print("Part 1", part1(input_numbers))

    print("Part 2", part1(input_numbers, 30000000))
