
def part1(map_, slope):
    dy, dx = slope
    x, y = 0, 0
    rows = map_.split("\n")
    check_locations = []
    while x < len(rows):
        check_locations.append((x, y))
        x += dx
        y += dy

    repeat_pattern = len(rows[0])

    return sum(1 for x, y in check_locations if rows[x][y % repeat_pattern] == "#")


SLOPES_PART_2 = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]


def part2(map_, slopes):
    p = 1
    for slope in slopes:
        p *= part1(map_, slope)
    return p


TEST_INPUT = """\
..##.........##.........##.........##.........##.........##.......
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#"""


def test_part1():
    assert 7 == part1(TEST_INPUT, slope=(3, 1))


def test_part2():
    assert 336 == part2(TEST_INPUT, slopes=SLOPES_PART_2)


if __name__ == "__main__":
    map_ = open("day03_input.txt").read()
    print("Part 1", part1(map_, slope=(3, 1)))
    print("Part 2", part2(map_, slopes=SLOPES_PART_2))
