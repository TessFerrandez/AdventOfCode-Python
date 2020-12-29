from typing import List
from collections import defaultdict

CLEAN = 0
WEAKENED = 1
INFECTED = 2
FLAGGED = 3


def parse_input(filename: str) -> (dict, int):
    lines = [line.strip() for line in open(filename).readlines()]
    nodes = defaultdict(int)
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            if ch == '#':
                nodes[x * 1 + y * 1j] = INFECTED
    center = (len(lines) // 2)
    return nodes, center * 1 + center * 1j


def part1(nodes: dict, position: complex, iterations: int) -> int:
    # start looking up
    direction = -1j

    num_infections = 0
    for i in range(iterations):
        if nodes[position] == INFECTED:
            direction *= 1j    # rotate right
            nodes[position] = CLEAN
        else:
            direction *= -1j     # rotate left
            nodes[position] = INFECTED
            num_infections += 1
        position += direction

    return num_infections


def part2(nodes: dict, position: complex, iterations: int) -> int:
    # start looking up
    direction = -1j

    num_infections = 0
    for i in range(iterations):
        if nodes[position] == INFECTED:
            direction *= 1j    # rotate right
            nodes[position] = FLAGGED
        elif nodes[position] == CLEAN:
            direction *= -1j     # rotate left
            nodes[position] = WEAKENED
        elif nodes[position] == WEAKENED:
            nodes[position] = INFECTED
            num_infections += 1
        elif nodes[position] == FLAGGED:
            direction *= -1
            nodes[position] = CLEAN
        position += direction

    return num_infections


def main():
    nodes, center = parse_input('input/day22.txt')
    print(f'Part 1: {part1(nodes, center, 10000)}')
    nodes, center = parse_input('input/day22.txt')
    print(f'Part 2: {part2(nodes, center, 10000000)}')


if __name__ == "__main__":
    main()
