from math import atan2, degrees, pi
from collections import defaultdict


ex1 = '''.#..#
.....
#####
....#
...##'''

ex2 = '''......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####'''

ex3 = '''.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##'''


def parse_input(raw_input):
    asteroids = []

    lines = raw_input.strip().splitlines()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                asteroids.append((x, y))

    return asteroids


def get_dir(a1, a2):
    x1, y1 = a1
    x2, y2 = a2

    delta_x = x2 - x1
    delta_y = y2 - y1
    rads = atan2(delta_x, delta_y)
    if rads < 0:
        rads = abs(rads)
    else:
        rads = 2 * pi - rads
    return (degrees(rads) - 180) % 360


def get_best_outpost(asteroids):
    best_asteroid = (-1, -1)
    best_seen = 0

    for a1 in asteroids:
        seen_dirs = set()
        for a2 in asteroids:
            if a1 != a2:
                seen_dirs.add(get_dir(a1, a2))

        if len(seen_dirs) > best_seen:
            best_asteroid = a1
            best_seen = len(seen_dirs)

    return best_asteroid, best_seen


def vaporize(asteroids, outpost):
    dirs = defaultdict(lambda: [])

    for asteroid in asteroids:
        if asteroid == outpost:
            continue
        direction = get_dir(outpost, asteroid)
        dirs[direction].append(asteroid)

    for dir in dirs:
        dirs[dir].sort(key=lambda x: abs(outpost[0] - x[0]) + abs(outpost[1] - x[1]), reverse=True)

    sorted_dirs = sorted(dirs.keys())
    order = []
    while sorted_dirs:
        for dir in sorted_dirs:
            order.append(dirs[dir].pop())
        sorted_dirs = [dir for dir in dirs if dirs[dir]]

    return order


def tests():
    asteroids = parse_input(ex3)
    _, seen = get_best_outpost(asteroids)
    assert seen == 210


tests()

raw_input = open('2019/input/day10.txt').read().strip()
asteroids = parse_input(raw_input)

outpost, seen = get_best_outpost(asteroids)
print("Part 1:", seen)

vaporized = vaporize(asteroids, outpost)
x, y = vaporized[199]
print("Part 2:", x * 100 + y)
