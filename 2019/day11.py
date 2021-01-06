import numpy as np
import matplotlib.pyplot as plt
from typing import List
from Computer import Computer, InputInterrupt, OutputInterrupt
from collections import defaultdict


def parse_input(filename: str) -> List[int]:
    return [int(d) for d in open(filename).read().strip().split(',')]


def part1(code: List[int]) -> int:
    grid = defaultdict(int)
    position = 0
    direction = -1j

    read_color = True

    computer = Computer(code)
    while not computer.done:
        try:
            computer.run()
        except InputInterrupt:
            # send in the color at the current spot
            computer.inputs.append(grid[position])
        except OutputInterrupt:
            value = computer.outputs[-1]
            if read_color:
                # get the color to paint - and paint
                grid[position] = value
            else:
                # read direction - change direction - and move forward 1 step
                direction = direction * -1j if value == 0 else direction * 1j
                position += direction
            read_color = not read_color

    # return the visited squares
    return len(grid)


def part2(code: List[int]) -> int:
    grid = defaultdict(int)
    position = 0
    grid[0] = 1
    direction = -1j

    read_color = True

    computer = Computer(code)
    while not computer.done:
        try:
            computer.run()
        except InputInterrupt:
            # send in the color at the current spot
            computer.inputs.append(grid[position])
        except OutputInterrupt:
            value = computer.outputs[-1]
            if read_color:
                # get the color to paint - and paint
                grid[position] = value
            else:
                # read direction - change direction - and move forward 1 step
                direction = direction * -1j if value == 0 else direction * 1j
                position += direction
            read_color = not read_color

    positions = grid.keys()

    min_x = int(min(position.real for position in positions))
    max_x = int(max(position.real for position in positions))
    min_y = int(min(position.imag for position in positions))
    max_y = int(max(position.imag for position in positions))

    board = np.zeros((max_y - min_y + 1, max_x - min_x + 1))
    for pos in grid:
        if grid[pos] == 1:
            board[int(pos.imag) - min_y][int(pos.real) - min_x] = 1

    plt.imshow(board)
    plt.show()

    return len(grid)


def main():
    code = parse_input('input/day11.txt')
    print(f'Part 1: {part1(code)}')
    code = parse_input('input/day11.txt')
    print(f'Part 2: {part2(code)}')


if __name__ == "__main__":
    main()
