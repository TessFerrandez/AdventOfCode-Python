from typing import List
from Computer import Computer, InputInterrupt, OutputInterrupt
import numpy as np
import matplotlib.pyplot as plt


BLOCK = 2
PADDLE = 3
BALL = 4

LEFT = -1
NEUTRAL = 0
RIGHT = 1


def parse_input(filename: str) -> List[int]:
    return [int(d) for d in open(filename).read().strip().split(',')]


def part1(code: List[int]) -> int:
    display = np.zeros((37, 37))

    computer = Computer(code)
    output_values = []
    while not computer.done:
        try:
            computer.run()
        except InputInterrupt:
            computer.inputs.append(0)
        except OutputInterrupt:
            output_values.append(computer.outputs[-1])
            # wait for 3 consecutive outputs
            if len(output_values) == 3:
                x, y, tile = output_values
                display[y][x] = tile
                output_values.clear()

    plt.imshow(display)
    plt.show()
    return np.count_nonzero(display[display == BLOCK])


def part2(code: List[int]) -> int:
    display = np.zeros((37, 37))
    computer = Computer(code)

    # enter 2 coins
    computer.code[0] = 2

    # set up x positions for ball and paddle
    ball_x = 0
    paddle_x = 0

    # set up initial score
    score = 0

    output_values = []
    while not computer.done:
        try:
            computer.run()
        except InputInterrupt:
            if ball_x < paddle_x:
                computer.inputs.append(LEFT)
            elif ball_x > paddle_x:
                computer.inputs.append(RIGHT)
            else:
                computer.inputs.append(NEUTRAL)
        except OutputInterrupt:
            output_values.append(computer.outputs[-1])
            if len(output_values) == 3:
                x, y, tile = output_values
                if x == -1 and y == 0:
                    score = tile
                else:
                    display[y][x] = tile
                if tile == BALL:
                    ball_x = x
                elif tile == PADDLE:
                    paddle_x = x
                output_values.clear()

    plt.imshow(display)
    plt.show()
    return score


def main():
    code = parse_input('input/day13.txt')
    print(f'Part 1: {part1(code)}')
    code = parse_input('input/day13.txt')
    print(f'Part 2: {part2(code)}')


if __name__ == "__main__":
    main()
