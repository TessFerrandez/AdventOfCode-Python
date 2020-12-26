from typing import List
from collections import defaultdict


def parse_input(filename: str) -> List[List[str]]:
    return [[part for part in line.strip().split(' ')] for line in open(filename).readlines()]


def run(instructions: List[List[str]]) -> (dict, int):
    max_reg = 0
    ops1 = {'inc': 1, 'dec': -1}
    ops2 = {'<=': lambda x, y: x <= y,
            '!=': lambda x, y: x != y,
            '>': lambda x, y: x > y,
            '<': lambda x, y: x < y,
            '>=': lambda x, y: x >= y,
            '==': lambda x, y: x == y}
    registers = defaultdict(int)
    for instruction in instructions:
        reg, op1, num, _, left, op2, right = instruction
        do_op = ops2[op2](registers[left], int(right))
        if do_op:
            registers[reg] += ops1[op1] * int(num)
            if registers[reg] > max_reg:
                max_reg = registers[reg]
    return registers, max_reg


def part1(instructions: List[List[str]]) -> int:
    registers, _ = run(instructions)
    return max(registers.values())


def part2(instructions: List[List[str]]) -> int:
    registers, max_reg = run(instructions)
    return max_reg


def main():
    instructions = parse_input('input/day8.txt')
    print(f'Part 1: {part1(instructions)}')
    print(f'Part 2: {part2(instructions)}')


if __name__ == "__main__":
    main()
