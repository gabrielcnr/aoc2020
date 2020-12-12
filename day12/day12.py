
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


if __name__ == '__main__':
    input_ = open("day12_input.txt").readlines()
    print("Part 1:", part1(input_))
