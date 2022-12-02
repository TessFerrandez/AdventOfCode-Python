from collections import defaultdict
from ComputerV4 import Computer, InputInterrupt, OutputInterrupt
import numpy as np
import matplotlib.pyplot as plt


sample_input = '''..#..........
..#..........
#######...###
#.#...#...#.#
#############
..#...#...#..
..#####...^..'''


def get_raw_grid(code):
    computer = Computer(code)
    raw_grid = ""

    while not computer.done:
        try:
            computer.run()
        except OutputInterrupt:
            raw_grid += chr(computer.outputs.pop())

    return raw_grid


def create_grid(raw_input):
    grid = defaultdict(lambda: '.')
    x, y = 0, 0
    start = 0

    for y, line in enumerate(raw_input.strip().splitlines()):
        for x, char in enumerate(line):
            if char != '.':
                grid[x + y * 1j] = char
            if char == "^":
                start = x + y * 1j

    return grid, x + 1, y + 1, start


def get_intersections(grid):
    intersections = []

    for pos, char in grid.items():
        if char == "#":
            if (pos + 1j) in grid and (pos - 1j) in grid and (pos + 1) in grid and (pos - 1) in grid:
                intersections.append(pos)

    return intersections


def get_alignment_sum(grid):
    intersections = get_intersections(grid)
    return sum(int(i.real) * int(i.imag) for i in intersections)


def print_grid(grid, width, heigh):
    image = np.zeros((heigh, width))

    for pos, char in grid.items():
        x, y = int(pos.real), int(pos.imag)
        if char == "#":
            image[y][x] = 1
        elif char == "^":
            image[y][x] = 2

    plt.imshow(image)
    plt.show()


def get_path(grid, start):
    direction = -1j
    pos = start
    done = False
    path = ""

    while not done:
        steps = 0
        while (pos + direction) in grid:
            pos += direction
            steps += 1

        path += str(steps) + ","

        if pos + (direction * 1j) in grid:
            direction *= 1j
            path += "R,"
        elif pos + (direction * -1j) in grid:
            direction *= -1j
            path += "L,"
        else:
            done = True

    return path[2:-1]


def encode_inputs(inputs):
    return [ord(ch) for ch in inputs]


def move_rumba(code, inputs):
    rumba = Computer(code)
    rumba.memory[0] = 2

    # while inputs:
    #    rumba.inputs.append(inputs.pop())
    inputs.reverse()

    while not rumba.done:
        try:
            rumba.run()
        except InputInterrupt:
            rumba.inputs.append(inputs.pop())
        except OutputInterrupt:
            # print(chr(rumba.outputs.pop()), end='')
            pass

    return rumba.outputs.pop()


code = open('2019/input/day17.txt').read().strip()
raw_grid = get_raw_grid(code)

grid, width, heigh, start = create_grid(raw_grid)

# PART 1
print("Part 1:", get_alignment_sum(grid))
# print_grid(grid, width, heigh)

# PART 2
path = get_path(grid, start)
# print("Path:", path)

'''
L,8,R,12,R,12,R,10, R,10,R,12,R,10,
L,8,R,12,R,12,R,10, R,10,R,12,R,10,
L,10,R,10,L,6,
L,10,R,10,L,6,
R,10,R,12,R,10,
L,8,R,12,R,12,R,10, R,10,R,12,R,10,
L,10,R,10,L,6

which can be described as:'''

inputs = '''A,B,A,B,C,C,B,A,B,C
L,8,R,12,R,12,R,10
R,10,R,12,R,10
L,10,R,10,L,6
n
'''
result = move_rumba(code, encode_inputs(inputs))
print("Part 2:", result)
