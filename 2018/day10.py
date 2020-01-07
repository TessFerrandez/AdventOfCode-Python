import re
import numpy as np
import matplotlib.pyplot as plt


def get_min_max_x_y(data, step) -> (int, int, int, int):
    minx = min(x + step * vx for (x, y, vx, vy) in data)
    maxx = max(x + step * vx for (x, y, vx, vy) in data)
    miny = min(y + step * vy for (x, y, vx, vy) in data)
    maxy = max(y + step * vy for (x, y, vx, vy) in data)
    return minx, maxx, miny, maxy


def puzzle1():
    data = [
        [int(num) for num in re.findall(r"-?\d+", line)]
        for line in open("input/day10.txt").readlines()
    ]

    boxes = []
    for i in range(20000):
        minx, maxx, miny, maxy = get_min_max_x_y(data, i)
        boxes.append(maxx - minx + maxy - miny)

    min_box = min(boxes)
    i = boxes.index(min_box)
    minx, maxx, miny, maxy = get_min_max_x_y(data, i)

    grid = np.zeros((maxy - miny + 1, maxx - minx + 1), int)
    for (x, y, vx, vy) in data:
        grid[y + i * vy - miny][x + i * vx - minx] = 1

    print(i)
    plt.imshow(grid)
    plt.show()


if __name__ == "__main__":
    puzzle1()
