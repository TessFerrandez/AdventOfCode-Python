from ComputerV4 import Computer, OutputInterrupt, InputInterrupt
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple


def get_tile(droid: Computer, param: int) -> int:
    try:
        droid.run()
    except InputInterrupt:
        droid.inputs.append(param)

    try:
        droid.run()
    except OutputInterrupt:
        return droid.outputs.pop()


WALL = 0
EMPTY = 1
WALKABLE = -1
OXYGEN = 2

DIRECTIONS = [1, 4, 2, 3]
DIRECTION = [-1j, 1, 1j, -1]


def explore_world(code):
    droid = Computer(code)

    dir_i = 0
    origin = 0
    position = 0
    world = {}
    fully_explored = False
    found_oxygen = False
    path = [origin]
    oxygen = 0

    while not fully_explored:
        new_position = position + DIRECTION[dir_i]

        if new_position == origin:
            fully_explored = True

        tile = get_tile(droid, DIRECTIONS[dir_i])

        if tile == WALL:
            dir_i = (dir_i + 1) % 4
            world[new_position] = WALL
        elif tile == EMPTY or tile == OXYGEN:
            if new_position in world:
                if not found_oxygen:
                    path.pop()
            else:
                world[new_position] = tile
                if tile == OXYGEN:
                    found_oxygen = True
                    oxygen = new_position
                if not found_oxygen:
                    path.append(new_position)
            dir_i = (dir_i - 1) % 4
            position = new_position

    return world, path, oxygen


def oxygenate_world(world, oxygen):
    todo: List[Tuple[int, complex]] = [(0, oxygen)]
    max_minutes = 0

    while todo:
        minutes, pos = todo.pop()
        world[pos] = minutes
        max_minutes = max(minutes, max_minutes)
        for d in [-1j, 1, 1j, -1]:
            if world[pos + d] == EMPTY:
                todo.append((minutes + 1, pos + d))

    return max_minutes


def print_world(world, oxygen):
    minx, maxx = min(int(pos.real) for pos in world), max(int(pos.real) for pos in world)
    miny, maxy = min(int(pos.imag) for pos in world), max(int(pos.imag) for pos in world)
    xoff, yoff = abs(minx), abs(miny)

    image = np.zeros((maxy - miny + 1, maxx - minx + 1))
    for pos, tile in world.items():
        x, y = int(pos.real) + xoff, int(pos.imag) + yoff
        image[y][x] = tile
    # image[int(oxygen.imag)][int(oxygen.real)] = 2

    plt.imshow(image)
    plt.show()


def print_world2(world, oxygen):
    minx, maxx = min(int(pos.real) for pos in world), max(int(pos.real) for pos in world)
    miny, maxy = min(int(pos.imag) for pos in world), max(int(pos.imag) for pos in world)

    # xs = set(int(pos.real) for pos in world)
    # ys = set(int(pos.imag) for pos in world)

    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            if oxygen == (x + y * 1j):
                print('O', end='')
            elif (x + y * 1j) not in world:
                print('#', end='')
            elif world[x + y * 1j] == -1:
                print('.', end='')
            else:
                print('#', end='')
        print()


code = open('2019/input/day15.txt').read().strip()
world, path, oxygen = explore_world(code)
print("Part 1:", len(path))

print_world(world, oxygen)

minutes = oxygenate_world(world, oxygen)
print("Part 2:", minutes)
