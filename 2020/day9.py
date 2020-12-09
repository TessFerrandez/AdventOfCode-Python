import pytest
from typing import List


@pytest.mark.parametrize('data, preamble, expected',
                         [
                             ([35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576], 5, 127),
                         ])
def test_part1(data: List[int], preamble: int, expected: int):
    assert part1(data, preamble) == expected


@pytest.mark.parametrize('data, target, expected',
                         [
                             ([35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576], 127, 62),
                         ])
def test_part2(data: List[int], target: int, expected: int):
    assert part2(data, target) == expected


def parse_input(filename: str):
    return [int(line.strip()) for line in open(filename).readlines()]


def match_sum(data: List[int], target: int) -> bool:
    for i in range(len(data) - 1):
        for j in range(i, len(data)):
            if data[i] + data[j] == target:
                return True
    return False


def part1(data: List[int], preamble: int) -> int:
    i = 0
    data_length = len(data)
    while i + preamble < data_length:
        if not match_sum(data[i: i + preamble], data[i + preamble]):
            return data[i + preamble]
        i += 1


def part2(data: List[int], target: int) -> (int, int):
    data_length = len(data)
    for i in range(data_length - 1):
        i_end = i + 1
        while i_end < data_length:
            sub_sum = sum(data[i: i_end])
            if sub_sum == target:
                return min(data[i: i_end]) + max(data[i: i_end])
            if sub_sum > target:
                break
            i_end += 1
    return 0


def main():
    data = parse_input('input/day9.txt')
    part1_result = part1(data, 25)
    print(f'Part 1: {part1_result}')
    print(f'Part 2: {part2(data, part1_result)}')


if __name__ == "__main__":
    main()
