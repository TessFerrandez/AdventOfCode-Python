from typing import List
from copy import copy
from Computer import Computer


def parse_input(filename: str) -> List[int]:
    return [int(d) for d in open(filename).read().strip().split(',')]


def part1(code: List[int]) -> int:
    code[1] = 12
    code[2] = 2

    computer = Computer(code)
    computer.run()

    return computer.code[0]


def part2(code: List[int]) -> int:
    original = copy(code)

    for noun in range(100):
        for verb in range(100):
            code = copy(original)
            code[1] = noun
            code[2] = verb
            computer = Computer(code)
            computer.run()
            result = computer.code[0]
            if result == 19690720:
                return 100 * noun + verb
    return 0


def main():
    code = parse_input('input/day2.txt')
    print(f'Part 1: {part1(code)}')
    code = parse_input('input/day2.txt')
    print(f'Part 2: {part2(code)}')


if __name__ == "__main__":
    main()
