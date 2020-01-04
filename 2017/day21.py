import numpy as np
from collections import Counter


rules2 = []
rules3 = []


def expand(pre, post):
    rules = []

    for k in range(4):
        rot = np.rot90(pre, k=k)
        rules.append((rot.flatten(), post))
        rules.append((np.fliplr(rot).flatten(), post))
        rules.append((np.flipud(rot).flatten(), post))

    return rules


def match(incell, rules):
    for pre, post in rules:
        if np.allclose(incell.flatten(), pre):
            return post
    assert False


def iterate(grid):
    size = len(grid)
    if size % 2 == 0:
        steps = size // 2
        new_grid = np.zeros((3 * steps, 3 * steps))
        for row in range(steps):
            for col in range(steps):
                incell = grid[2 * row : 2 * row + 2, 2 * col : 2 * col + 2].copy()
                outcell = match(incell, rules2)
                new_grid[3 * row : 3 * row + 3, 3 * col : 3 * col + 3] = outcell.copy()
    elif size % 3 == 0:
        steps = size // 3
        new_grid = np.zeros((4 * steps, 4 * steps))
        for row in range(steps):
            for col in range(steps):
                incell = grid[3 * row : 3 * row + 3, 3 * col : 3 * col + 3].copy()
                outcell = match(incell, rules3)
                new_grid[4 * row : 4 * row + 4, 4 * col : 4 * col + 4] = outcell.copy()
    else:
        assert False
    return new_grid


def read_input():
    global rules2
    global rules3

    lines = [line.strip() for line in open("input/day21.txt").readlines()]
    for line in lines:
        pre, post = line.split(" => ")
        pre = pre.replace("/", "")
        post = post.replace("/", "")
        pre = np.array([1 if c == "#" else 0 for c in pre])
        post = np.array([1 if c == "#" else 0 for c in post])

        if len(pre) == 4:
            rules2 += expand(pre.reshape((2, 2)), post.reshape((3, 3)))
        elif len(pre) == 9:
            rules3 += expand(pre.reshape((3, 3)), post.reshape((4, 4)))
        else:
            assert False


def count_ones(initial_state: str, num_iterations: int) -> int:
    grid = np.array([int(c) for c in initial_state]).reshape((3, 3))
    for i in range(num_iterations):
        grid = iterate(grid)
        print(i, np.count_nonzero(grid == 1))
    return np.count_nonzero(grid == 1)


def puzzles():
    read_input()
    initial_state = "010001111"
    print("ones:", count_ones(initial_state, 5))
    print("ones:", count_ones(initial_state, 18))


if __name__ == "__main__":
    puzzles()
