from typing import List
from Computer import Computer, OutputInterrupt


def parse_input(filename: str) -> List[int]:
    return [int(d) for d in open(filename).read().strip().split(',')]


def part1(code: List[int]) -> int:
    computer = Computer(code)
    computer.inputs.append(1)
    while not computer.done:
        try:
            computer.run()
        except OutputInterrupt:
            return computer.outputs[-1]
    return 0


def part2(code: List[int]) -> int:
    computer = Computer(code)
    computer.inputs.append(2)
    while not computer.done:
        try:
            computer.run()
        except OutputInterrupt:
            return computer.outputs[-1]
    return 0


def main():
    code = parse_input('input/day9.txt')
    print(f'Part 1: {part1(code)}')
    code = parse_input('input/day9.txt')
    print(f'Part 2: {part2(code)}')


if __name__ == "__main__":
    main()
