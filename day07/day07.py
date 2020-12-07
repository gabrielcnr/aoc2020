import re
from collections import deque, defaultdict


REGEX = re.compile(r"(.*) bags contain|(\d+) (.*?) bag")


def parse_rule(rule):
    matches = REGEX.findall(rule)
    if not matches:
        raise ValueError(f"Invalid rule: {rule!r}")
    parent_match, *children_matches = matches
    parent_bag, *_ = parent_match
    d = {}
    for child_match in children_matches:
        _, count, child_bag = child_match
        d[child_bag] = int(count)
    return parent_bag, d


def test_parse_rule():
    rule = "light red bags contain 1 bright white bag, 2 muted yellow bags."
    expected = "light red", {"bright white": 1, "muted yellow": 2}
    assert expected == parse_rule(rule)


def part1(input_, lookup_bag):
    rules, reversed_rules_lookup = populate_lookup_tables(input_)
    queue = deque(reversed_rules_lookup[lookup_bag])
    visited = set()
    while queue:
        bag = queue.popleft()
        if bag not in visited:
            visited.add(bag)
            for i in reversed_rules_lookup[bag]:
                queue.append(i)
    return visited


def populate_lookup_tables(input_):
    rules = {}
    reversed_rules_lookup = defaultdict(list)
    for rule in input_.splitlines():
        parent, children_counts = parse_rule(rule)
        rules[parent] = children_counts
        for child in children_counts:
            reversed_rules_lookup[child].append(parent)
    return rules, reversed_rules_lookup


TEST_INPUT = """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


def test_part1():
    visited = part1(TEST_INPUT, "shiny gold")
    assert {'bright white', 'muted yellow', 'dark orange', 'light red'} == visited


TEST_INPUT_2 = """\
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


def part2(input_, lookup_bag):
    rules, reversed_rules_lookup = populate_lookup_tables(input_)
    bags = []
    queue = deque([lookup_bag])
    while queue:
        bag = queue.popleft()
        bags.append(bag)
        for child, count in rules[bag].items():
            queue.extend([child] * count)
    return bags


def test_part2():
    # we include the target bag in the list of bags - so we need to discount 1
    assert 126 == len(part2(TEST_INPUT_2, "shiny gold")) - 1


if __name__ == "__main__":
    input_ = open("day07_input.txt").read()
    bags_containing_shiny_gold = part1(input_, "shiny gold")
    count = len(bags_containing_shiny_gold)
    print(f"Part 1 - bags eventually containing shiny gold: {count}")

    nested_bags = part2(input_, "shiny gold")
    count = len(nested_bags)
    print(f"Part 2 - total nested bags: {count-1}")