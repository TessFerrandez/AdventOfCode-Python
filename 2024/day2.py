from input_processing import read_data, get_numbers_from_lines


def parse(data):
    return get_numbers_from_lines(data)


def is_safe(report):
    increasing = report[1] > report[0]

    if increasing:
        for i in range(1, len(report)):
            diff = report[i] - report[i - 1]
            if not (1 <= diff <= 3):
                return False
        return True
    else:
        for i in range(1, len(report)):
            diff = report[i] - report[i - 1]
            if not (-3 <= diff <= -1):
                return False
        return True


def part1(data):
    valid = 0
    for report in data:
        valid += is_safe(report)

    return valid


def is_really_safe(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        if is_safe(report[: i] + report[i + 1:]):
            return True
    return False


def part2(data):
    valid = 0
    for report in data:
        valid += is_really_safe(report)

    return valid


def test():
    data = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''
    assert part1(parse(data)) == 2
    assert part2(parse(data)) == 4


test()
data = read_data(2024, 2)
print('Part1:', part1(parse(data)))
print('Part2:', part2(parse(data)))
