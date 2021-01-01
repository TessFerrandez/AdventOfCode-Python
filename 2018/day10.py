import numpy as np
from typing import List
from common.helpers import extract_numbers
import matplotlib.pyplot as plt


def parse_input(filename: str) -> List[List[int]]:
    return [extract_numbers(line.strip()) for line in open(filename).readlines()]


def calculate_box_size(points: List[List[int]]) -> int:
    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    min_y = min([p[1] for p in points])
    max_y = max([p[1] for p in points])
    return max_x - min_x + max_y - min_y


def part1(points: List[List[int]]) -> int:

    # the minimum size is the place where the squares are the most
    # concentrated - we go from big to minimum to expanding

    iteration = 0
    box_size = calculate_box_size(points)
    while True:
        iteration += 1
        for point in points:
            point[0] += point[2]
            point[1] += point[3]

        new_box_size = calculate_box_size(points)
        if new_box_size > box_size:
            break
        else:
            box_size = new_box_size

    # we hit the first time we expand - so roll back one
    for point in points:
        point[0] -= point[2]
        point[1] -= point[3]
    iteration -= 1

    return iteration


def draw_grid(points: List[List[int]]):
    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    min_y = min([p[1] for p in points])
    max_y = max([p[1] for p in points])

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    grid = np.zeros((height, width))
    for point in points:
        x, y, _, _ = point
        grid[y - min_y][x - min_x] = 1

    plt.imshow(grid)
    plt.show()


def main():
    points = parse_input('input/day10.txt')
    iteration = part1(points)
    print('Part 1: SEE IMAGE')
    draw_grid(points)
    print(f'Part 2: {iteration}')


if __name__ == "__main__":
    main()
