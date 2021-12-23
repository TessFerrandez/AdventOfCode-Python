"""
Finished part 1 but part 2 gave me so many headaches that I gave up.
This is based on a solution by alykzandr
"""

import re
from typing import List, Tuple, Union


def read_input() -> List[List[Union[str, int]]]:
    lines = open('2021/input/day22.txt').read().splitlines()
    steps = []
    for line in lines:
        parts = re.match(r'(\w+) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)$', line).groups()
        steps.append([parts[0]] + [int(i) for i in parts[1:]])
    return steps


def overlapping(zone1: List[int], zone2: List[int]) -> Union[Tuple[int, ...], None]:
    maxx, maxy, maxz = [max(zone1[i], zone2[i]) for i in (0, 2, 4)]
    minx, miny, minz = [min(zone1[i], zone2[i]) for i in (1, 3, 5)]

    if minx >= maxx and miny >= maxy and minz >= maxz:
        return maxx, minx, maxy, miny, maxz, minz
    else:
        return None


def count_lit(steps):
    lit = 0
    counted_zones = []
    for step in reversed(steps):
        mode, box = step[0], step[1:]
        minx, maxx, miny, maxy, minz, maxz = box
        if mode == 'on':
            dead_zones = []
            for overlap in [overlapping(zone, box) for zone in counted_zones]:
                if overlap:
                    dead_zones.append(('on', *overlap))
            lit += (maxx - minx + 1) * (maxy - miny + 1) * (maxz - minz + 1)
            lit -= count_lit(dead_zones)
        counted_zones.append(box)
    return lit


def filter_outliers(steps, max_val=50, min_val=-50):
    new_steps = []
    for step in steps:
        minx, maxx, miny, maxy, minz, maxz = step[1:]
        if minx <= max_val and miny <= max_val and minz <= max_val and maxx >= min_val and maxy >= min_val and maxz >= min_val:
            new_steps.append(step)
    return new_steps


steps = read_input()
steps = filter_outliers(steps)
print("Part 1:", count_lit(steps))

steps = read_input()
print("Part 2:", count_lit(steps))
