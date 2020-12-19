from typing import List, Set
from collections import defaultdict


def parse_input(filename: str) -> (List[str], List[str]):
    rule_group, string_group = open(filename).read().split('\n\n')
    rules = [rule.strip() for rule in rule_group.split('\n')]
    strings = [string.strip() for string in string_group.split('\n')]
    return rules, strings


def all_solved(rules: List[List[int]], solved: List[int]) -> bool:
    for part in rules:
        for section in part:
            if section not in solved:
                return False
    return True


def solve(rule_id: int, unsolved_rules: dict, solved: dict):
    rule = unsolved_rules[rule_id]
    for part in rule:
        if len(part) == 1:
            # one item
            p1 = part[0]
            for s1 in solved[p1]:
                solved[rule_id].append(s1)
        elif len(part) == 2:
            # two items
            p1, p2 = part
            for s1 in solved[p1]:
                for s2 in solved[p2]:
                    solved[rule_id].append(s1 + s2)
        elif len(part) == 3:
            # three items
            p1, p2, p3 = part
            for s1 in solved[p1]:
                for s2 in solved[p2]:
                    for s3 in solved[p3]:
                        solved[rule_id].append(s1 + s2 + s3)
    del unsolved_rules[rule_id]


def get_solved_rules(rule_strings: List[str]) -> dict:
    solved = defaultdict(lambda: [])
    unsolved_rules = defaultdict(lambda: [])

    # get initial set of rules
    for rule_string in rule_strings:
        identifier, rule = rule_string.split(': ')
        rule_parts = rule.split(' | ')
        for rule_part in rule_parts:
            if '"' in rule_part:
                solved[identifier].append(rule_part[1])
            else:
                rule_bits = rule_part.split(' ')
                unsolved_rules[identifier].append(rule_bits)

    print('SOLVING RULES')

    # solve unsolved rules
    while unsolved_rules:
        for rule in unsolved_rules:
            rule_parts = unsolved_rules[rule]
            if all_solved(rule_parts, list(solved.keys())):
                solve(rule, unsolved_rules, solved)
                break

    print('SOLVED')

    return solved


def part1(solved: dict, strings: List[str]) -> int:
    # generate a set of all valid strings
    valid_strings = set()
    for rule in solved:
        for valid in solved[rule]:
            valid_strings.add(valid)

    # count strings that are valid
    valid = []
    for string in strings:
        if string in valid_strings:
            valid.append(string)

    return len(valid)


def is_valid_p2(string: str, rule_42: Set[str], rule_31: Set[str]) -> bool:
    """
    0: 8 11
    8: 42 | 42 8
    11: 42 31 | 42 11 31
    ---------------------------------------------------------------------------
    everything can be expressed in 42 (A) and 31 (B)
    8: (A)+ ex. A AA AAA AAAA...
    11: (A)x(B)x with equal amounts of A and B and x > 0 ex. AB AABB AAABBB...
    0: (A)+(A)x(B)x
    ---------------------------------------------------------------------------
    A = set(42) and B = set(31) are completely different and len(A) = len(B) = 8
    """
    num_b = 0
    while string != '' and string[-8:] in rule_31:
        string = string[:-8]
        num_b += 1

    if num_b == 0:
        return False

    num_a = 0
    while string != '' and string[-8:] in rule_42:
        string = string[:-8]
        num_a += 1

    if string != '':
        return False
    if num_a < num_b + 1:
        return False

    return True


def part2(solved: dict, strings: List[str]) -> int:
    rule_42 = set(solved['42'])
    rule_31 = set(solved['31'])

    valid = []
    for string in strings:
        if is_valid_p2(string, rule_42, rule_31):
            valid.append(string)

    return len(valid)


def main():
    rules, strings = parse_input('input/day19.txt')
    solved = get_solved_rules(rules)
    print(f'Part 1: {part1(solved, strings)}')
    print(f'Part 2: {part2(solved, strings)}')


if __name__ == "__main__":
    main()
