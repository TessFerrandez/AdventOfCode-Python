from input_processing import read_data
import numpy as np


def parse(data, empty_padding=1):
    grid = np.array([list(row) for row in data.split("\n")])
    rows, cols = grid.shape

    empty_rows = [r for r, row in enumerate(grid) if np.all(row == ".")]
    empty_rows.insert(0, -1)
    empty_rows.append(rows)
    row_translation = [(empty_rows[i] + 1, empty_rows[i + 1] - 1, i) for i in range(len(empty_rows) - 1)]

    empty_cols = [c for c, col in enumerate(grid.T) if np.all(col == ".")]
    empty_cols.insert(0, -1)
    empty_cols.append(cols)
    col_translation = [(empty_cols[i] + 1, empty_cols[i + 1] - 1, i) for i in range(len(empty_cols) - 1)]

    def get_row_offset(r):
        for start, end, offset in row_translation:
            if start <= r <= end:
                return offset * empty_padding

    def get_col_offset(c):
        for start, end, offset in col_translation:
            if start <= c <= end:
                return offset * empty_padding

    galaxies = []
    for r, row in enumerate(grid):
        row_offset = get_row_offset(r)
        for c, ch in enumerate(row):
            col_offset = get_col_offset(c)
            if ch == "#":
                galaxies.append((r + row_offset, c + col_offset))

    return galaxies


def part1(galaxies):
    total = 0

    for i in range(len(galaxies)):
        x, y = galaxies[i]
        for j in range(i + 1, len(galaxies)):
            x2, y2 = galaxies[j]
            total += abs(x - x2) + abs(y - y2)

    return total


def test():
    sample = '''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....'''
    galaxies = parse(sample)
    assert part1(galaxies) == 374
    galaxies = parse(sample, 9)
    assert part1(galaxies) == 1030
    galaxies = parse(sample, 99)
    assert part1(galaxies) == 8410


test()
data = read_data(2023, 11)
galaxies = parse(data)
print('Part1:', part1(galaxies))
galaxies = parse(data, 999999)
print("Part2:", part1(galaxies))
