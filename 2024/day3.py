import re
from input_processing import read_data


def parse(data):
    return data


def multiply(data):
    multiplication_statements = re.findall(r"mul\([\d]+,[\d]+\)", data)
    total = 0
    for statement in multiplication_statements:
        x, y = map(int, re.findall(r"[\d]+", statement))
        total += x * y
    return total


def part1(data):
    multiplication_statements = re.findall(r"mul\([\d]+,[\d]+\)", data)
    total = 0
    for statement in multiplication_statements:
        x, y = map(int, re.findall(r"[\d]+", statement))
        total += x * y
    return total


def part2(data):
    do_pos = 0
    do_strings = []

    while do_pos != -1:
        dont_pos = data.find("don't()", do_pos)
        do_strings.append(data[do_pos: dont_pos])
        do_pos = data.find("do()", dont_pos)

    return sum(multiply(do_string) for do_string in do_strings)


def test():
    data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    assert part1(parse(data)) == 161
    data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    assert part2(parse(data)) == 48


test()
data = read_data(2024, 3)
print('Part1:', part1(parse(data)))
print('Part2:', part2(parse(data)))
