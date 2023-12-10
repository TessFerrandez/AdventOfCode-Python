from input_processing import read_data


def parse(data):
    return [[int(n) for n in line.split()] for line in data.split('\n')]


def get_prediction(line):
    last_values = [line[-1]]

    next_row = [b - a for a, b in zip(line, line[1:])]
    last_values.append(next_row[-1])

    while next_row.count(0) != len(next_row):
        next_row = [b - a for a, b in zip(next_row, next_row[1:])]
        last_values.append(next_row[-1])

    return sum(last_values)


def get_predecessor(line):
    first_values = [line[0]]

    next_row = [b - a for a, b in zip(line, line[1:])]
    first_values.append(next_row[0])

    while next_row.count(0) != len(next_row):
        next_row = [b - a for a, b in zip(next_row, next_row[1:])]
        first_values.append(next_row[0])

    current = 0
    while first_values:
        current = first_values.pop() - current
    return current


def part1(data):
    return sum(get_prediction(line) for line in data)


def part2(data):
    return sum(get_predecessor(line) for line in data)


def test():
    sample = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''
    assert part1(parse(sample)) == 114
    assert part2(parse(sample)) == 2


test()
data = read_data(2023, 9)
print('Part1:', part1(parse(data)))
print('Part2:', part2(parse(data)))
