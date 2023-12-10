# based on https://www.reddit.com/r/adventofcode/comments/1883ibu/2023_day_1_solutions/
# replace 2nd char of all words with the number
from input_processing import read_data


def parse(data):
    lines = data.splitlines()
    return lines


def part1(lines):
    numbers = []

    for line in lines:
        numbers.append([int(ch) for ch in [*line] if ch.isdigit()])

    return sum(nums[0] * 10 + nums[-1] for nums in numbers)


def part2(lines):
    numbers = []
    translate = {'zero': 'z0o', 'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}

    for line in lines:
        for key, value in translate.items():
            line = line.replace(key, value)
        numbers.append([int(ch) for ch in [*line] if ch.isdigit()])

    return sum(nums[0] * 10 + nums[-1] for nums in numbers)


def test():
    sample = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''
    assert part1(parse(sample)) == 142

    sample2 = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''
    assert part2(parse(sample2)) == 281


test()
data = read_data(2023, 1)
print('Part1:', part1(parse(data)))
print('Part2:', part2(parse(data)))
