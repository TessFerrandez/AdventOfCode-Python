from typing import List, Tuple
import numpy as np


def expand(pre: np.array, post: np.array) -> List[Tuple]:
    rules = []

    for i in range(4):
        rot = np.rot90(pre, k=i)
        rules.append((rot.flatten(), post))
        rules.append((np.fliplr(rot).flatten(), post))
        rules.append((np.flipud(rot).flatten(), post))

    return rules


def parse_input(filename: str) -> (List, List):
    rules2, rules3 = [], []
    lines = [line.strip() for line in open(filename).readlines()]
    for line in lines:
        pre, post = line.split(' => ')
        pre = pre.replace('/', '')
        post = post.replace('/', '')
        pre = np.array([1 if c == '#' else 0 for c in pre])
        post = np.array([1 if c == '#' else 0 for c in post])

        if len(pre) == 4:
            rules2 += expand(pre.reshape((2, 2)), post.reshape((3, 3)))
        else:
            rules3 += expand(pre.reshape((3, 3)), post.reshape((4, 4)))

    return rules2, rules3


def match(in_cell: np.array, rules: List):
    for pre, post in rules:
        if np.allclose(in_cell.flatten(), pre):
            return post


def iterate(grid: np.array, rules2: List, rules3: List) -> np.array:
    size = len(grid)

    if size % 2 == 0:
        steps = size // 2
        new_grid = np.zeros((3 * steps, 3 * steps))
        for row in range(steps):
            for col in range(steps):
                in_cell = grid[2 * row: 2 * row + 2, 2 * col: 2 * col + 2].copy()
                out_cell = match(in_cell, rules2)
                new_grid[3 * row: 3 * row + 3, 3 * col: 3 * col + 3] = out_cell
    else:
        steps = size // 3
        new_grid = np.zeros((4 * steps, 4 * steps))
        for row in range(steps):
            for col in range(steps):
                in_cell = grid[3 * row: 3 * row + 3, 3 * col: 3 * col + 3].copy()
                out_cell = match(in_cell, rules3)
                new_grid[4 * row: 4 * row + 4, 4 * col: 4 * col + 4] = out_cell

    return new_grid


def part1(initial_state: str, iterations: int, rules2: List, rules3: List) -> int:
    grid = np.array([int(c) for c in initial_state]).reshape((3, 3))
    for i in range(iterations):
        grid = iterate(grid, rules2, rules3)
        print(i, np.count_nonzero(grid == 1))
    return np.count_nonzero(grid == 1)


def main():
    rules2, rules3 = parse_input('input/day21.txt')
    initial_state = '010001111'
    print(f'Part 1: {part1(initial_state, 5, rules2, rules3)}')
    print(f'Part 2: {part1(initial_state, 18, rules2, rules3)}')


if __name__ == "__main__":
    main()
