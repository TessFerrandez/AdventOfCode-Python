import numpy as np
import matplotlib.pyplot as plt


def parse_input():
    point_section, fold_section = open('2021//input//day13.txt').read().split('\n\n')
    points = [list(map(int, line.split(','))) for line in point_section.split('\n')]
    max_x, max_y = max(p[0] for p in points), max(p[1] for p in points)
    folds = [(line.split('=')[0][-1], int(line.split('=')[1])) for line in fold_section.strip().split('\n')]

    paper = np.zeros((max_y + 1, max_x + 1))
    for point in points:
        paper[point[1], point[0]] = 1

    return paper, folds


def fold_paper(paper: np.ndarray, axis: str, value: int) -> np.ndarray:
    if axis == 'x':
        return paper[:, :value] + paper[:, :-value - 1:-1]
    else:
        return paper[:value, :] + paper[:-value - 1:-1, :]


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
