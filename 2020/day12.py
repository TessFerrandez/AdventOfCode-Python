import pytest
from typing import List, Tuple


@pytest.mark.parametrize('data, expected',
                         [
                             ('', 0),
                         ])
def test_part1(data: str, expected: int):
    assert part1(data) == expected


@pytest.mark.parametrize('data, expected',
                         [
                             ('', 0),
                         ])
def test_part2(data: str, expected: int):
    assert part2(data) == expected


def parse_input(filename: str) -> List[Tuple[str, int]]:
    lines = [line.strip() for line in open(filename).readlines()]
    return [(line[0], int(line[1:])) for line in lines]


def part1(instructions: List[Tuple[str, int]]) -> int:
    dirs = {'E': 1, 'S': -1j, 'W': -1, 'N': 1j}
    position = 0
    direction = dirs['E']
    for instruction in instructions:
        move_dir, steps = instruction
        if move_dir == 'R':
            for i in range(steps // 90):
                direction *= -1j
        elif move_dir == 'L':
            for i in range(steps // 90):
                direction *= 1j
        elif move_dir == 'F':
            position += steps * direction
        else:
            position += steps * dirs[move_dir]
    return int(abs(position.real) + abs(position.imag))


def part2(instructions: List[Tuple[str, int]]) -> int:
    dirs = {'E': 1, 'S': -1j, 'W': -1, 'N': 1j}
    ship = 0
    waypoint = 10 + 1j

    for instruction in instructions:
        inst, steps = instruction
        if inst == 'F':
            ship += steps * waypoint
        elif inst == 'R':
            for i in range(steps // 90):
                waypoint *= -1j
        elif inst == 'L':
            for i in range(steps // 90):
                waypoint *= 1j
        else:
            waypoint += steps * dirs[inst]
    return int(abs(ship.real) + abs(ship.imag))


def main():
    instructions = parse_input('input/day12.txt')
    print(f'Part 1: {part1(instructions)}')
    print(f'Part 2: {part2(instructions)}')


if __name__ == "__main__":
    main()
