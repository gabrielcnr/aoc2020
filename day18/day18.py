def iter_expressions(expr):
    parens = 0
    e = ""
    for c in expr:
        if c == "(":
            parens += 1
            e += c
        elif c == ")":
            parens -= 1
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
    if expr[0] == "(" and expr[-1] == ")" and expr.count("(") == 1:  # TODO: isso aqui ta ruim
        expr = expr[1:-1]
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
    assert ["2", "*", "(3 + 4)"] == list(iter_expressions("2 * (3 + 4)"))
    assert ["2", "*", "(3 + (4 * 2))"] == list(iter_expressions("2 * (3 + (4 * 2))"))


def test_calc_parentheses():
    # assert 14 == calc("2 * (3 + 4)")
    assert 6 == calc("(1 + 2) * (1 + 1)")


def test_part1_calc():
    assert 71 == calc("1 + 2 * 3 + 4 * 5 + 6")
    assert 26 == calc("2 * 3 + (4 * 5)")
    assert 437 == calc("5 + (8 * 3 + 9 + 3 * 4 * 3)")
    assert 12240 == calc("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")
    assert 13632 == calc("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")


def part1(input_: str):
    for e in input_.splitlines():
        try:
            calc(e)
        except Exception:
            import pdb; pdb.set_trace()
    return sum(calc(expr) for expr in input_.splitlines())


if __name__ == '__main__':
    input_ = open("input18.txt").read()
    print("Part 1:", part1(input_))
