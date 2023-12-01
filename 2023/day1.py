from input_processing import read_data


def parse(data):
    return data.splitlines()


def get_numbers(line):
    return [int(n) for n in list(line) if n.isnumeric()]


def get_first_number(line):
    if line[0].isnumeric():
        return int(line[0])
    if line.startswith('one'):
        return 1
    if line.startswith('two'):
        return 2
    if line.startswith('three'):
        return 3
    if line.startswith('four'):
        return 4
    if line.startswith('five'):
        return 5
    if line.startswith('six'):
        return 6
    if line.startswith('seven'):
        return 7
    if line.startswith('eight'):
        return 8
    if line.startswith('nine'):
        return 9
    return get_first_number(line[1:])


def get_last_number(line):
    if line[-1].isnumeric():
        return int(line[-1])
    if line.endswith('one'):
        return 1
    if line.endswith('two'):
        return 2
    if line.endswith('three'):
        return 3
    if line.endswith('four'):
        return 4
    if line.endswith('five'):
        return 5
    if line.endswith('six'):
        return 6
    if line.endswith('seven'):
        return 7
    if line.endswith('eight'):
        return 8
    if line.endswith('nine'):
        return 9
    return get_last_number(line[:-1])


def get_numbers2(line):
    first_number = get_first_number(line)
    last_number = get_last_number(line)
    return first_number * 10 + last_number


def part1(data):
    all_numbers = list(map(get_numbers, data))
    return sum(numbers[0] * 10 + numbers[-1] for numbers in all_numbers)


def part2(data):
    return sum(map(get_numbers2, data))


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
