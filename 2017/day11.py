from typing import List
import pytest


DIRECTIONS = {'n': (0, 1),
              'ne': (0.5, 0.5),
              'se': (0.5, -0.5),
              's': (0, -1),
              'sw': (-0.5, -0.5),
              'nw': (-0.5, 0.5)}


@pytest.mark.parametrize('data, expected',
                         [
                             (['ne', 'ne', 'ne'], 3),
                             (['ne', 'ne', 'sw', 'sw'], 0),
                             (['ne', 'ne', 's', 's'], 2),
                             (['se', 'sw', 'se', 'sw', 'sw'], 3),
                         ])
def test_part1(data: List[str], expected: int):
    assert part1(data) == expected


def parse_input(filename: str) -> List[str]:
    return [d for d in open(filename).read().strip().split(',')]


def part1(directions: List[str]) -> int:
    x, y = 0, 0
    for direction in directions:
        dx, dy = DIRECTIONS[direction]
        x += dx
        y += dy
    return int(abs(x) + abs(y))


def part2(directions: List[str]) -> int:
    max_distance = 0

    x, y = 0, 0
    for direction in directions:
        dx, dy = DIRECTIONS[direction]
        x += dx
        y += dy
        distance = abs(x) + abs(y)
        if distance > max_distance:
            max_distance = distance
    return int(max_distance)


def main():
    data = parse_input('input/day11.txt')
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == "__main__":
    main()
