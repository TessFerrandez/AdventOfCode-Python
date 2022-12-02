from ComputerV4 import Computer, InputInterrupt, OutputInterrupt
import numpy as np
import matplotlib.pyplot as plt

BALL = 4
PADDEL = 3


def build_board(code):
    board = np.zeros((26, 37))
    step = 0

    computer = Computer(code)
    while not computer.done:
        try:
            computer.run()
        except OutputInterrupt:
            step += 1
            if step == 3:
                tile = computer.outputs.pop()
                y = computer.outputs.pop()
                x = computer.outputs.pop()
                board[y][x] = tile
                step = 0

    return board


def play_game(code):
    board = np.zeros((26, 37))
    step = 0
    ball_x = 0
    paddel_x = 0
    score = 0

    computer = Computer(code)
    computer.memory[0] = 2

    while not computer.done:
        try:
            computer.run()
        except InputInterrupt:
            if ball_x == paddel_x:
                computer.inputs.append(0)
            elif ball_x < paddel_x:
                computer.inputs.append(-1)
            else:
                computer.inputs.append(1)
        except OutputInterrupt:
            step += 1
            if step == 3:
                tile = computer.outputs.pop()
                y = computer.outputs.pop()
                x = computer.outputs.pop()

                if x == -1 and y == 0:
                    score = tile
                else:
                    board[y][x] = tile

                if tile == BALL:
                    ball_x = x
                elif tile == PADDEL:
                    paddel_x = x

                step = 0

    return score


code = open('2019/input/day13.txt').read().strip()

board = build_board(code)
print("Part 1:", np.count_nonzero(board[board == 2]))

plt.imshow(board)
plt.show()

score = play_game(code)
print("Part 2:", score)
