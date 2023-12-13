from input_processing import read_data


def parse_grid(grid_base):
    rows = grid_base.splitlines()

    row_nums = [sum(2 ** i for i, ch in enumerate(row[::-1]) if ch == '#') for row in rows]
    col_nums = []
    for col in range(len(rows[0])):
        col_num = sum(2 ** i for i, row in enumerate(rows) if row[col] == '#')
        col_nums.append(col_num)

    return row_nums, col_nums


def parse(data):
    return [parse_grid(grid_base) for grid_base in data.split('\n\n')]


def is_match(nums, low, high):
    while low < high:
        if nums[low] != nums[high]:
            return False
        low += 1
        high -= 1
    return True


def get_fold(nums):
    n = len(nums)
    half = n // 2

    folds = 0

    for i in range(half):
        # from front -- ex 0|1 01|23 012|345 ...
        if is_match(nums, 0, 2 * i + 1):
            folds += i + 1
        # from back -- ex 7|8 56|78 345|678 ... if 8 items
        if is_match(nums, n - 2 - 2 * i, n - 1):
            folds += n - 1 - i

    return folds


def part1(grids):
    total = 0

    for rows, cols in grids:
        total += 100 * get_fold(rows)
        total += get_fold(cols)

    return total


def is_power_of_2(n):
    return n != 0 and n & (n - 1) == 0


def is_one_bit_diff(num1, num2):
    return is_power_of_2(num1 ^ num2)


def is_match_with_smudge(nums, low, high):
    smudges = 0
    while low < high:
        if nums[low] != nums[high]:
            if smudges == 0 and is_one_bit_diff(nums[low], nums[high]):
                smudges += 1
            else:
                return False
        low += 1
        high -= 1
    return smudges == 1


def get_fold2(nums):
    n = len(nums)
    half = n // 2

    folds = 0

    for i in range(half):
        # from front -- ex 0|1 01|23 012|345 ...
        if is_match_with_smudge(nums, 0, 2 * i + 1):
            folds += i + 1
        # from back -- ex 7|8 56|78 345|678 ... if 8 items
        if is_match_with_smudge(nums, n - 2 - 2 * i, n - 1):
            folds += n - 1 - i

    return folds


def part2(grids):
    total = 0

    for rows, cols in grids:
        total += 100 * get_fold2(rows)
        total += get_fold2(cols)

    return total


def test():
    sample = '''#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#'''
    grids = parse(sample)
    assert part1(grids) == 405
    assert part2(grids) == 400


test()
data = read_data(2023, 13)
grids = parse(data)
print('Part1:', part1(grids))
print('Part2:', part2(grids))
