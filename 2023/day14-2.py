# solution based on h9419's solution
from input_processing import read_data
import numpy as np


EMPTY = 0
ROUND = 1
CUBE = 2


def parse(data):
    grid = np.array([list(row) for row in data.splitlines()])
    grid_int = np.zeros(grid.shape, dtype=int)
    grid_int[grid == 'O'] = ROUND
    grid_int[grid == '#'] = CUBE
    return grid_int


def tilt_west(grid):
    new_grid = []
    for row in grid:
        last_empty = 0
        new_row = row.copy()
        for idx, slot in enumerate(row):
            if idx >= last_empty and slot == ROUND:
                new_row[idx] = 0
                new_row[last_empty] = 1
                last_empty += 1
            if slot == CUBE:
                last_empty = idx + 1
        new_grid.append(new_row)
    return np.array(new_grid)


def tilt_north(grid):
    return tilt_west(grid.transpose((1, 0))).transpose((1, 0))


def calculate_weight(grid):
    return np.sum(grid.shape[0] - np.where(grid == ROUND)[0])


def part1(grid):
    return calculate_weight(tilt_north(grid))


def hash(grid):
    return np.sum(grid.reshape(-1) * 3 * np.arange(grid.size))


def tilt_east(grid):
    grid = np.flip(grid, axis=1)
    grid = tilt_west(grid)
    grid = np.flip(grid, axis=1)
    return grid


def tilt_south(grid):
    grid = np.flip(grid, axis=0)
    grid = tilt_north(grid)
    grid = np.flip(grid, axis=0)
    return grid


cache = {}


def cycle(grid):
    global cache
    key = hash(grid)
    if key in cache.keys():
        return cache[key]
    new_grid = tilt_east(tilt_south(tilt_west(tilt_north(grid))))
    cache[key] = new_grid
    return new_grid


def part2(data):
    hits = {}
    grid = parse(data)

    for i in range(1000):
        key = hash(grid)
        if key in cache.keys():
            initial_cycle = hits[key] + 1
            cycle_size = i - hits[key]
            real_iterations = initial_cycle + (1000000000 - initial_cycle) % cycle_size
            break
        grid = cycle(grid)
        hits[key] = i

    grid = parse(data)

    for _ in range(real_iterations):
        grid = cycle(grid)

    return calculate_weight(grid)


def test():
    sample = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''
    grid = parse(sample)
    assert part1(grid) == 136
    assert part2(sample) == 64


test()
data = read_data(2023, 14)
grid = parse(data)
print('Part1:', part1(grid))
print('Part2:', part2(data))
