import pytest
from typing import List, Tuple
from math import atan2, degrees
from collections import defaultdict, OrderedDict


@pytest.mark.parametrize('filename, expected',
                         [
                             ('input/day10_test1.txt', 8),
                             ('input/day10_test2.txt', 33),
                         ])
def test_part1(filename: str, expected: int):
    data = parse_input(filename)
    assert part1(data) == expected


def parse_input(filename: str) -> List[Tuple]:
    asteroids = []
    lines = [line.strip() for line in open(filename).readlines()]
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == '#':
                asteroids.append((x, y))
    return asteroids


def angle_between(p1, p2):
    x_diff = p2[0] - p1[0]
    y_diff = p2[1] - p1[1]
    return degrees(atan2(y_diff, x_diff))


def part1(asteroids: List[Tuple]) -> (int, Tuple[int, int]):
    max_seen = 0
    best_asteroid = (0, 0)

    for a1 in asteroids:
        seen = set(angle_between(a1, a2) for a2 in asteroids if a1 != a2)
        if len(seen) > max_seen:
            max_seen = len(seen)
            best_asteroid = a1
    return max_seen, best_asteroid


def part2(asteroids: List[Tuple], outpost: Tuple[int, int]) -> int:
    angles = defaultdict(lambda: [])
    ox, oy = outpost

    # get all asteroids - grouped by angle we see them at
    for asteroid in asteroids:
        if asteroid != outpost:
            angles[(angle_between(asteroid, outpost) - 90 + 360) % 360].append(asteroid)

    # sort the asteroids for each angle based on how far they are from the outpost
    for angle in angles:
        angles[angle] = list(sorted(angles[angle], key=lambda a: abs(a[0] - ox) + abs(a[1] - oy)))

    # get the possible angles we rotate between
    possible_angles = list(sorted(angles.keys()))
    num_possible = len(possible_angles)

    angle_index = 0
    for i in range(1, 201):
        # find the next angle with asteroids left
        while not angles[possible_angles[angle_index]]:
            angle_index = (angle_index + 1) % num_possible

        # vaporize the closest asteroid
        vaporized = angles[possible_angles[angle_index]].pop(0)
        if i == 200:
            return vaporized[0] * 100 + vaporized[1]

        # move to the next angle
        angle_index = (angle_index + 1) % num_possible
    return 0


def main():
    asteroids = parse_input('input/day10.txt')
    max_seen, best_asteroid = part1(asteroids)
    print(f'Part 1: {max_seen}')
    print(f'Part 2: {part2(asteroids, best_asteroid)}')


if __name__ == "__main__":
    main()
