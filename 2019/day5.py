from typing import List
from Computer import Computer, OutputInterrupt


def parse_input(filename: str) -> List[int]:
    return [int(d) for d in open(filename).read().strip().split(',')]


def part1(code: List[int], input_value: int) -> int:
    computer = Computer(code)
    computer.inputs.append(input_value)
    while True:
        try:
            computer.run()
        except OutputInterrupt:
            output = computer.outputs[-1]
            if output != 0:
                return output


def part2(code: List[int], input_value: int) -> int:
    computer = Computer(code)
    computer.inputs.append(input_value)
    while True:
        try:
            computer.run()
        except OutputInterrupt:
            output = computer.outputs[-1]
            return output


def main():
    code = parse_input('input/day5.txt')
    print(f'Part 1: {part1(code, 1)}')
    code = parse_input('input/day5.txt')
    print(f'Part 2: {part2(code, 5)}')


if __name__ == "__main__":
    main()
