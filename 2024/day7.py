from functools import reduce
from operator import mul
from input_processing import read_data, get_numbers_from_lines


def parse(data):
    return get_numbers_from_lines(data)


def part1(data):
    def is_good(target, terms):
        if len(terms) == 1:
            return target == terms[0]
        first, second = terms[:2]
        return is_good(target, [first + second, *terms[2:]]) or is_good(target, [first * second, *terms[2:]])

    good = []
    for line in data:
        target = line[0]
        terms = line[1:]
        if is_good(target, terms):
            good.append(target)

    return sum(good)


def part2(data):
    def is_good(target, terms):
        if len(terms) == 1:
            return target == terms[0]
        first, second = terms[:2]
        return is_good(target, [first + second, *terms[2:]]) or \
                is_good(target, [first * second, *terms[2:]]) or \
                is_good(target, [int(str(first) + str(second)), *terms[2:]])

    good = []
    for line in data:
        target = line[0]
        terms = line[1:]
        if is_good(target, terms):
            good.append(target)

    return sum(good)


def test():
    data = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20'''
    assert part1(parse(data)) == 3749
    assert part2(parse(data)) == 11387

test()
data = read_data(2024, 7)
print('Part1:', part1(parse(data)))
print('Part2:', part2(parse(data)))
