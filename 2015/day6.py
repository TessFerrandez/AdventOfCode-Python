import pytest
import numpy as np
from common.helpers import extract_numbers
from typing import List


TURN_ON = 0
TURN_OFF = 1
TOGGLE = 2


@pytest.mark.parametrize('data, expected',
                         [
                             ([[0, 0, 999, 999, TURN_ON]], 1000000),
                             ([[0, 0, 999, 0, TOGGLE]], 1000),
                             ([[0, 0, 999, 999, TURN_ON], [499, 499, 500, 500, TURN_OFF]], 999996),
                         ])
def test_part1(data: List[List[int]], expected: int):
    assert part1(data) == expected


@pytest.mark.parametrize('data, expected',
                         [
                             ([[0, 0, 0, 0, TURN_ON]], 1),
                             ([[0, 0, 999, 999, TOGGLE]], 2000000),
                         ])
def test_part2(data: List[List[int]], expected: int):
    assert part2(data) == expected


def parse_input(filename: str):
    instructions = []
    lines = [line.strip() for line in open(filename).readlines()]
    for line in lines:
        digits = extract_numbers(line)
        if line.startswith('turn on'):
            digits.append(TURN_ON)
        elif line.startswith('turn off'):
            digits.append(TURN_OFF)
        else:
            digits.append(TOGGLE)
        instructions.append(digits)
    return instructions


def part1(data: List[List[int]]) -> int:
    grid = np.zeros((1000, 1000))
    for instruction in data:
        x1, y1, x2, y2, op = instruction
        if op == TURN_ON:
            grid[y1: y2 + 1, x1: x2 + 1] = 1
        elif op == TURN_OFF:
            grid[y1: y2 + 1, x1: x2 + 1] = 0
        else:
            grid[y1: y2 + 1, x1: x2 + 1] = 1 - grid[y1: y2 + 1, x1: x2 + 1]
    return np.count_nonzero(grid == 1)


def part2(data: List[List[int]]) -> int:
    grid = np.zeros((1000, 1000))
    for instruction in data:
        x1, y1, x2, y2, op = instruction
        if op == TURN_ON:
            grid[y1: y2 + 1, x1: x2 + 1] = grid[y1: y2 + 1, x1: x2 + 1] + 1
        elif op == TURN_OFF:
            for y in range(y1, y2 + 1):
                for x in range(x1, x2 + 1):
                    grid[y][x] = max(0, grid[y][x] - 1)
        else:
            grid[y1: y2 + 1, x1: x2 + 1] = grid[y1: y2 + 1, x1: x2 + 1] + 2
    return int(np.sum(grid))


def main():
    data = parse_input('input/day6.txt')
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == "__main__":
    main()
