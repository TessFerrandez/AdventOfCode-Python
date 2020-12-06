import pytest
from typing import List
from common.helpers import extract_numbers


@pytest.mark.parametrize('data, expected',
                         [
                             ([[2, 3, 4]], 58),
                             ([[4, 3, 2]], 58),
                             ([[1, 1, 10]], 43),
                             ([[2, 3, 4], [1, 1, 10]], 101),
                         ])
def test_part1(data: List[List[int]], expected: int):
    assert part1(data) == expected


@pytest.mark.parametrize('data, expected',
                         [
                             ([[2, 3, 4]], 34),
                             ([[4, 3, 2]], 34),
                             ([[1, 1, 10]], 14),
                             ([[2, 3, 4], [1, 1, 10]], 48),
                         ])
def test_part2(data: List[List[int]], expected: int):
    assert part2(data) == expected


def parse_input(filename: str) -> List[List[int]]:
    return [extract_numbers(line) for line in open(filename).readlines()]


def part1(data: List[List[int]]) -> int:
    total_paper = 0
    for present in data:
        l, w, h = sorted(present)
        paper = 2 * (l * w) + 2 * (w * h) + 2 * (l * h) + (l * w)
        total_paper += paper
    return total_paper


def part2(data: List[List[int]]) -> int:
    total_ribbon = 0
    for present in data:
        l, w, h = sorted(present)
        ribbon = 2 * l + 2 * w + l * w * h
        total_ribbon += ribbon
    return total_ribbon


def main():
    data = parse_input('input/day2.txt')
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == "__main__":
    main()
