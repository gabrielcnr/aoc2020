import itertools


FLOOR = "."
EMPTY = "L"
OCCUPIED = "#"


TEST_INPUT = """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

DIRECTIONS = {
    "NW": (-1, 1),
    "N": (0, 1),
    "NE": (1, 1),
    "W": (-1, 0),
    "E": (1, 0),
    "SW": (-1, -1),
    "S": (0, -1),
    "SE": (1, -1),
}


# def get_adjacents(layout, row, col):
#     for direction, (dx, dy) in DIRECTIONS.items():
#         x = row + dx
#         y = col + dy

#         if x >= 0 and y >= 0:
#             try:
#                 yield layout[x][y]
#             except IndexError:
#                 continue



def get_adjacents(layout, row, col, callback):
    for direction, (dx, dy) in DIRECTIONS.items():
        x, y = row + dx, col + dy
        found = False
        out_of_bounds = x < 0 or y < 0
        while not found and not out_of_bounds:
            try:
                state = layout[x][y]
                if callback(state):
                    yield state
                    found = True
            except IndexError:
                out_of_bounds = True
            else:
                x += dx
                y += dy
                out_of_bounds = x < 0 or y < 0



def solver(input_, callback, occupied_seats_threshold):
    layout = [list(s) for s in input_.splitlines()]

    num_rows = len(layout)
    num_cols = len(layout[0])

    while True:
        new_layout = []
        for row in range(num_rows):
            new_row = []
            for col in range(num_cols):
                state = layout[row][col]
                if state == FLOOR:
                    new_row.append(state)
                else:
                    adjacents_occupied = sum(1 for adj in get_adjacents(layout, row, col, callback)
                        if adj == OCCUPIED)
                    if state == EMPTY and not adjacents_occupied:
                        new_row.append(OCCUPIED)
                    elif state == OCCUPIED and adjacents_occupied >= occupied_seats_threshold:
                        new_row.append(EMPTY)
                    else:
                        new_row.append(state)
            new_layout.append(new_row)

        if new_layout == layout:
            break

        layout = new_layout

    return sum(1 for row in layout for seat in row if seat == OCCUPIED)


def part1(input_):
    def callback(state):
        return True

    threshold = 4
    return solver(input_, callback, threshold)


def part2(input_):
    def callback(state):
        return state != FLOOR

    threshold = 5
    return solver(input_, callback, threshold)


def test_part1():
    assert 37 == part1(TEST_INPUT)


def test_part2():
    assert 26 == part2(TEST_INPUT)


if __name__ == "__main__":
    input_ = open("day11_input.txt").read()
    print("Part 1", part1(input_))

    print("Part 2", part2(input_))
