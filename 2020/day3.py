from typing import List


def parse_input():
    with open("input/day3.txt") as f:
        return [line.strip() for line in f.readlines()]


def calculate_trees(grid: List[str], slope_x: int, slope_y: int) -> int:
    x, y = 0, 0
    h, w = len(grid), len(grid[0])

    num_trees = 0
    while y < h - slope_y:
        x = (x + slope_x) % w
        y = y + slope_y
        if grid[y][x] == "#":
            num_trees += 1
    return num_trees


def puzzle1(grid: List[str]) -> int:
    return calculate_trees(grid, 3, 1)


def puzzle2(grid: List[str]) -> int:
    return (
        calculate_trees(grid, 1, 1)
        * calculate_trees(grid, 3, 1)
        * calculate_trees(grid, 5, 1)
        * calculate_trees(grid, 7, 1)
        * calculate_trees(grid, 1, 2)
    )


def main():
    grid = parse_input()
    puzzle1_result = puzzle1(grid)
    print(f"Puzzle 1: {puzzle1_result}")
    puzzle2_result = puzzle2(grid)
    print(f"Puzzle 2: {puzzle2_result}")


if __name__ == "__main__":
    main()
