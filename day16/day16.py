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



def produce_my_ticket(X):
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

    def is_valid(nums):
        results = []
        for n in nums:
            ok = False
            for field, rule in rules.items():
                if eval(rule, {"x": n}):
                    ok = True
                    break
            results.append(ok)
        return all(results)

    valid_tickets = []
    valid_tickets = [[int(n) for n in my_ticket[0].split(",")]]
    for nearby_ticket in nearby_tickets:
        nums = [int(n) for n in nearby_ticket.split(",")]
        if is_valid(nums):
            valid_tickets.append(nums)

    # if len(valid_tickets)== 1:
    #     valid_tickets = valid_tickets * 2

    fields = []
    for nums in zip(*valid_tickets):
        found = False
        for field, rule in rules.items():
            if all(eval(rule, {"x": n}) for n in nums):
                fields.append(field)
                found = True
                break
        if found:
            del rules[field]

    my_ticket = dict(zip(fields, [int(n) for n in my_ticket[0].split(",")]))
    import pdb; pdb.set_trace()
    return my_ticket


def part2(X):
    my_ticket = produce_my_ticket(X)

    prod = 1
    for field, value in my_ticket.items():
        if field.startswith("departure"):
            prod *= value

    return prod


TEST_INPUT_2 = """\
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""

def test_part2():
    assert {"class": 12, "row": 11, "seat": 13} == produce_my_ticket(TEST_INPUT_2)


if __name__ == "__main__":
    input_ = open("day16_input.txt").read()
    print("Part 1:", part1(input_))

    print("Part 2:", part2(input_))
