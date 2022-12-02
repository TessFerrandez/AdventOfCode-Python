from collections import defaultdict
from typing import List, Tuple


def parse_input(data):
    lines = []
    for line in data.strip().splitlines():
        p1, p2 = line.split(' -> ')
        x1, y1 = (int(d) for d in p1.split(','))
        x2, y2 = (int(d) for d in p2.split(','))
        lines.append((x1, y1, x2, y2))
    return lines


def part1(lines: List[Tuple[int]]) -> int:
    points = defaultdict(int)
    for x1, y1, x2, y2 in lines:
        if x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            for y in range(y1, y2 + 1):
                points[(x1, y)] += 1
        elif y1 == y2:
            x1, x2 = min(x1, x2), max(x1, x2)
            for x in range(x1, x2 + 1):
                points[(x, y1)] += 1

    num_over_two = 0
    for point, count in points.items():
        if count >= 2:
            num_over_two += 1

    return num_over_two


def part2(lines: List[Tuple[int]]) -> int:
    points = defaultdict(int)
    for x1, y1, x2, y2 in lines:
        if x1 == x2:
            y1, y2 = min(y1, y2), max(y1, y2)
            for y in range(y1, y2 + 1):
                points[(x1, y)] += 1
        elif y1 == y2:
            x1, x2 = min(x1, x2), max(x1, x2)
            for x in range(x1, x2 + 1):
                points[(x, y1)] += 1
        elif abs(x1 - x2) == abs(y1 - y2):
            if x1 > x2:
                x1, x2, y1, y2 = x2, x1, y2, y1
            stepy = 1 if y2 > y1 else -1
            x, y = x1, y1
            while x <= x2:
                points[(x, y)] += 1
                x += 1
                y += stepy

    num_over_two = 0
    for point, count in points.items():
        if count >= 2:
            num_over_two += 1

    return num_over_two


sample_input = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''

lines = parse_input(sample_input)
assert part1(lines) == 5
assert part2(lines) == 12

lines = parse_input(open('./2021/input/day5.txt').read())
print("Part1:", part1(lines))
print("Part2:", part2(lines))
