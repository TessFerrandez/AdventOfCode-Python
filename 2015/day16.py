import pytest
from collections import defaultdict


def parse_input(filename: str):
    lines = [line.strip() for line in open(filename).readlines()]
    sues = {}

    for line in lines:
        _, sue_num, *properties = line.split()
        sue_num = int(sue_num[: -1])
        sues[sue_num] = defaultdict(lambda: -1)
        n_props = len(properties)
        for i in range(0, n_props - 1, 2):
            prop = properties[i][: -1]
            if i == n_props - 2:
                value = int(properties[i + 1])
            else:
                value = int(properties[i + 1][: -1])
            sues[sue_num][prop] = value
    return sues


def sue_is_ok(sue: dict) -> bool:
    evidence = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }
    for prop in evidence:
        if not (sue[prop] == evidence[prop] or sue[prop] == -1):
            return False
    return True


def part1(sues: dict) -> int:
    for sue_nr in sues:
        sue = sues[sue_nr]
        if sue_is_ok(sue):
            return sue_nr
    return 0


def sue_is_ok_too(sue: dict) -> bool:
    evidence = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }
    for prop in evidence:
        if sue[prop] == -1:
            continue
        if prop in ['cats', 'trees'] and sue[prop] <= evidence[prop]:
            return False
        elif prop in ['pomeranians', 'goldfish'] and sue[prop] >= evidence[prop]:
            return False
        elif prop not in ['cats', 'trees', 'pomeranians', 'goldfish'] and sue[prop] != evidence[prop]:
            return False
    return True


def part2(sues: dict) -> int:
    for sue_nr in sues:
        sue = sues[sue_nr]
        if sue_is_ok_too(sue):
            return sue_nr
    return 0


def main():
    sues = parse_input('input/day16.txt')
    print(f'Part 1: {part1(sues)}')
    print(f'Part 2: {part2(sues)}')


if __name__ == "__main__":
    main()
