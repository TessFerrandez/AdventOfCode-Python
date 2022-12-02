from collections import deque
from typing import Dict, Tuple, Union
import numpy as np
import matplotlib.pyplot as plt


def get_neighbors(grid, current, key_ring):
    possible = [current + dir for dir in [-1j, 1, 1j, -1]]

    neighbors = []
    for neighbor in possible:
        if grid[neighbor] == "#":
            continue
        if grid[neighbor] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and grid[neighbor].lower() not in key_ring:
            continue

        if grid[neighbor] in "abcdefghijklmnopqrstuvwxyz" and grid[neighbor] not in key_ring:
            new_key_ring = key_ring + grid[neighbor]
            new_key_ring = ''.join(sorted(new_key_ring))
            neighbors.append((neighbor, new_key_ring))
        else:
            neighbors.append((neighbor, key_ring))

    return neighbors


def get_shortest_path(start, grid, all_keys):
    todo = deque([(start, "")])
    previous: Dict[Tuple[complex, str], Union[Tuple[complex, str], None]] = {(start, ""): None}

    target = None

    while todo:
        current, key_ring = todo.popleft()
        if key_ring == all_keys:
            target = (current, key_ring)
            break

        for neighbor in get_neighbors(grid, current, key_ring):
            if neighbor not in previous:
                previous[neighbor] = (current, key_ring)
                todo.append(neighbor)

    # target was never found
    if not target:
        return []

    # build path
    path = []
    current = target

    while current:
        path.append(current)
        current = previous[current]

    path.reverse()
    return path


def parse_grid(raw_input):
    grid = {}
    keys = ""
    start = 0

    lines = raw_input.strip().splitlines()

    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == "@":
                ch = "."
                start = x + y * 1j
            if ch in 'abcdefghijklmnopqrstuvwxyz':
                keys += ch
            grid[x + y * 1j] = ch

    keys = ''.join(sorted(keys))

    return grid, start, keys, len(lines[0]), len(lines)


def print_grid(grid, width, height, start):
    image = np.zeros((height, width))

    for pos, char in grid.items():
        x, y = int(pos.real), int(pos.imag)
        if char == ".":
            continue
        elif char == "#":
            image[y][x] = 1
        elif char in 'abcdefghijklmnopqrstuvwxyz':
            image[y][x] = 2
        elif char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            image[y][x] = 3

    startx, starty = int(start.real), int(start.imag)
    image[starty][startx] = 4

    plt.imshow(image)
    plt.show()


def block_blinds(grid):
    did_something = True

    while did_something:
        did_something = False
        for pos, ch in grid.items():
            if ch == ".":
                neighbors = [pos + dir for dir in [-1j, 1, 1j, -1]]
                if sum(1 if grid[neighbor] == "#" else 0 for neighbor in neighbors) == 3:
                    grid[pos] = "#"
                    did_something = True

    return grid


raw_input1 = '''#########
#b.A.@.a#
#########'''

raw_input2 = '''########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################'''

raw_input3 = '''#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################'''

raw_input = open('2019/input/day18.txt').read()

grid, start, keys, width, height = parse_grid(raw_input)
grid = block_blinds(grid)
shortest_path = get_shortest_path(start, grid, keys)

print("Part 1:", len(shortest_path) - 1)
