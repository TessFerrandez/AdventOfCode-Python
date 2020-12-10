import pytest
from itertools import combinations
from typing import List


@pytest.mark.parametrize('data, target, expected',
                         [
                             ([20, 15, 10, 5, 5], 25, 4),
                         ])
def test_part1(data: List[int], target: int, expected: int):
    assert part1(data, target) == expected


@pytest.mark.parametrize('data, target, expected',
                         [
                             ([20, 15, 10, 5, 5], 25, 3),
                         ])
def test_part2(data: List[int], target: int, expected: int):
    assert part2(data, target) == expected


def parse_input(filename: str):
    return [int(line) for line in open(filename).readlines()]


def find_sum_combos(data: List[int], target: int) -> List[List[int]]:
    combos = []
    for i in range(len(data)):
        for combo in combinations(data, i):
            if sum(combo) == target:
                combos.append(combo)
    return combos


def part1(data: List[int], target: int) -> int:
    combos = find_sum_combos(data, target)
    return len(combos)


def part2(data: List[int], target: int) -> int:
    combos = find_sum_combos(data, target)
    lengths = [len(combo) for combo in combos]
    lengths.sort()
    return lengths.count(lengths[0])


def main():
    data = parse_input('input/day17.txt')
    print(f'Part 1: {part1(data, 150)}')
    print(f'Part 2: {part2(data, 150)}')


if __name__ == "__main__":
    main()
