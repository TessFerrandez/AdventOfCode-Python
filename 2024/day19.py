from collections import defaultdict
from functools import cache
from input_processing import read_data


def parse(data):
    towels, patterns = data.split('\n\n')
    towels = towels.split(', ')
    patterns = patterns.split('\n')
    return towels, patterns


def part1(towels_list, patterns):
    towels = defaultdict(list)
    for towel in towels_list:
        towels[towel[0]].append(towel)

    @cache
    def makes_pattern(pattern):
        if not pattern:
            return True
        for towel in towels[pattern[0]]:
            if pattern.startswith(towel):
                if makes_pattern(pattern[len(towel):]):
                    return True
        return False

    return sum(makes_pattern(pattern) for pattern in patterns)


def part2(towels_list, patterns):
    towels = defaultdict(list)
    for towel in towels_list:
        towels[towel[0]].append(towel)

    @cache
    def makes_pattern(pattern):
        if not pattern:
            return 1
        total = 0
        for towel in towels[pattern[0]]:
            if pattern.startswith(towel):
                total += makes_pattern(pattern[len(towel):])
        return total

    return sum(makes_pattern(pattern) for pattern in patterns)


def test():
    data = '''r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb'''
    towels, patterns = parse(data)
    assert part1(towels, patterns) == 6
    assert part2(towels, patterns) == 16

test()
data = read_data(2024, 19)
towels, patterns = parse(data)
print('Part1:', part1(towels, patterns))
print('Part2:', part2(towels, patterns))
