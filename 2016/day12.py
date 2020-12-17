from typing import List
from collections import defaultdict
import progressbar


class Computer:
    def __init__(self, instructions: List[List[str]], registers: dict):
        self.instructions = instructions
        self.registers = registers
        self.ptr = 0

    def run(self):
        end = len(self.instructions)

        with progressbar.ProgressBar() as p:
            while self.ptr != end:
                p.update(self.ptr)

                instruction = self.instructions[self.ptr]
                op = instruction[0]
                if op == 'cpy':
                    _, value, reg = instruction
                    self.registers[reg] = self.registers[value] if value in ['a', 'b', 'c', 'd'] else int(value)
                    self.ptr += 1
                elif op == 'inc':
                    self.registers[instruction[1]] += 1
                    self.ptr += 1
                elif op == 'dec':
                    self.registers[instruction[1]] -= 1
                    self.ptr += 1
                elif op == 'jnz':
                    _, reg, offset = instruction
                    value = self.registers[reg] if reg in ['a', 'b', 'c', 'd'] else int(reg)
                    self.ptr += int(offset) if value != 0 else 1
                else:
                    print('operation not recognized:', op)
                    break


def parse_input(filename: str):
    return [line.strip().split() for line in open(filename).readlines()]


def part1(instructions: List[List[str]]) -> int:
    registers = defaultdict(int)
    computer = Computer(instructions, registers)
    computer.run()
    return computer.registers['a']


def part2(instructions: List[List[str]]) -> int:
    registers = defaultdict(int)
    registers['c'] = 1
    computer = Computer(instructions, registers)
    computer.run()
    return computer.registers['a']


def main():
    instructions = parse_input('input/day12.txt')
    print(f'Part 1: {part1(instructions)}')
    print(f'Part 2: {part2(instructions)}')


if __name__ == "__main__":
    main()
