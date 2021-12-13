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

    paper = np.zeros((max_y + 1, max_x + 1))
    for point in points:
        paper[point[1], point[0]] = 1

    return paper, folds


def fold_paper(paper, axis, value):
    if axis == 'x':
        folded_paper = paper[:, :value] + paper[:, :-value - 1:-1]
    elif axis == 'y':
        folded_paper = paper[:value, :] + paper[:-value - 1:-1, :]
    return folded_paper


paper, folds = parse_input()

# make one fold
axis, value = folds[0]
folded_paper = fold_paper(paper, axis, value)
print("Part 1:", np.count_nonzero(folded_paper))

# origami the heck out of the paper
for axis, value in folds:
    paper = fold_paper(paper, axis, value)

# plot the paper
paper[paper > 0] = 1
plt.imshow(paper)
plt.show()
