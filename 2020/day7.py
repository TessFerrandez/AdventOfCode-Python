import pytest
from collections import defaultdict


def parse_input(filename: str):
    lines = [line.strip() for line in open(filename).readlines()]
    bags = defaultdict(dict)
    for line in lines:
        outer, inner = line.split(' contain ')
        outer_color = outer.replace(' bags', '')
        inner_bags = inner.split(', ')
        for inner_bag in inner_bags:
            num, *color, _ = inner_bag.split(' ')
            if num == 'no':
                bags[outer_color] = {}
            else:
                inner_color = ' '.join(color)
                bags[outer_color][inner_color] = int(num)
    return bags


def part1(rules: defaultdict, inner_bag: str) -> int:
    containers = set()
    bags_to_check = set()

    bags_to_check.add(inner_bag)
    while bags_to_check:
        bag = bags_to_check.pop()
        for outer_bag in rules:
            if bag in rules[outer_bag]:
                # print('adding:', outer_bag)
                containers.add(outer_bag)
                bags_to_check.add(outer_bag)
    return len(containers)


def get_contents(bag_color: str, rules: defaultdict) -> int:
    num_bags = 0
    bag_types = rules[bag_color]
    for bag_type in bag_types:
        num_of_bag_type = bag_types[bag_type]
        num_bags += num_of_bag_type
        num_bags += num_of_bag_type * get_contents(bag_type, rules)
    return num_bags


def part2(rules: defaultdict) -> int:
    return get_contents('shiny gold', rules)


def main():
    rules = parse_input('input/day7.txt')
    print(f'Part 1: {part1(rules, "shiny gold")}')
    print(f'Part 2: {part2(rules)}')


if __name__ == "__main__":
    main()
