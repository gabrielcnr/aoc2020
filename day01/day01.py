def find(numbers, target):
    for x in numbers:
        y = target - x
        if y in numbers:
            return x, y
    return None, None


def part1():
    numbers = set(int(n) for n in open("day01.txt").readlines())
    x, y = find(numbers, 2020)
    if x is not None:
        return x, y


def part2():
    numbers = set(int(n) for n in open("day01.txt").readlines())

    for x in numbers:
        target = 2020 - x
        y, z = find(numbers, target) 
        if y is not None:
            return x, y, z



if __name__ == "__main__":
    print("Part 1")
    x, y = part1()
    print(f"{x=}, {y=} --> {x*y}")

    print("Part 2")
    x, y, z = part2()
    print(f"{x=}, {y=}, {z=} --> {x*y*z}")
