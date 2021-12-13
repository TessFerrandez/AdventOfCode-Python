import numpy as np
import matplotlib.pyplot as plt


def parse_input():
    points, folds = [], []
    max_x, max_y = 0, 0

    lines = [line.strip() for line in open('2021//input//day13.txt').readlines()]

    for line in lines:
        if ',' in line:
            sx, sy = line.split(',')
            max_x = max(max_x, int(sx))
            max_y = max(max_y, int(sy))
            points.append((int(sx), int(sy)))
        if '=' in line:
            axis = line.split('=')[0][-1]
            value = int(line.split('=')[1])
            folds.append((axis, value))

    grid = np.zeros((max_y + 1, max_x + 1))
    for point in points:
        grid[point[1], point[0]] = 1

    return grid, folds


def fold_grid(grid, axis, value):
    if axis == 'x':
        folded_grid = grid[:, :value] + grid[:, :-value - 1:-1]
    elif axis == 'y':
        folded_grid = grid[:value, :] + grid[:-value - 1:-1, :]
    return folded_grid


grid, folds = parse_input()

# fold along y
axis, value = folds[0]
folded_grid = fold_grid(grid, axis, value)
print("Part 1:", np.count_nonzero(folded_grid))

# fold along x
for axis, value in folds:
    grid = fold_grid(grid, axis, value)

# plot the grid
grid[grid > 0] = 1
plt.imshow(grid)
plt.show()
