from collections import deque, defaultdict


def part1(cards_1, cards_2):
    cards_1 = deque(cards_1)
    cards_2 = deque(cards_2)

    while cards_1 and cards_2:
        c1 = cards_1.popleft()
        c2 = cards_2.popleft()
        if c1 > c2:
            cards_1.extend([c1, c2])
        else:
            cards_2.extend([c2, c1])

    winner = cards_1 or cards_2

    score = 0
    for i, card in enumerate(reversed(winner), 1):
        score += (i * card)

    return score


def test_part1():
    assert 306 == part1(
        [9, 2, 6, 3, 1],
        [5, 8, 4, 7, 10],
    )


def parse_input():
    player = 0
    cards = defaultdict(list)
    with open("input22.txt") as f:
        for line in f:
            if line.strip():
                if line.startswith("Player"):
                    player += 1
                else:
                    cards[player].append(int(line.strip()))
    return cards.values()


if __name__ == "__main__":
    cards_1, cards_2 = parse_input()
    print("Part 1 winners score:", part1(cards_1, cards_2))
