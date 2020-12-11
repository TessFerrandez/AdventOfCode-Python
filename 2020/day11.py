import pytest
import numpy as np
from copy import copy
import progressbar
from typing import List


@pytest.mark.parametrize('layout, row, col, expected',
                         [
                             (['.......#.',
                               '...#.....',
                               '.#.......',
                               '.........',
                               '..#L....#',
                               '....#....',
                               '.........',
                               '#........',
                               '...#.....'],
                              4, 3, 8),
                             (['.............',
                               '.L.L.#.#.#.#.',
                               '.............'],
                              1, 1, 0),
                             (['.##.##.',
                               '#.#.#.#',
                               '##...##',
                               '...L...',
                               '##...##',
                               '#.#.#.#',
                               '.##.##.'],
                              3, 3, 0),
                         ])
def test_get_visible_occupied(layout: List[str], row: int, col: int, expected: int):
    # arrange
    grid, height, width = grid_from_layout(layout)

    # act and assert
    assert get_visible_occupied(grid, row, col, height, width) == expected


def grid_from_layout(layout: List[str]) -> (np.array, int, int):
    height = len(layout)
    width = len(layout[0])
    grid = np.zeros((height, width))
    for row in range(height):
        for col in range(width):
            if layout[row][col] == 'L':
                grid[row][col] = 1
            if layout[row][col] == '#':
                grid[row][col] = 2
    return grid, height, width


def parse_input(filename: str) -> (np.array, int, int):
    lines = [line.strip() for line in open(filename).readlines()]
    return grid_from_layout(lines)


def get_adjacent_occupied(grid: np.array, row: int, col: int, height: int, width: int) -> int:
    min_row, min_col = max(0, row - 1), max(0, col - 1)
    max_row, max_col = min(row + 1, height - 1), min(col + 1, width - 1)
    sum_occupied = 0
    for r in range(min_row, max_row + 1):
        for c in range(min_col, max_col + 1):
            if r == row and c == col:
                continue
            if grid[r][c] == 2:
                sum_occupied += 1
    return sum_occupied


def get_visible_occupied(grid: np.array, row: int, col: int, height: int, width: int) -> int:
    sum_occupied = 0

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            x, y = col + dx, row + dy
            while 0 <= x < width and 0 <= y < height:
                if grid[y][x] == 1:
                    break
                if grid[y][x] == 2:
                    sum_occupied += 1
                    break
                x, y = x + dx, y + dy

    return sum_occupied


def iterate_adjacent(grid: np.array, height: int, width: int) -> bool:
    old_grid = copy(grid)
    changed = False
    for row in range(height):
        for col in range(width):
            if old_grid[row][col] == 1 and get_adjacent_occupied(old_grid, row, col, height, width) == 0:
                grid[row][col] = 2
                changed = True
            if old_grid[row][col] == 2 and get_adjacent_occupied(old_grid, row, col, height, width) >= 4:
                grid[row][col] = 1
                changed = True
    return changed


def iterate_visible(grid: np.array, height: int, width: int) -> bool:
    old_grid = copy(grid)
    changed = False
    for row in range(height):
        for col in range(width):
            if old_grid[row][col] == 1 and get_visible_occupied(old_grid, row, col, height, width) == 0:
                grid[row][col] = 2
                changed = True
            if old_grid[row][col] == 2 and get_visible_occupied(old_grid, row, col, height, width) >= 5:
                grid[row][col] = 1
                changed = True
    return changed


def count_occupied(grid: np.array) -> int:
    return len(grid[np.where(grid == 2)])


def part1(grid: np.array, height: int, width: int) -> int:
    iteration = 0
    with progressbar.ProgressBar(max_value=117, redirect_stdout=True) as p:
        while iterate_adjacent(grid, height, width):
            iteration += 1
            p.update(iteration)
    return count_occupied(grid)


def part2(grid: np.array, height: int, width: int) -> int:
    iteration = 0
    with progressbar.ProgressBar(max_value=85, redirect_stdout=True) as p:
        while iterate_visible(grid, height, width):
            iteration += 1
            p.update(iteration)
    return count_occupied(grid)


def main():
    grid, height, width = parse_input('input/day11.txt')
    print(f'Part 1: {part1(grid, height, width)}')
    grid, height, width = parse_input('input/day11.txt')
    print(f'Part 2: {part2(grid, height, width)}')


if __name__ == "__main__":
    main()
