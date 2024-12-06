from collections import defaultdict
from input_processing import read_data, get_numbers_from_lines, get_groups


def parse(data):
    rules, updates = get_groups(data)
    rules = get_numbers_from_lines(rules)
    updates = get_numbers_from_lines(updates)
    return rules, updates


def get_print_order(update):
    return {page: i for i, page in enumerate(update)}


def get_applicable_rules(rules, update):
    return [rule for rule in rules if rule[0] in update and rule[1] in update]


def valid_order(order, rules):
    for rule in rules:
        if order[rule[0]] > order[rule[1]]:
            return False
    return True


def part1(rules, updates):
    total = 0

    for update in updates:
        print_order = get_print_order(update)
        applicable_rules = get_applicable_rules(rules, print_order)
        if valid_order(print_order, applicable_rules):
            total += update[len(update) // 2]

    return total


def part2(rules, updates):
    # topological sort
    def sort_pages(rules, pages):
        visited = set()
        result = []

        rule_graph = defaultdict(list)
        for rule in rules:
            rule_graph[rule[0]].append(rule[1])

        def sort_helper(page):
            visited.add(page)
            for next_page in rule_graph[page]:
                if next_page not in visited:
                    sort_helper(next_page)
            result.insert(0, page)

        for page in pages:
            if page not in visited:
                sort_helper(page)

        return result

    total = 0
    for update in updates:
        print_order = get_print_order(update)
        applicable_rules = get_applicable_rules(rules, print_order)
        if not valid_order(print_order, applicable_rules):
            order = sort_pages(applicable_rules, update)
            total += order[len(order) // 2]

    return total


def test():
    data = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''
    rules, updates = parse(data)
    assert part1(rules, updates) == 143
    assert part2(rules, updates) == 123


test()
data = read_data(2024, 5)
rules, updates = parse(data)
print('Part1:', part1(rules, updates))
print('Part2:', part2(rules, updates))
