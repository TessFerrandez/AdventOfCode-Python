from typing import List
import numpy as np
import progressbar


def parse_input(filename: str):
    initial_grid = [line.strip() for line in open(filename).readlines()]
    return initial_grid


def create_conway_cube(initial_grid: List[str], num_cycles=6) -> np.array:
    initial_size = len(initial_grid[0])
    end_size = initial_size + 2 * num_cycles
    cube = np.zeros((end_size, end_size, end_size))
    x_offset, y_offset, z_offset = num_cycles, num_cycles, num_cycles + initial_size // 2
    for y, row in enumerate(initial_grid):
        for x, ch in enumerate(row):
            if ch == '#':
                cube[y + y_offset][x + x_offset][z_offset] = 1
    return cube


def get_active_neighbors_in_cube(cube: np.array, x: int, y: int, z: int, cube_size: int) -> int:
    y_min, y_max = max(y - 1, 0), min(y + 2, cube_size)
    x_min, x_max = max(x - 1, 0), min(x + 2, cube_size)
    z_min, z_max = max(z - 1, 0), min(z + 2, cube_size)
    sum_active = np.sum(cube[y_min: y_max, x_min: x_max, z_min: z_max]) - cube[y][x][z]
    return sum_active


def iterate_3d(cube: np.array):
    original_cube = cube.copy()
    cube_size = len(cube[0])
    for y in range(cube_size):
        for x in range(cube_size):
            for z in range(cube_size):
                active = get_active_neighbors_in_cube(original_cube, x, y, z, cube_size)
                if cube[y][x][z] == 1 and active not in [2, 3]:
                    cube[y][x][z] = 0
                elif cube[y][x][z] == 0 and active == 3:
                    cube[y][x][z] = 1


def create_conway_quad(initial_grid: List[str], num_cycles=6) -> np.array:
    initial_size = len(initial_grid[0])
    end_size = initial_size + 2 * num_cycles
    quad = np.zeros((end_size, end_size, end_size, end_size))
    x_offset, y_offset, z_offset, w_offset = num_cycles, num_cycles, num_cycles, num_cycles + initial_size // 2
    for y, row in enumerate(initial_grid):
        for x, plane in enumerate(row):
            for z, ch in enumerate(plane):
                if ch == '#':
                    quad[y + y_offset][x + x_offset][z + z_offset][w_offset] = 1
    return quad


def get_active_neighbors_in_quad(quad: np.array, x: int, y: int, z: int, w: int, quad_size: int) -> int:
    y_min, y_max = max(y - 1, 0), min(y + 2, quad_size)
    x_min, x_max = max(x - 1, 0), min(x + 2, quad_size)
    z_min, z_max = max(z - 1, 0), min(z + 2, quad_size)
    w_min, w_max = max(w - 1, 0), min(w + 2, quad_size)
    sum_active = np.sum(quad[y_min: y_max, x_min: x_max, z_min: z_max, w_min: w_max]) - quad[y][x][z][w]
    return sum_active


def iterate_4d(quad: np.array):
    original_quad = quad.copy()
    quad_size = len(quad[0])
    for y in range(quad_size):
        for x in range(quad_size):
            for z in range(quad_size):
                for w in range(quad_size):
                    active = get_active_neighbors_in_quad(original_quad, x, y, z, w, quad_size)
                    if quad[y][x][z][w] == 1 and active not in [2, 3]:
                        quad[y][x][z][w] = 0
                    elif quad[y][x][z][w] == 0 and active == 3:
                        quad[y][x][z][w] = 1


def part1(initial_grid: List[str]) -> int:
    cube = create_conway_cube(initial_grid, 6)

    with progressbar.ProgressBar(max_value=6) as p:
        for i in range(6):
            iterate_3d(cube)
            p.update(i)

    return int(np.sum(cube))


def part2(initial_grid: List[str]) -> int:
    quad = create_conway_quad(initial_grid, 6)

    with progressbar.ProgressBar(max_value=6) as p:
        for i in range(6):
            iterate_4d(quad)
            p.update(i)

    return int(np.sum(quad))


def main():
    data = parse_input('input/day17.txt')
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == "__main__":
    main()
