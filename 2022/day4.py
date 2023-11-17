from input_processing import read_data


def parse(data):
    rows = data.splitlines()
    pairs = []
    for row in rows:
        pair = row.split(",")
        pairs.append([[int(d) for d in pair[i].split("-")] for i in [0, 1]])
    return pairs


def part1(data):
    count = 0
    for p1, p2 in data:
        if p1[0] <= p2[0] and p1[1] >= p2[1]:
            count += 1
        elif p2[0] <= p1[0] and p2[1] >= p1[1]:
            count += 1
    return count


def part2(data):
    count = 0
    for pair in data:
        pair.sort()
        p1, p2 = pair
        if p1[1] >= p2[0]:
            count += 1
    return count


def test():
    sample = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
    sample_pairs = parse(sample)
    assert part1(sample_pairs) == 2
    assert part2(sample_pairs) == 4


test()
data = parse(read_data(2022, 4))
print('Part1:', part1(data))
print('Part2:', part2(data))
