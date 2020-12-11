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


def get_adjacents(layout, row, col):
    for x, y in itertools.product([row - 1, row, row + 1], [col - 1, col, col + 1]):
        if (x, y) != (row, col) and x >= 0 and y >= 0:
            try:
                yield layout[x][y]
            except IndexError:
                pass

def part1(input_):
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
                    adjacents_occupied = sum(1 for adj in get_adjacents(layout, row, col)
                        if adj == OCCUPIED)
                    if state == EMPTY and not adjacents_occupied:
                        new_row.append(OCCUPIED)
                    elif state == OCCUPIED and adjacents_occupied >= 4:
                        new_row.append(EMPTY)
                    else:
                        new_row.append(state)
            new_layout.append(new_row)

        if new_layout == layout:
            break

        layout = new_layout

    return sum(1 for row in layout for seat in row if seat == OCCUPIED)


def test_part1():
    37 == part1(TEST_INPUT)


if __name__ == "__main__":
    input_ = open("day11_input.txt").read()
    print("Part 1", part1(input_))

