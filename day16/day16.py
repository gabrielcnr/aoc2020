TEST_INPUT = """\
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

def part1(X):
    field_lines = []
    my_ticket = []
    nearby_tickets = []

    L = field_lines
    for line in X.splitlines():
        if line == "your ticket:":
            L = my_ticket
        elif line == "nearby tickets:":
            L = nearby_tickets
        elif line:
            L.append(line)

    rules = {}
    for field_line in field_lines:
        field, rule = field_line.split(":")
        rule = rule.replace("-", "<= x <=")
        rules[field] = rule

    err_rate = 0
    for nearby_ticket in nearby_tickets:
        for n in nearby_ticket.split(","):
            n = int(n)
            ok = False
            for field, rule in rules.items():
                if eval(rule, {"x": n}):
                    ok = True
                    break
            if not ok:
                err_rate += n

    return err_rate


def test_part1():
    assert 71 == part1(TEST_INPUT)


if __name__ == "__main__":
    input_ = open("day16_input.txt").read()
    print("Part 1:", part1(input_))
