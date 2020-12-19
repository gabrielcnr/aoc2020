def iter_expressions(expr):
    parens = 0
    e = ""
    for c in expr:
        if c == "(":
            parens += 1
            if parens > 1: # the first open parentheses we don't include
                e += c
        elif c == ")":
            parens -= 1
            if parens > 0: # the last close parentheses we don't include
                e += c
        elif c == " " and parens == 0:
            yield e
            e = ""
        else:
            e += c
    yield e


def calc(expr):
    if isinstance(expr, int):
        return expr
    stack = list(iter_expressions(expr))
    while len(stack) > 1:
        left, op, right, *stack_tail = stack
        a = calc(left)
        b = calc(right)
        stack = [eval(f"a {op} b", {"a": a, "b": b})] + stack_tail
    result, = stack
    return int(result)


def test_calc_simplest():
    assert 3 == calc("1 + 2")


def test_iter_expressions():
    assert ["7"] == list(iter_expressions("7"))
    assert ["2", "*", "3 + 4"] == list(iter_expressions("2 * (3 + 4)"))
    assert ["2", "*", "3 + (4 * 2)"] == list(iter_expressions("2 * (3 + (4 * 2))"))


def test_calc_parentheses():
    assert 14 == calc("2 * (3 + 4)")
    assert 6 == calc("(1 + 2) * (1 + 1)")


def test_part1_calc():
    assert 71 == calc("1 + 2 * 3 + 4 * 5 + 6")
    assert 26 == calc("2 * 3 + (4 * 5)")
    assert 437 == calc("5 + (8 * 3 + 9 + 3 * 4 * 3)")
    assert 12240 == calc("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")
    assert 13632 == calc("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")


def part1(input_: str):
    return sum(calc(expr) for expr in input_.splitlines())


def calc2(expr):
    if isinstance(expr, int):
        return expr
    stack = list(iter_expressions(expr))
    while len(stack) > 1:
        # look for addition first
        if "+" in stack:
            add_idx = stack.index("+")
            left, op, right = stack[add_idx - 1: add_idx + 2]
            stack_head = stack[:add_idx - 1]
            stack_tail = stack[add_idx + 2:]
        else:
            stack_head = []
            left, op, right, *stack_tail = stack
        a = calc2(left)
        b = calc2(right)
        stack = stack_head + [eval(f"a {op} b", {"a": a, "b": b})] + stack_tail
    result, = stack
    return int(result)


def test_part2_calc():
    assert 231 == calc2("1 + 2 * 3 + 4 * 5 + 6")
    assert 51 == calc2("1 + (2 * 3) + (4 * (5 + 6))")
    assert 46 == calc2("2 * 3 + (4 * 5)")
    assert 1445 == calc2("5 + (8 * 3 + 9 + 3 * 4 * 3)")
    assert 669060 == calc2("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")
    assert 23340 == calc2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")


def part2(input_: str):
    return sum(calc2(expr) for expr in input_.splitlines())


if __name__ == '__main__':
    input_ = open("input18.txt").read()
    print("Part 1:", part1(input_))

    print("Part 2:", part2(input_))
