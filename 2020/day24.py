from collections import Counter
from typing import List
import pytest


@pytest.mark.parametrize('data, expected',
                         [
                             ('esenee', 'eee'),
                             ('esew', 'se'),
                             ('nwwswee', ''),
                         ])
def test_reduce_path(data: str, expected: str):
    assert reduce_path(data) == expected


def create_path(path_str: str) -> List[str]:
    path = []
    i = 0
    while i < len(path_str):
        if path_str[i] in ['e', 'w']:
            path.append(path_str[i])
        else:
            path.append(path_str[i] + path_str[i + 1])
            i += 1
        i += 1
    return path


def reduce(counts: dict, dir1: str, dir2: str) -> int:
    reduced = 0
    if dir1 in counts and dir2 in counts:
        reduced = min(counts[dir1], counts[dir2])
        counts[dir1] -= reduced
        counts[dir2] -= reduced
        if counts[dir1] == 0:
            del counts[dir1]
        if counts[dir2] == 0:
            del counts[dir2]
    return reduced


def update(counts: dict, direction: str, reduced: int):
    if reduced == 0:
        return
    if direction in counts:
        counts[direction] += reduced
    else:
        counts[direction] = reduced


def reduce_path(path_str) -> str:
    path = create_path(path_str)
    counts = Counter(path)
    reduce(counts, 'se', 'nw')
    reduce(counts, 'ne', 'sw')
    reduced = reduce(counts, 'ne', 'se')
    update(counts, 'e', reduced)
    reduced = reduce(counts, 'nw', 'sw')
    update(counts, 'w', reduced)
    reduce(counts, 'e', 'w')
    reduced = reduce(counts, 'nw', 'e')
    update(counts, 'ne', reduced)
    reduced = reduce(counts, 'ne', 'w')
    update(counts, 'nw', reduced)
    reduced = reduce(counts, 'sw', 'e')
    update(counts, 'se', reduced)
    reduced = reduce(counts, 'se', 'w')
    update(counts, 'sw', reduced)

    reduced_path = []
    for direction in counts:
        for _ in range(counts[direction]):
            reduced_path.append(direction)
    reduced_path.sort()
    return ''.join(reduced_path)


def parse_input(filename: str) -> List[str]:
    return [line.strip() for line in open(filename).readlines()]


def part1(black: List[str]) -> int:
    return len(black)


def get_neighbors(black: List[str]) -> dict:
    neighbors = []
    directions = ['e', 'w', 'ne', 'nw', 'se', 'sw']
    for black_tile in black:
        for direction in directions:
            neighbors.append(reduce_path(black_tile + direction))

    return Counter(neighbors)


def part2(black: List[str]) -> int:
    for day in range(100):
        neighbors = get_neighbors(black)
        two_blacks = [neighbor for neighbor in neighbors if neighbors[neighbor] == 2]
        for tile in two_blacks:
            if tile not in black:
                black.append(tile)
        more_than_two_blacks = [neighbor for neighbor in neighbors if neighbors[neighbor] > 2]
        for tile in more_than_two_blacks:
            if tile in black:
                black.remove(tile)
        zero_blacks = [tile for tile in black if tile not in neighbors]
        for tile in zero_blacks:
            black.remove(tile)
        # print(f'Day {day}: {len(black)}')
    return len(black)


def get_black(paths: List[str]) -> List[str]:
    reduced = [reduce_path(path) for path in paths]
    counts = Counter(reduced)
    black = [tile for tile in counts if counts[tile] % 2 == 1]
    return black


def main():
    paths = parse_input('input/day24.txt')
    black = get_black(paths)
    print(f'Part 1: {part1(black)}')
    print(f'Part 2: {part2(black)}')


if __name__ == "__main__":
    main()
