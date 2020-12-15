import pytest
from typing import List


@pytest.mark.parametrize('data, expected',
                         [
                             (['ULL', 'RRDDD', 'LURDL', 'UUUUD'], 1985),
                         ])
def test_part1(data: List[str], expected: int):
    assert part1(data) == expected


@pytest.mark.parametrize('data, expected',
                         [
                             (['ULL', 'RRDDD', 'LURDL', 'UUUUD'], '5DB3'),
                         ])
def test_part2(data: List[str], expected: int):
    assert part2(data) == expected


def parse_input(filename: str) -> List[str]:
    return [line.strip() for line in open(filename).readlines()]


def part1(instructions: List[str]) -> int:
    dirs = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}
    code_pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    button = (1, 1)
    code = []

    for instruction in instructions:
        for d in instruction:
            dx, dy = dirs[d]
            button = (max(min(button[0] + dx, 2), 0), max(min(button[1] + dy, 2), 0))
        x, y = button
        code.append(code_pad[y][x])
    return int(''.join(str(c) for c in code))


def part2(instructions: List[str]) -> str:
    dirs = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}
    code_pad = [['X', 'X', 'X', 'X', 'X', 'X', 'X'],
                ['X', 'X', 'X', '1', 'X', 'X', 'X'],
                ['X', 'X', '2', '3', '4', 'X', 'X'],
                ['X', '5', '6', '7', '8', '9', 'X'],
                ['X', 'X', 'A', 'B', 'C', 'X', 'X'],
                ['X', 'X', 'X', 'D', 'X', 'X', 'X'],
                ['X', 'X', 'X', 'X', 'X', 'X', 'X']]

    button = (1, 3)
    code = []

    for instruction in instructions:
        for d in instruction:
            dx, dy = dirs[d]
            x, y = button
            x += dx
            y += dy
            if code_pad[y][x] != 'X':
                button = (x, y)

        x, y = button
        code.append(code_pad[y][x])

    return ''.join(code)


def main():
    data = parse_input('input/day2.txt')
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == "__main__":
    main()
