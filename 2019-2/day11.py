from collections import defaultdict
from typing import DefaultDict
from ComputerV4 import Computer, InputInterrupt, OutputInterrupt
import numpy as np
import matplotlib.pyplot as plt


code = open('2019/input/day11.txt').read().strip()


def process_moves(start_color: int) -> DefaultDict[complex, int]:
    grid = defaultdict(lambda: 0)
    grid[0] = start_color
    position = 0
    direction = 1j

    get_color = True

    computer = Computer(code)

    while not computer.done:
        try:
            computer.run()
        except InputInterrupt:
            computer.inputs.append(grid[position])
        except OutputInterrupt:
            out = computer.outputs.pop()
            if get_color:
                grid[position] = out
            else:
                direction = direction * 1j if out == 0 else direction * -1j
                position += direction
            get_color = not get_color

    return grid


def print_grid(grid):
    min_x, max_x = 0, 0
    min_y, max_y = 0, 0

    for pos in grid:
        x, y = int(pos.real), int(pos.imag)
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    image = np.zeros((height, width))
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            image[min_y - y + max_y - 1][x] = grid[x + y * 1j]

    plt.imshow(image)
    plt.show()


grid = process_moves(0)
print("Part 1:", len(grid))

grid = process_moves(1)
print("Part 2:")
print_grid(grid)
