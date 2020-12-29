import numpy as np
from utils import knot_hash


def part1(grid: np.array) -> int:
    return int(np.sum(grid))


def part2(grid: np.array) -> int:
    regions = []

    size = len(grid)
    for y in range(size):
        for x in range(size):
            combine = []
            if grid[y][x] == 1:
                for j in range(len(regions)):
                    if (x - 1, y) in regions[j]:
                        combine.append(j)
                        break
                for j in range(len(regions)):
                    if (x, y - 1) in regions[j]:
                        combine.append(j)
                        break
                if not combine:
                    regions.append([(x, y)])
                else:
                    regions[combine[0]] += [(x, y)]
                    if len(combine) == 2 and combine[0] != combine[1]:
                        regions[combine[0]] += regions[combine[1]]
                        regions.pop(combine[1])

    return len(regions)


def build_grid(input_str: str) -> np.array:
    grid = np.zeros((128, 128))
    for y in range(128):
        hash_result = bin(int(knot_hash(f'{input_str}-{y}'), 16))[2:].zfill(128)
        for x, ch in enumerate(hash_result):
            if ch == '1':
                grid[y][x] = 1
    return grid


def build_sample_grid() -> np.array:
    grid = np.zeros((8, 8))
    grid[0][0] = 1
    grid[0][1] = 1
    grid[0][3] = 1
    grid[0][5] = 1
    grid[1][1] = 1
    grid[1][3] = 1
    grid[1][5] = 1
    grid[1][7] = 1
    grid[2][4] = 1
    grid[2][6] = 1
    grid[3][0] = 1
    grid[3][2] = 1
    grid[3][4] = 1
    grid[3][5] = 1
    grid[3][7] = 1
    grid[4][1] = 1
    grid[4][2] = 1
    grid[4][4] = 1
    grid[5][0] = 1
    grid[5][1] = 1
    grid[5][4] = 1
    grid[5][7] = 1
    grid[6][1] = 1
    grid[6][5] = 1
    grid[7][0] = 1
    grid[7][1] = 1
    grid[7][3] = 1
    grid[7][5] = 1
    grid[7][6] = 1
    return grid


def main():
    input_str = 'stpzcrnm'
    grid = build_grid(input_str)
    print(f'Part 1: {part1(grid)}')
    print(f'Part 2: {part2(grid)}')


if __name__ == "__main__":
    main()
