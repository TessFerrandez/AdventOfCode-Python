import pytest
from collections import defaultdict
from itertools import permutations


@pytest.mark.parametrize('data, expected',
                         [
                             ({'London': {'Dublin': 464, 'Belfast': 518},
                               'Dublin': {'London': 464, 'Belfast': 141},
                               'Belfast': {'London': 518, 'Dublin': 141}},
                              605),
                         ])
def test_part1(data: dict, expected: int):
    assert part1(data) == expected


@pytest.mark.parametrize('data, expected',
                         [
                             ({'London': {'Dublin': 464, 'Belfast': 518},
                               'Dublin': {'London': 464, 'Belfast': 141},
                               'Belfast': {'London': 518, 'Dublin': 141}},
                              982),
                         ])
def test_part2(data: dict, expected: int):
    assert part2(data) == expected


def parse_input(filename: str) -> dict:
    lines = [line.strip() for line in open(filename).readlines()]
    routes = defaultdict(dict)
    for line in lines:
        city1, _, city2, _, distance = line.split(' ')
        routes[city1][city2] = int(distance)
        routes[city2][city1] = int(distance)
    return routes


def part1(data: dict) -> int:
    cities = data.keys()
    num_cities = len(cities)
    routes = permutations(cities)

    best_distance = float('inf')
    for route in routes:
        distance = 0
        for i in range(num_cities - 1):
            distance += data[route[i]][route[i + 1]]
        if distance < best_distance:
            best_distance = distance
    return best_distance


def part2(data: dict) -> int:
    cities = data.keys()
    num_cities = len(cities)
    routes = permutations(cities)

    best_distance = 0
    for route in routes:
        distance = 0
        for i in range(num_cities - 1):
            distance += data[route[i]][route[i + 1]]
        if distance > best_distance:
            best_distance = distance
    return best_distance


def main():
    data = parse_input('input/day9.txt')
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == "__main__":
    main()
