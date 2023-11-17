import numpy as np
from input_processing import read_data


def parse(input):
    lines = input.splitlines()
    trees = np.zeros((len(lines), len(lines[0])), dtype=int)
    for i, line in enumerate(lines):
        trees[i, :] = np.array(list(line))
    return trees


def part1(trees):
    rows, cols = trees.shape

    def can_see_from_left():
        return ((trees[row, :col] - trees[row, col]) < 0).all()

    def can_see_from_right():
        return ((trees[row, col + 1:] - trees[row, col]) < 0).all()

    def can_see_from_north():
        return ((trees[:row, col] - trees[row, col]) < 0).all()

    def can_see_from_south():
        return ((trees[row + 1:, col] - trees[row, col]) < 0).all()

    # edges are visible
    visible_trees = 2 * rows + 2 * cols - 4

    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if can_see_from_left() or can_see_from_right() or can_see_from_north() or can_see_from_south():
                visible_trees += 1

    return visible_trees


def part2(trees):
    rows, cols = trees.shape

    def can_see(range, current):
        seen = 0

        for tree in range:
            seen += 1
            if tree >= current:
                break

        return seen

    max_score = 0
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            can_see_left = can_see(trees[row, :col][::-1], trees[row, col])
            can_see_right = can_see(trees[row, col + 1:], trees[row, col])
            can_see_up = can_see(trees[:row, col][::-1], trees[row, col])
            can_see_down = can_see(trees[row + 1:, col], trees[row, col])
            score = can_see_left * can_see_right * can_see_up * can_see_down
            max_score = max(score, max_score)

    return max_score


def test():
    sample = """30373
25512
65332
33549
35390"""
    trees = parse(sample)
    assert part1(trees) == 21
    assert part2(trees) == 8


test()
trees = parse(read_data(2022, 8))
print('Part1:', part1(trees))
print('Part2:', part2(trees))
