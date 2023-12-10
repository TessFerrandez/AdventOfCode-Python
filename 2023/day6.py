import re
from input_processing import read_data
from math import sqrt, prod, ceil


def parse(data):
    lines = data.splitlines()
    times = [int(num) for num in re.findall(r'\d+', lines[0])]
    distances = [int(num) for num in re.findall(r'\d+', lines[1])]
    return list(zip(times, distances))


def parse2(data):
    lines = data.splitlines()
    time = int(re.findall(r'\d+', lines[0].replace(' ', ''))[0])
    distance = int(re.findall(r'\d+', lines[1].replace(' ', ''))[0])

    return time, distance


def count_winning(time, distance):
    t0 = (time - sqrt(time ** 2 - 4 * distance)) // 2
    return int(time - (t0 + t0 + 1))


def part1(data):
    '''
    PART 1 - algorithm

    Ex: (7, 9)

    time    result
    0       0 * 7
    1       1 * 6 (7 - 1) = 6
    2       2 * 5 (7 - 2) = 10*
    3       3 * 4 (7 - 3) = 12*
    4       4 * 3 (7 - 4) = 12*
    5       5 * 2 (7 - 5) = 10*
    6       6 * 1 (7 - 6) = 6
    7       7 * 0 (7 - 7) = 0

    so if time(t) * (total(tot) - time(t)) >= distance(d), we win

    t * tot - t^2 >= d      => quadratic equation

    so we need to find the smallest t such that t^2 - tot * t + d <= 0
    which is done by solving the quadratic equation - ex. a*t^2 + b*t + c = 0 => t = (-b +- sqrt(b^2 - 4ac)) / 2a

    in the above case this would be ~1.7 so 1 => t0

    the number of winning options are total - (t0 + t0 + 1) = 7 - (2 + 1) = 4
    '''
    return prod([count_winning(time, distance) for time, distance in data])


def part2(time, distance):
    return count_winning(time, distance)


def test():
    sample = '''Time:      7  15   30
Distance:  9  40  200'''
    assert part1(parse(sample)) == 288
    time, distance = parse2(sample)
    assert part2(time, distance) == 71503


test()
data = read_data(2023, 6)
print('Part1:', part1(parse(data)))
time, distance = parse2(data)
print('Part2:', part2(time, distance))
