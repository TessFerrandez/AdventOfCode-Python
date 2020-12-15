import re
from typing import List


def parse_input(filename: str):
    values = [[int(number) for number in re.findall(r'[-\d]+', line)] for line in open(filename).readlines()]
    return values


def part1(triangles: List[List[int]]) -> int:
    sorted_triangles = [list(sorted(triangle)) for triangle in triangles]
    return sum(1 for triangle in sorted_triangles if triangle[0] + triangle[1] > triangle[2])


def part2(values: List[List[int]]) -> int:
    possible = 0

    for col in range(3):
        for row in range(0, len(values), 3):
            sides = [values[row][col], values[row + 1][col], values[row + 2][col]]
            sides.sort()
            s1, s2, s3 = sides
            if s1 + s2 > s3:
                possible += 1
    return possible


def main():
    values = parse_input('input/day3.txt')
    print(f'Part 1: {part1(values)}')
    print(f'Part 2: {part2(values)}')


if __name__ == "__main__":
    main()
