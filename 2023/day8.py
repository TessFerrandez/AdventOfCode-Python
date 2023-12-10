from input_processing import read_data
from math import gcd


def parse(data):
    instructions, map_data = data.split('\n\n')
    map_lines = map_data.split('\n')
    desert_map = {}

    for i, line in enumerate(map_lines):
        source, target = line.split(' = ')
        left, right = target.split(', ')
        left = left[1:]
        right = right[:-1]
        desert_map[source] = (left, right)

    return instructions, desert_map


def get_steps(instructions, map, start, end):
    current = start

    steps = 0
    while current != end:
        if instructions[steps % len(instructions)] == 'L':
            current = map[current][0]
        else:
            current = map[current][1]
        steps += 1
        if steps > 100000:
            return 100000

    return steps


def part1(instructions, map):
    return get_steps(instructions, map, 'AAA', 'ZZZ')


def part2(instructions, map):
    def all_are_at_final_destinations(locations):
        for location in locations:
            if location[-1] != 'Z':
                return False
        return True

    starts = [location for location in map if location[-1] == 'A']
    goals = [location for location in map if location[-1] == 'Z']

    best_steps = []
    for start in starts:
        min_steps = 100000
        for goal in goals:
            steps = get_steps(instructions, map, start, goal)
            if steps < min_steps:
                min_steps = steps
        best_steps.append(min_steps)

    lcm = 1
    for step in best_steps:
        lcm = lcm * step // gcd(lcm, step)

    return lcm


def test():
    sample1 = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''
    sample2 = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)'''
    instructions, map = parse(sample1)
    assert part1(instructions, map) == 2
    instructions, map = parse(sample2)
    assert part1(instructions, map) == 6
    sample3 = '''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)'''
    instructions, map = parse(sample3)
    assert part2(instructions, map) == 6


test()
data = read_data(2023, 8)
instructions, map = parse(data)
print('Part1:', part1(instructions, map))
print('Part2:', part2(instructions, map))
