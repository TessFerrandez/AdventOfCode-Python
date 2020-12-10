import pytest
from typing import List
from collections import defaultdict


@pytest.mark.parametrize('data, expected',
                         [
                             ([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4], 35),
                             ([28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3], 220),
                         ])
def test_part1(data: List[int], expected: int):
    assert part1(data) == expected


@pytest.mark.parametrize('data, expected',
                         [
                             ([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4], 8),
                             ([28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3], 19208),
                         ])
def test_part2(data: List[int], expected: int):
    assert part2(data) == expected


def parse_input(filename: str):
    adapters = [int(line) for line in open(filename).readlines()]
    return adapters


def part1(adapters: List[int]) -> int:
    adapters.sort()
    current = 0
    num_1, num_3 = 0, 1
    for adapter in adapters:
        if adapter - current == 1:
            num_1 += 1
        elif adapter - current == 3:
            num_3 += 1
        current = adapter
    return num_1 * num_3


def get_options(adapters: List[int]) -> dict:
    options = defaultdict(lambda: [])

    for i in range(1, 4):
        if i in adapters:
            options[0].append(i)

    for pos, adapter in enumerate(adapters):
        for i in range(1, 4):
            if adapter + i in adapters[pos:]:
                options[adapter].append(adapter + i)

    options[adapters[-1]].append(adapters[-1] + 3)
    return options


def part2(adapters: List[int]) -> int:
    adapters.sort()
    options = get_options(adapters)
    end = adapters[-1] + 3
    routes = {end: 1}
    reversed_adapters = list(reversed(adapters))
    reversed_adapters.append(0)
    for adapter in reversed_adapters:
        adapter_options = options[adapter]
        num_routes = 0
        for option in adapter_options:
            num_routes += routes[option]
        routes[adapter] = num_routes
    return routes[0]


def main():
    data = parse_input('input/day10.txt')
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == "__main__":
    main()
