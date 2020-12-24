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


def game2(cards_1, cards_2):
    """ recursive combat game
    """
    cards_1 = deque(cards_1)
    cards_2 = deque(cards_2)

    rounds_history = set()

    while cards_1 and cards_2:
        # before anything else let's check against infinite recursion
        hands = (tuple(cards_1), tuple(cards_2))
        if hands in rounds_history:
            # winner is player 1
            return 1, 0
        else:
            rounds_history.add(hands)

        c1 = cards_1.popleft()
        c2 = cards_2.popleft()
        
        if len(cards_1) >= c1 and len(cards_2) >= c2:
            # sub-game!
            round_winner, _ = game2(list(cards_1)[:c1], list(cards_2)[:c2])
            if round_winner == 1:
                cards_1.extend([c1, c2])
            else:
                cards_2.extend([c2, c1])
        elif c1 > c2:
            cards_1.extend([c1, c2])
        else:
            cards_2.extend([c2, c1])

    if cards_1:
        winner = 1
        winners_deck = cards_1
    else:
        winner = 2
        winners_deck = cards_2

    score = 0
    for i, card in enumerate(reversed(winners_deck), 1):
        score += (i * card)

    return winner, score


def test_part2():
    winner, score = game2(
        [9, 2, 6, 3, 1],
        [5, 8, 4, 7, 10],
    )
    assert winner == 2  # Player 2 wins
    assert score == 291


# def test_part2_infinite_game_prevention_rule():
#     game2([43, 19], [2, 29, 14])


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

    cards_1, cards_2 = parse_input()
    print("Part 2 winners score:", game2(cards_1, cards_2))
