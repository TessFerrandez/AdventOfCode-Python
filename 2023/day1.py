import re
from input_processing import read_data


def parse(data):
    return data.splitlines()


def get_calibration_value(line):
    pattern = re.compile(r'\d')
    numbers = pattern.findall(line)
    return int(numbers[0]) * 10 + int(numbers[-1])


def get_calibration_value_ex(line):
    nums = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    pattern = re.compile(r'(one|two|three|four|five|six|seven|eight|nine|\d)')
    numbers = pattern.findall(line)
    return int(''.join(nums.get(num, num) for num in [numbers[0], numbers[-1]]))


def part1(data):
    return sum(map(get_calibration_value, data))


def part2(data):
    return sum(map(get_calibration_value_ex, data))


def test():
    sample_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
    assert part1(parse(sample_input)) == 142
    sample_input2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    assert part2(parse(sample_input2)) == 281


test()
data = read_data(2023, 1)
print('Part1:', part1(parse(data)))
print('Part2:', part2(parse(data)))
