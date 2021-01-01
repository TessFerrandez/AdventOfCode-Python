import re
import numpy as np
from typing import List


def parse_input(filename: str) -> List[List[int]]:
    return [[int(d) for d in re.findall(r'\d+', line.strip())] for line in open(filename).readlines()]


def part1(claims: List[List[int]]) -> int:
    grid = np.zeros((1000, 1000))

    for claim in claims:
        i, left, top, width, height = claim
        grid[top: top + height, left: left + width] += 1

    return np.count_nonzero(grid[grid > 1])


def part2(claims: List[List[int]]) -> int:
    grid = np.zeros((1000, 1000))

    for claim in claims:
        i, left, top, width, height = claim
        grid[top: top + height, left: left + width] += 1

    for claim in claims:
        i, left, top, width, height = claim
        claim_grid = grid[top: top + height, left: left + width]
        if np.count_nonzero(claim_grid[claim_grid > 1]) == 0:
            return i

    return 0


def main():
    claims = parse_input('input/day3.txt')
    print(f'Part 1: {part1(claims)}')
    print(f'Part 2: {part2(claims)}')


if __name__ == "__main__":
    main()
