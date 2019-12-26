# https://github.com/vesche/adventofcode-2017/blob/master/day03.py
from typing import List, Tuple

coords: List[Tuple[int, int]] = [
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
]


def calculate_steps(number: int) -> int:
    x = y = dx = 0
    dy = -1
    step = 0

    while True:
        step += 1
        if number == step:
            return abs(x) + abs(y)
        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy


def calculate_next_num(number: int) -> int:
    x = y = dx = 0
    dy = -1
    grid = {}

    while True:
        total = 0
        for offset in coords:
            ox, oy = offset
            if (x + ox, y + oy) in grid:
                total += grid[(x + ox, y + oy)]
        if total > int(number):
            return total
        if (x, y) == (0, 0):
            grid[(0, 0)] = 1
        else:
            grid[(x, y)] = total
        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy


def puzzles():
    print("steps:", calculate_steps(368078))
    print("next num:", calculate_next_num(368078))


if __name__ == "__main__":
    puzzles()
