import numpy as np


OPEN = 0
TREE = 1
LUMBER = 2

SIZE = 10


def print_grid(grid: np.array):
    symbols = {OPEN: ".", TREE: "|", LUMBER: "#"}
    for line in grid:
        for tile in line:
            print(symbols[tile], end="")
        print()
    print()


def parse_input(filename: str) -> np.array:
    global SIZE

    lines = [line.strip() for line in open(filename).readlines()]
    SIZE = len(lines)
    grid = np.zeros((SIZE, SIZE))

    symbols = {".": OPEN, "|": TREE, "#": LUMBER}
    for y, line in enumerate(lines):
        for x, tile in enumerate(line):
            grid[y][x] = symbols[tile]

    return grid


def get_adjacent(grid: np.array, x: int, y: int, tile: int):
    x_from, x_to = max(0, x - 1), min(x + 1, SIZE)
    y_from, y_to = max(0, y - 1), min(y + 1, SIZE)
    adjacent = grid[y_from : y_to + 1, x_from : x_to + 1]
    return np.sum(adjacent == tile)


def puzzle1(grid: np.array, minutes: int) -> int:
    for i in range(minutes):
        grid_copy = grid.copy()
        for y, row in enumerate(grid):
            for x, tile in enumerate(row):
                if tile == OPEN:
                    if get_adjacent(grid_copy, x, y, TREE) >= 3:
                        grid[y][x] = TREE
                elif tile == TREE:
                    if get_adjacent(grid_copy, x, y, LUMBER) >= 3:
                        grid[y][x] = LUMBER
                elif tile == LUMBER:
                    if (
                        get_adjacent(grid_copy, x, y, LUMBER) >= 2
                        and get_adjacent(grid_copy, x, y, TREE) >= 1
                    ):
                        grid[y][x] = LUMBER
                    else:
                        grid[y][x] = OPEN
        # print_grid(grid)
        if i % 1000 == 0:
            print(i)

    trees = np.sum(grid == TREE)
    lumber = np.sum(grid == LUMBER)
    return trees * lumber


def main():
    grid = parse_input("input/day18.txt")
    puzzle1_result = puzzle1(grid, 10)
    print(f"Puzzle 1: {puzzle1_result}")
    print("Puzzle 2: Takes an unreasonable long time - have to get back to this")


if __name__ == "__main__":
    main()
