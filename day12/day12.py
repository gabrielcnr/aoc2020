INPUT = """\
F10
N3
F7
R90
F11"""


def test_part1():
    assert (17, -8) == navigate(INPUT.splitlines())


POINTS = "NESW"


def navigate(input_):
    x = 0
    y = 0

    face = "E"

    for instruction in input_:
        action = instruction[0]
        value = int(instruction[1:])

        if action == "F":
            action = face

        if action == "N":
            y += value
        elif action == "S":
            y -= value
        elif action == "E":
            x += value
        elif action == "W":
            x -= value
        elif action == "R":
            rotations = value // 90
            idx = (POINTS.index(face) + rotations) % len(POINTS)
            face = POINTS[idx]
        elif action == "L":
            rotations = value // 90
            idx = (POINTS.index(face) - rotations) % len(POINTS)
            face = POINTS[idx]
        else:
            raise ValueError

        # print(f"{x=}, {y=}")

    return (x, y)


def part1(input_):
    x, y = navigate(input_)
    return abs(x) + abs(y)


def test_part2():
    assert (214, -72) == navigate2(INPUT.splitlines())


def navigate2(input_):
    x, y = 0, 0  # ship

    wpx, wpy = 10, 1  # waypoint

    for instruction in input_:
        action = instruction[0]
        value = int(instruction[1:])

        if action == "F":
            # moves the ship
            x += (wpx * value)
            y += (wpy * value)
        elif action == "N":
            wpy += value
        elif action == "S":
            wpy -= value
        elif action == "E":
            wpx += value
        elif action == "W":
            wpx -= value
        elif action == "R":
            rotations = value // 90
            while rotations:
                # (10, 4) --> 90 graus --> (4, -10)
                # (x, y) -> (y, -x)
                wpx, wpy = wpy, -wpx
                rotations -= 1
        elif action == "L":
            rotations = value // 90
            while rotations:
                # (4, -10) --> -90 graus --> (10, 4)
                # (-y, x)
                wpx, wpy = -wpy, wpx
                rotations -= 1
        else:
            raise ValueError

        # print(f"{x=}, {y=}, {wpx=}, {wpy=}")

    return (x, y)


def part2(input_):
    x, y = navigate2(input_)
    return abs(x) + abs(y)


if __name__ == '__main__':
    input_ = open("day12_input.txt").readlines()
    print("Part 1:", part1(input_))
    print("Part 2:", part2(input_))
