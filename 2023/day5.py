from input_processing import read_data
import re


def parse_group(group):
    rows = [[int(d) for d in re.findall(r'-?\d+', line)] for line in group[1:]]
    map = sorted([(row[1], row[1] + row[2] - 1, row[0] - row[1]) for row in rows])
    if map[0][0] != 0:
        map.insert(0, (0, map[0][0] - 1, 0))

    full_map = [map[0]]
    for (fr, to, diff) in map[1:]:
        if fr != full_map[-1][1] + 1:
            full_map.append((full_map[-1][1] + 1, fr - 1, 0))
        full_map.append((fr, to, diff))
    return map


def parse(data):
    groups = [group.splitlines() for group in data.split('\n\n')]
    seeds = [int(seed) for seed in re.findall(r'-?\d+', groups[0][0])]
    maps = [parse_group(group) for group in groups[1:]]
    return seeds, maps


def translate(current, map):
    for (fr, to, diff) in map:
        if fr <= current <= to:
            return current + diff
    return current


def calculate_location(seed, maps):
    current = seed
    for map in maps:
        current = translate(current, map)
    return current


def part1(seeds, maps):
    return min(calculate_location(seed, maps) for seed in seeds)


def translate_range(seed_range, map):
    new_ranges = []

    range_start, range_end = seed_range

    for (fr, to, diff) in map:
        # range is after this map range
        # just continue
        if range_start > to:
            continue

        # range is fully included in this map range
        # translate it, add to ranges and break
        if range_end <= to:
            new_ranges.append((range_start + diff, range_end + diff))
            break

        # range is partially included in this map range
        # translate the part that is included, add to ranges,
        # and continue translating the rest
        if range_start <= to:
            new_ranges.append((range_start + diff, to + diff))
            range_start = to + 1

    if range_start > map[-1][1]:
        new_ranges.append((range_start, range_end))

    return new_ranges


def part2(seeds, maps):
    seed_ranges = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]
    for map in maps:
        new_seed_ranges = []
        for seed_range in seed_ranges:
            new_seed_ranges += translate_range(seed_range, map)
        seed_ranges = new_seed_ranges

    seed_ranges.sort()
    return seed_ranges[0][0]


def test():
    sample = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''
    seeds, maps = parse(sample)
    assert part1(seeds, maps) == 35
    assert part2(seeds, maps) == 46


test()
seeds, maps = parse(read_data(2023, 5))
print('Part1:', part1(seeds, maps))
print('Part2:', part2(seeds, maps))
