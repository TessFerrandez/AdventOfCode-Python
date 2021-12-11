### PART 2 IS INCOMPLETE ###

from typing import List, Tuple
from common.helpers import extract_numbers


def parse_input(filename: str) -> List:
    lines = [extract_numbers(line) for line in open(filename).readlines()]
    bots = [[(x, y, z), r] for x, y, z, r in lines]
    return bots


def get_distance(bot1: Tuple[int, int, int], bot2: Tuple[int, int, int]) -> int:
    return abs(bot1[0] - bot2[0]) + abs(bot1[1] - bot2[1]) + abs(bot1[2] - bot2[2])


def part1(nanobots: List) -> int:
    strongest = (0, 0, 0)
    max_radius = 0

    for nanobot in nanobots:
        if nanobot[1] > max_radius:
            max_radius = nanobot[1]
            strongest = nanobot[0]

    in_range = 0
    for nanobot in nanobots:
        if get_distance(strongest, nanobot[0]) <= max_radius:
            in_range += 1

    return in_range


def part2(nanobots: List) -> int:
    # INCOMPLETE
    return 0


def main():
    nanobots = parse_input('input/day23.txt')
    print(f'Part 1: {part1(nanobots)}')
    print(f'Part 2: {part2(nanobots)}')


if __name__ == "__main__":
    main()
