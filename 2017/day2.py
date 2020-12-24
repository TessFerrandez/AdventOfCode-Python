from common.helpers import extract_numbers
from typing import List


def parse_input(filename: str) -> List[List[int]]:
    return [extract_numbers(line.strip()) for line in open(filename).readlines()]


def part1(data: List[List[int]]) -> int:
    return sum([max(line) - min(line) for line in data])


def find_divisible(line: List[int]) -> int:
    for num1 in line:
        for num2 in line:
            if num1 != num2 and num1 % num2 == 0:
                return num1 // num2


def part2(data: List[List[int]]) -> int:
    return sum([find_divisible(line) for line in data])


def main():
    data = parse_input('input/day2.txt')
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == "__main__":
    main()
