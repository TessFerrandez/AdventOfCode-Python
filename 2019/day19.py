import numpy as np
from typing import List
from Computer import Computer, InputInterrupt, OutputInterrupt
from copy import copy


def parse_input(filename: str) -> List[int]:
    return [int(d) for d in open(filename).read().strip().split(',')]


def get_status(code: List[int], x: int, y: int) -> int:
    computer = Computer(copy(code))
    try:
        computer.inputs.append(x)
        computer.inputs.append(y)
        computer.run()
    except OutputInterrupt:
        status = computer.outputs[-1]
        return status
    return 0


def part1(code: List[int]) -> int:
    return sum(get_status(code, x, y) for x in range(50) for y in range(50))


def part2(code: List[int]) -> int:
    x = y = 0
    while not get_status(code, x + 99, y):
        y += 1
        while not get_status(code, x, y + 99):
            x += 1
    return x * 10000 + y


def main():
    code = parse_input('input/day19.txt')
    print(f'Part 1: {part1(code)}')
    code = parse_input('input/day19.txt')
    print(f'Part 2: {part2(code)}')


if __name__ == "__main__":
    main()
