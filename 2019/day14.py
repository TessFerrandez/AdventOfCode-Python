from collections import defaultdict
from math import ceil


def parse_input(filename: str):
    lines = [line.strip().split(' => ') for line in open(filename).readlines()]
    reactions = {}
    for line in lines:
        parts, target = line
        target_amount, target_chemical = target.split(' ')
        target_amount = int(target_amount)
        components = []
        for component in parts.split(', '):
            amount, chemical = component.split(' ')
            components.append([int(amount), chemical])
        reactions[target_chemical] = (target_amount, components)
    return reactions


def get_fuel(reactions: dict, num_fuel: int) -> int:
    resources = defaultdict(int)
    ore_needed = 0
    needs = [[component[0] * num_fuel, component[1]] for component in reactions['FUEL'][1]]
    while needs:
        amount, chemical = needs.pop(-1)
        if chemical == 'ORE':
            ore_needed += amount
            continue
        if resources[chemical] > amount:
            resources[chemical] -= amount
            amount = 0
        else:
            amount -= resources[chemical]
            resources[chemical] = 0
        reaction_amount, components = reactions[chemical]
        num_reactions = ceil(amount / reaction_amount)
        reaction_rest = (num_reactions * reaction_amount) - amount
        resources[chemical] += reaction_rest
        for component in components:
            needs.append([num_reactions * component[0], component[1]])
    return ore_needed


def part1(reactions: dict) -> int:
    return get_fuel(reactions, 1)


def part2(reactions: dict) -> int:
    ore = 1000000000000

    upper_bound = None
    lower_bound = 1

    while lower_bound + 1 != upper_bound:
        if upper_bound is None:
            guess = lower_bound * 2
        else:
            guess = (upper_bound + lower_bound) // 2

        ore_needed = get_fuel(reactions, guess)
        if ore_needed > ore:
            upper_bound = guess
        else:
            lower_bound = guess

    return lower_bound


def main():
    reactions = parse_input('input/day14.txt')
    print(f'Part 1: {part1(reactions)}')
    print(f'Part 2: {part2(reactions)}')


if __name__ == "__main__":
    main()
