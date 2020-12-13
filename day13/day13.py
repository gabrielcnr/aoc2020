TEST_INPUT = """\
939
7,13,x,x,59,x,31,19"""


def parse_input(input_):
    first, second = input_.splitlines()
    timestamp = int(first)
    buses = [int(i) for i in second.split(",") if i != "x"]
    return timestamp, buses


def get_earliest_bus_after(timestamp, buses):
    best_waiting_time = float("inf")
    earliest_bus = -1
    for bus in buses:
        time_since_last_departure = timestamp % bus
        if time_since_last_departure == 0:
            # bus is here!
            wait_time = 0
        else:
            wait_time = bus - time_since_last_departure

        if wait_time < best_waiting_time:
            best_waiting_time = wait_time
            earliest_bus = bus
    return earliest_bus, best_waiting_time


def part1(input_):
    timestamp, buses = parse_input(input_)
    bus, wait_time = get_earliest_bus_after(timestamp, buses)
    return bus * wait_time


def test_part1():
    timestamp, buses = parse_input(TEST_INPUT)
    bus, wait_time = get_earliest_bus_after(timestamp, buses)
    assert 59 == bus
    assert 5 == wait_time

    assert 295 == part1(TEST_INPUT)


if __name__ == '__main__':
    input_ = open("day13_input.txt").read()
    print("Part 1", part1(input_))
