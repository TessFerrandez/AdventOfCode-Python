from typing import List
import matplotlib.pyplot as plt
import numpy as np


OPEN = 0
TREE = 1
LUMBER = 2


def parse_input(filename: str) -> List[str]:
    lines = open(filename).read().splitlines()
    return lines


def iterate(grid: np.array):
    original = grid.copy()
    height, width = len(grid), len(grid[0])

    for y in range(height - 2):
        for x in range(width - 2):
            sub = original[y: y + 3, x: x + 3]
            if original[y + 1][x + 1] == OPEN:
                if np.count_nonzero(sub[sub == TREE]) >= 3:
                    grid[y + 1][x + 1] = TREE
            elif original[y + 1][x + 1] == TREE:
                if np.count_nonzero(sub[sub == LUMBER]) >= 3:
                    grid[y + 1][x + 1] = LUMBER
            elif original[y + 1][x + 1] == LUMBER:
                if np.count_nonzero(sub[sub == LUMBER]) >= 2 and np.count_nonzero(sub[sub == TREE]) >= 1:
                    grid[y + 1][x + 1] = LUMBER
                else:
                    grid[y + 1][x + 1] = OPEN


def part1(lines: List[str]) -> int:
    grid = generate_grid(lines)

    for i in range(10):
        iterate(grid)

    return np.count_nonzero(grid[grid == 1]) * np.count_nonzero(grid[grid == 2])


def part2(lines: List[str]) -> int:
    grid = generate_grid(lines)
    resource_values = {}

    fig, axs = plt.subplots(4, 14)

    # pattern repeats from 417 to 444
    for i in range(0, 473):
        iterate(grid)
        if 417 <= i:
            axs[(i - 417) // 14, (i - 417) % 14].imshow(grid)
            resource_value = np.count_nonzero(grid[grid == 1]) * np.count_nonzero(grid[grid == 2])
            resource_values[i - 417] = resource_value
    plt.show()

    return resource_values[((1000000000 - 417 - 1) % 56)]


def generate_grid(lines: List[str]) -> np.array:
    height, width = len(lines), len(lines[0])
    grid = np.zeros((height + 2, width + 2))
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == '#':
                grid[y + 1][x + 1] = LUMBER
            elif ch == '|':
                grid[y + 1][x + 1] = TREE
    return grid


def main():
    lines = parse_input('input/day18.txt')
    print(f'Part 1: {part1(lines)}')
    print(f'Part 2: {part2(lines)}')


if __name__ == "__main__":
    main()
