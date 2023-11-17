from input_processing import read_data


def part1(data):
    start = 0
    last_seen = {}

    for i, ch in enumerate(data):
        if i - start == 4:
            return i
        if ch in last_seen:
            start = max(start, last_seen[ch] + 1)
        last_seen[ch] = i


def part2(data):
    start = 0
    last_seen = {}

    for i, ch in enumerate(data):
        if i - start == 14:
            return i
        if ch in last_seen:
            start = max(start, last_seen[ch] + 1)
        last_seen[ch] = i


def test():
    sample = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    assert part1(sample) == 7
    assert part2(sample) == 19


test()
data = read_data(2022, 6)
print('Part1:', part1(data))
print('Part2:', part2(data))
