from typing import List
from collections import Counter


def parse_input(filename: str) -> dict:
    programs = {}
    lines = [line.strip() for line in open(filename).readlines()]
    for line in lines:
        parts = line.split(' -> ')
        program, weight = parts[0].split(' ')
        weight = int(weight[1:-1])
        if len(parts) == 2:
            children = parts[1].split(', ')
        else:
            children = []
        programs[program] = [weight, children]
    return programs


def part1(programs: dict) -> str:
    all_children = []
    for program in programs:
        all_children += programs[program][1]
    for program in programs:
        if program not in all_children:
            return program
    return ''


def is_balanced(weights: List[int]) -> (bool, int, int):
    if not weights:
        return True, 0, 0
    weight_count = Counter(weights)
    if len(weight_count) != 1:
        odd_number, num_of_most = 0, 0
        for num in weight_count:
            if weight_count[num] == 1:
                odd_number = num
            else:
                num_of_most = num
        diff = num_of_most - odd_number
        idx = weights.index(odd_number)
        return False, diff, idx
    return True, 0, 0


def calculate_weights(programs: dict, root: str) -> int:
    my_weight = programs[root][0]
    children = programs[root][1]
    child_weights = []
    for child in children:
        child_weights.append(calculate_weights(programs, child))
    balanced, diff, idx = is_balanced(child_weights)
    if not balanced:
        unbalanced_child = children[idx]
        after_balance = programs[unbalanced_child][0] + diff
        print(f'Part 2: Balance: {children[idx]} by: {diff} resulting in: {after_balance}')
        exit(0)
    return my_weight + sum(child_weights)


def part2(programs: dict, root: str):
    calculate_weights(programs, root)


def main():
    programs = parse_input('input/day7.txt')
    root = part1(programs)
    print(f'Part 1: {root}')
    part2(programs, root)


if __name__ == "__main__":
    main()
