from input_processing import read_data, get_numbers_from_lines
import matplotlib.pyplot as plt
import numpy as np


def parse(data):
    return set(tuple(row) for row in get_numbers_from_lines(data))


def part1(droplet):
    surface_areas = 0

    for x, y, z in droplet:
        for dx, dy, dz in (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1):
            if (x + dx, y + dy, z + dz) not in droplet:
                surface_areas += 1

    return surface_areas


def print_droplet_mri(levels):
    fig = plt.figure(figsize=(10, 10))

    for idx, level in levels.items():
        fig.add_subplot(5, 4, idx + 1)
        plt.imshow(level)

    plt.show()


def get_x_levels(droplet, max_x, max_y, max_z):
    levels = {}

    for level_x in range(1, max_x + 1):
        level = np.zeros((max_y + 1, max_z + 1))
        for x, y, z in droplet:
            if x == level_x:
                level[y, z] = 1
        levels[level_x] = level

    return levels


def get_z_levels(droplet, max_x, max_y, max_z):
    levels = {}

    for level_z in range(1, max_z + 1):
        level = np.zeros((max_x + 1, max_y + 1))
        for x, y, z in droplet:
            if z == level_z:
                level[x, y] = 1
        levels[level_z] = level

    return levels


def get_surrounded(level):
    outsides = set()

    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return
        if level[row, col] == 1:
            return
        if (row, col) in outsides:
            return
        outsides.add((row, col))
        dfs(row - 1, col)
        dfs(row + 1, col)
        dfs(row, col - 1)
        dfs(row, col + 1)

    rows, cols = level.shape
    for row in range(rows):
        dfs(row, 0)
        dfs(row, cols - 1)
    for col in range(cols):
        dfs(0, col)
        dfs(rows - 1, col)

    return set([(row, col) for row in range(rows) for col in range(cols) if level[row, col] == 0 and (row, col) not in outsides])


def get_x_surrounded(levels):
    surrounded = set()

    for x in levels:
        surrounded_in_level = get_surrounded(levels[x])
        for y, z in surrounded_in_level:
            surrounded.add((x, y, z))

    return surrounded


def get_z_surrounded(levels):
    surrounded = set()

    for z in levels:
        surrounded_in_level = get_surrounded(levels[z])
        for x, y in surrounded_in_level:
            surrounded.add((x, y, z))

    return surrounded


def part2(droplet, display_mri=False):
    max_x = max(x for x, y, z in droplet)
    max_y = max(y for x, y, z in droplet)
    max_z = max(z for x, y, z in droplet)

    x_levels = get_x_levels(droplet, max_x, max_y, max_z)
    z_levels = get_z_levels(droplet, max_x, max_y, max_z)

    if display_mri:
        print_droplet_mri(x_levels)
        print_droplet_mri(z_levels)

    yz_surrounded = get_x_surrounded(x_levels)
    xy_surrounded = get_z_surrounded(z_levels)
    surrounded = xy_surrounded & yz_surrounded

    # for cube in droplet
    # count exposed walls that are not facing completely surrounded air
    surface_areas = 0

    for x, y, z in droplet:
        for dx, dy, dz in (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1):
            cube = (x + dx, y + dy, z + dz)
            if cube not in droplet and cube not in surrounded:
                surface_areas += 1

    return surface_areas


def test():
    sample = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""
    data = parse(sample)
    assert part1(data) == 64
    assert part2(data) == 58


test()
data = parse(read_data(2022, 18))
print('Part1:', part1(data))
print('Part2:', part2(data, True))
