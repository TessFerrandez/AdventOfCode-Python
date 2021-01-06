from collections import defaultdict
from typing import List


def parse_input(filename: str) -> (dict, List[str]):
    planets = set()
    orbits = defaultdict(str)
    lines = [line.strip().split(')') for line in open(filename).readlines()]
    for inner, outer in lines:
        orbits[outer] = inner
        planets.add(inner)
        planets.add(outer)
    return orbits, list(planets)


def part1(orbits: dict, planets: List[str]) -> int:
    cache = {}

    for planet in planets:
        num_orbits = 0
        inner = orbits[planet]
        while inner != '' and inner not in cache:
            num_orbits += 1
            inner = orbits[inner]
        if inner == '':
            cache[planet] = num_orbits
        else:
            cache[planet] = num_orbits + cache[inner] + 1

    return sum(cache.values())


def part2(orbits: dict) -> int:
    # get the path from you to COM
    you_path = []
    inner = orbits['YOU']
    while inner != 'COM':
        you_path.append(inner)
        inner = orbits[inner]

    # get the path from santa to COM
    santa_path = []
    inner = orbits['SAN']
    while inner != 'COM':
        santa_path.append(inner)
        inner = orbits[inner]

    # remove the bits you got in common
    while you_path[-1] == santa_path[-1]:
        you_path.pop(-1)
        santa_path.pop(-1)

    # find the number of hops
    return len(you_path) + len(santa_path)


def main():
    orbits, planets = parse_input('input/day6.txt')
    print(f'Part 1: {part1(orbits, planets)}')
    print(f'Part 2: {part2(orbits)}')


if __name__ == "__main__":
    main()
