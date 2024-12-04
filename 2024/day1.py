from input_processing import read_data, get_numbers_from_lines
from collections import Counter


def parse(data):
    rows = get_numbers_from_lines(data)
    location_ids_1 = [id[0] for id in rows]
    location_ids_2 = [id[1] for id in rows]
    return [location_ids_1, location_ids_2]


def part1(data):
    location_ids_1, location_ids_2 = data
    location_ids_1.sort()
    location_ids_2.sort()

    total = 0
    for id1, id2 in zip(location_ids_1, location_ids_2):
        total += abs(id1 - id2)
    return total


def part2(data):
    location_ids_1, location_ids_2 = data
    counts = Counter(location_ids_2)

    total = 0
    for id in location_ids_1:
        total += counts[id] * id

    return total


def test():
    data = '''3   4
4   3
2   5
1   3
3   9
3   3'''
    assert part1(parse(data)) == 11
    assert part2(parse(data)) == 31
    print('Test passed')


test()
data = read_data(2024, 1)
print('Part1:', part1(parse(data)))
print('Part2:', part2(parse(data)))
