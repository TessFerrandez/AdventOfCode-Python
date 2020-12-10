import numpy as np
from copy import deepcopy


def parse_input(filename: str) -> np.array:
    lines = [line.strip() for line in open(filename).readlines()]
    size = len(lines)
    grid = np.zeros((size, size))

    for i in range(size):
        for j in range(size):
            grid[i][j] = 1 if lines[i][j] == '#' else 0
    return grid


def inc(grid: np.array, corner_lock: bool):
    old_grid = deepcopy(grid)
    size = len(grid)
    for row in range(size):
        for col in range(size):
            if corner_lock and ((row == 0 and col == 0) or (row == 0 and col == size - 1) or (row == size - 1 and col == 0) or (row == size - 1 and col == size - 1)):
                continue
            adjacent = np.sum(old_grid[max(row - 1, 0):min(row + 2, size), max(col - 1, 0):min(col + 2, size)])
            if old_grid[row][col] == 1 and adjacent not in [3.0, 4.0]:
                grid[row][col] = 0
            elif old_grid[row][col] == 0 and adjacent == 3.0:
                grid[row][col] = 1


def part1(grid: np.array, iterations: int) -> int:
    for i in range(iterations):
        inc(grid, False)
    return int(np.sum(grid))


def part2(grid: np.array, iterations: int) -> int:
    size = len(grid)
    grid[0][0] = 1
    grid[0][size - 1] = 1
    grid[size - 1][0] = 1
    grid[size - 1][size - 1] = 1
    for i in range(iterations):
        inc(grid, True)
    return int(np.sum(grid))


def main():
    grid = parse_input('input/day18.txt')
    print(f'Part 1: {part1(grid, 100)}')
    grid = parse_input('input/day18.txt')
    print(f'Part 2: {part2(grid, 100)}')


if __name__ == "__main__":
    main()
