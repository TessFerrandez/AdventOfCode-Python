import pytest
from typing import List


@pytest.mark.parametrize('instructions, expected',
                         [
                             (['R2', 'L3'], 5),
                             (['R2', 'R2', 'R2'], 2),
                             (['R5', 'L5', 'R5', 'R3'], 12),
                         ])
def test_part1(instructions: List[str], expected: int):
    assert part1(instructions) == expected


@pytest.mark.parametrize('instructions, expected',
                         [
                             (['R8', 'R4', 'R4', 'R8'], 4),
                         ])
def test_part2(instructions: List[str], expected: int):
    assert part2(instructions) == expected


def parse_input(filename: str) -> List[str]:
    return open(filename).read().strip().split(', ')


def part2(instructions: List[str]) -> int:
    position = 0
    visited = [position]
    direction = 1j

    for instruction in instructions:
        turn = instruction[0]
        steps = int(instruction[1:])
        if turn == 'R':
            direction *= -1j
        else:
            direction *= 1j
        for _ in range(steps):
            position += direction
            if position in visited:
                return int(abs(position.real) + abs(position.imag))
            visited.append(position)


def part1(instructions: List[str]) -> int:
    position = 0
    direction = 1j
    for instruction in instructions:
        turn = instruction[0]
        steps = int(instruction[1:])
        if turn == 'R':
            direction *= -1j
        else:
            direction *= 1j
        position += direction * steps
    return int(abs(position.real) + abs(position.imag))


def main():
    directions = parse_input('input/day1.txt')
    print(f'Part 1: {part1(directions)}')
    print(f'Part 2: {part2(directions)}')


if __name__ == "__main__":
    main()
