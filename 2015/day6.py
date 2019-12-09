import re
import numpy as np


def execute_commands(commands, height=1000, width=1000):
    height = 1000
    width = 1000
    screen = np.zeros((height, width))
    for command in commands:
        p = re.split(r"[ ,]", command)
        if p[0] == "toggle":
            for x in range(int(p[1]), int(p[4])+1):
                for y in range(int(p[2]), int(p[5])+1):
                    screen[x][y] = 1 - screen[x][y]
        else:
            val = 0
            if p[1] == "on":
                val = 1
            for x in range(int(p[2]), int(p[5])+1):
                for y in range(int(p[3]), int(p[6])+1):
                    screen[x][y] = val
    return screen


def execute_commands_v2(commands, height=1000, width=1000):
    screen = np.zeros((height, width))
    for command in commands:
        p = re.split(r"[ ,]", command)
        if p[0] == "toggle":
            for x in range(int(p[1]), int(p[4]) + 1):
                for y in range(int(p[2]), int(p[5]) + 1):
                    screen[x][y] += 2
        else:
            val = -1
            if p[1] == "on":
                val = 1
            for x in range(int(p[2]), int(p[5]) + 1):
                for y in range(int(p[3]), int(p[6]) + 1):
                    screen[x][y] = max(screen[x][y] + val, 0)
    return screen


def get_num_lit(screen, height=1000, width=1000):
    num_lit = 0
    for x in range(0, height):
        for y in range(0, width):
            num_lit += screen[x][y]
    return num_lit


def puzzle1():
    screen = execute_commands(open('input/day6.txt'))
    print("num lit: ", get_num_lit(screen))


def puzzle2():
    screen = execute_commands_v2(open('input/day6.txt'))
    print("num lit: ", get_num_lit(screen))


if __name__ == "__main__":
    puzzle1()
    puzzle2()