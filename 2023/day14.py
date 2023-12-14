from input_processing import read_data
from bisect import bisect_left


def parse(data):
    rows = data.splitlines()
    num_cols = len(rows[0])
    num_rows = len(rows)

    cubes = []
    round = []

    for r, row in enumerate(rows):
        for c, ch in enumerate(row):
            if ch == '#':
                cubes.append((r, c))
            if ch == 'O':
                round.append((r, c))

    return cubes, round, num_rows, num_cols


def get_stones_per_col(cubes, n_cols, add_first=False, add_last=False):
    if add_first:
        stones_per_col = [[-1] for _ in range(n_cols)]
    else:
        stones_per_col = [[] for _ in range(n_cols)]

    for r, c in cubes:
        stones_per_col[c].append(r)

    if add_last:
        for col in stones_per_col:
            col.append(n_cols)

    return stones_per_col


def get_stones_per_row(cubes, n_rows, add_first=False, add_last=False):
    if add_first:
        stones_per_row = [[-1] for _ in range(n_rows)]
    else:
        stones_per_row = [[] for _ in range(n_rows)]

    for r, c in cubes:
        stones_per_row[r].append(c)

    if add_last:
        for row in stones_per_row:
            row.append(n_rows)

    return stones_per_row


def part1(cube_pos, round_pos, n_rows, n_cols):
    round = tilt_north(cube_pos, round_pos, n_cols)
    return sum(n_rows - r for r, _ in round)


def tilt_north(cube_pos, round_pos, n_cols):
    cubes = get_stones_per_col(cube_pos, n_cols, add_first=True)
    round = get_stones_per_col(round_pos, n_cols)

    final_pos = [[] for _ in range(n_cols)]
    for col in range(n_cols):
        for stone in round[col]:
            blocking_cube = bisect_left(cubes[col], stone)
            final_pos[col].append(cubes[col][blocking_cube - 1] + 1)

    new_round = []
    for col in final_pos:
        for i in range(1, len(col)):
            if col[i] <= col[i - 1]:
                col[i] = col[i - 1] + 1

    for c, col in enumerate(final_pos):
        for r in col:
            new_round.append((r, c))

    return new_round


def tilt_west(cube_pos, round_pos, n_rows):
    cubes = get_stones_per_row(cube_pos, n_rows, add_first=True)
    round = get_stones_per_row(round_pos, n_rows)

    final_pos = [[] for _ in range(n_rows)]
    for row in range(n_rows):
        for stone in round[row]:
            blocking_cube = bisect_left(cubes[row], stone)
            final_pos[row].append(cubes[row][blocking_cube - 1] + 1)

    new_round = []
    for row in final_pos:
        for i in range(1, len(row)):
            if row[i] <= row[i - 1]:
                row[i] = row[i - 1] + 1

    for r, row in enumerate(final_pos):
        for c in row:
            new_round.append((r, c))

    return new_round


def tilt_south(cube_pos, round_pos, n_cols):
    cubes = get_stones_per_col(cube_pos, n_cols, add_last=True)
    round = get_stones_per_col(round_pos, n_cols)

    final_pos = [[] for _ in range(n_cols)]
    for col in range(n_cols):
        for stone in round[col]:
            blocking_cube = bisect_left(cubes[col], stone)
            final_pos[col].append(cubes[col][blocking_cube] - 1)

    new_round = []
    for col in final_pos:
        for i in range(len(col) - 2, -1, -1):
            if col[i] >= col[i + 1]:
                col[i] = col[i + 1] - 1

    for c, col in enumerate(final_pos):
        for r in col:
            new_round.append((r, c))

    return new_round


def tilt_east(cube_pos, round_pos, n_rows):
    cubes = get_stones_per_row(cube_pos, n_rows, add_last=True)
    round = get_stones_per_row(round_pos, n_rows)

    final_pos = [[] for _ in range(n_rows)]
    for row in range(n_rows):
        for stone in round[row]:
            blocking_cube = bisect_left(cubes[row], stone)
            final_pos[row].append(cubes[row][blocking_cube] - 1)

    new_round = []
    for row in final_pos:
        for i in range(len(row) - 2, -1, -1):
            if row[i] >= row[i + 1]:
                row[i] = row[i + 1] - 1

    for r, row in enumerate(final_pos):
        for c in row:
            new_round.append((r, c))

    return new_round


def part2(cubes, round, n_rows, n_cols, cycle):
    loads = []
    for _ in range(200):
        round = tilt_north(cubes, round, n_cols)
        round = tilt_west(cubes, round, n_rows)
        round = tilt_south(cubes, round, n_cols)
        round = tilt_east(cubes, round, n_rows)
        loads.append(sum(n_rows - r for r, _ in round))

    cycle_start = 199 - cycle
    cycle_pos = (1000000000 - 199) % cycle
    return loads[cycle_start + cycle_pos - 1]


def test():
    sample = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''
    cubes, round, num_rows, num_cols = parse(sample)
    print(part1(cubes, round, num_rows, num_cols))
    print(part2(cubes, round, num_rows, num_cols, cycle=7))


test()
data = read_data(2023, 14)
cubes, round, num_rows, num_cols = parse(data)
print('Part1:', part1(cubes, round, num_rows, num_cols))
print('Part2:', part2(cubes, round, num_rows, num_cols, cycle=52))
