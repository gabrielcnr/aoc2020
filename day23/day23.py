def take(it, n):
    for _ in range(n):
        yield next(it)


def part1(cups, n_rounds):
    cups = [int(n) for n in cups]
    # let's make the current cup always the first cup 
    # we rotate in the end of each round

    for round in range(1, n_rounds + 1):
        # print(f"-------- move {round} ---------")
        # print(f"cups: {cups}")
        # print(f"current: {cups[0]}")

        # The crab picks up the three cups that are immediately clockwise of the current cup. They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
        circle = cups[:]
        taken_cups = circle[1:4]
        # print(f"pick up: {taken_cups}")
        del circle[1:4]

        # Select destination cup
        destination_cup = circle[0] - 1
        if destination_cup < 1:
            destination_cup = 9

        while destination_cup in taken_cups:
            destination_cup -= 1
            if destination_cup < 1:
                destination_cup = 9

        # print(f"destination: {destination_cup}\n")

        destination_cup_index = circle.index(destination_cup) + 1
        for cup in reversed(taken_cups):
            circle.insert(destination_cup_index, cup)

        cups = circle[1:] + [circle[0]]

    index_of_cup_1 = cups.index(1)
    cups_clockwise_after_1 = cups[index_of_cup_1 + 1:] + cups[:index_of_cup_1]
    return "".join([str(n) for n in cups_clockwise_after_1])


def test_part1():
    assert "92658374" == part1("389125467", 10)
    assert "67384529" == part1("389125467", 100)


if __name__ == "__main__":
    print("Part 1:", part1("315679824", 100))