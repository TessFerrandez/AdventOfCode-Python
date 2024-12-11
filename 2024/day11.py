from functools import cache
from input_processing import read_data


def parse(data):
    return [int(d) for d in data.split()]


@cache
def count(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return count(1, steps - 1)
    str_stone = str(stone)
    if len(str_stone) % 2 == 0:
        half = len(str_stone) // 2
        return count(int(str_stone[:half]), steps - 1) + count(int(str_stone[half:]), steps - 1)
    return count(stone * 2024, steps - 1)


def part1(data):
    return sum(count(stone, 25) for stone in data)


def part2(data):
    return sum(count(stone, 75) for stone in data)


def test():
    data = '''125 17'''
    assert part1(parse(data)) == 55312


test()
data = read_data(2024, 11)
print('Part1:', part1(parse(data)))
print('Part2:', part2(parse(data)))
