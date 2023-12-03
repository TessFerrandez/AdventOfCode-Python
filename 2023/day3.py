import re
from input_processing import read_data


def parse(data):
    rows = data.splitlines()

    numbers = [(int(number.group()), set((r, c) for c in range(*number.span())))
               for r, row in enumerate(rows)
               for number in re.finditer(r'\d+', row)]

    symbols = set((r, c, ch)
                  for r, row in enumerate(rows)
                  for c, ch in enumerate(row)
                  if not ch.isdigit() and ch != '.')

    return numbers, symbols


def part1(numbers, symbols):
    neighbors = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1), (0, 1),
                 (1, -1), (1, 0), (1, 1)]
    symbol_neighbors = set((r + dr, c + dc)
                           for dr, dc in neighbors
                           for r, c, _ in symbols)
    return sum(number for number, span in numbers if span & symbol_neighbors)


def part2(numbers, symbols):
    neighbors = [(-1, -1), (-1, 0), (-1, 1),
                 (0, -1), (0, 1),
                 (1, -1), (1, 0), (1, 1)]
    gears = [(r, c) for r, c, ch in symbols if ch == '*']
    gear_neighbors = [set((r + dr, c + dc) for dr, dc in neighbors) for r, c in gears]

    total = 0
    for neighborhood in gear_neighbors:
        nums = [number for number, span in numbers if span & neighborhood]
        if len(nums) == 2:
            total += nums[0] * nums[1]

    return total


def test():
    sample = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''
    numbers, symbols = parse(sample)
    assert part1(numbers, symbols) == 4361
    assert part2(numbers, symbols) == 467835


test()
data = read_data(2023, 3)
numbers, symbols = parse(data)
print('Part1:', part1(numbers, symbols))
print('Part2:', part2(numbers, symbols))
