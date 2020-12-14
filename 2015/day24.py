import pytest
from typing import List
from itertools import combinations
from functools import reduce


@pytest.mark.parametrize('packages, expected',
                         [
                             ([1, 2, 3, 4, 5, 7, 8, 9, 10, 11], 99),
                         ])
def test_part1(packages: List[int], expected: int):
    assert part1(packages) == expected


@pytest.mark.parametrize('packages, expected',
                         [
                             ([1, 2, 3, 4, 5, 7, 8, 9, 10, 11], 44),
                         ])
def test_part2(packages: List[int], expected: int):
    assert part2(packages) == expected


def parse_input(filename: str) -> List[int]:
    return [int(package.strip()) for package in open(filename).readlines()]


def find_smallest_qe(packages: List[int], n_groups: int) -> int:
    total_weight = sum(packages)
    group_weight = total_weight // n_groups

    smallest_combos = []
    for length in range(0, len(packages) + 1):
        for combo in combinations(packages, length):
            if sum(combo) == group_weight:
                smallest_combos.append(combo)
        if smallest_combos:
            break

    smallest_qe = float('inf')
    for combo in smallest_combos:
        qe = reduce((lambda x, y: x * y), combo)
        if qe < smallest_qe:
            smallest_qe = qe

    return smallest_qe


def part1(packages: List[int]) -> int:
    return find_smallest_qe(packages, 3)


def part2(packages: List[int]) -> int:
    return find_smallest_qe(packages, 4)


def main():
    packages = parse_input('input/day24.txt')
    print(f'Part 1: {part1(packages)}')
    print(f'Part 2: {part2(packages)}')


if __name__ == "__main__":
    main()
