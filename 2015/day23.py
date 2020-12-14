from typing import List


class Computer:
    def __init__(self, instructions: List, regs: dict):
        self.ptr = 0
        self.regs = regs
        self.instructions = instructions
        self.end = len(self.instructions)

    def run(self):
        while self.ptr < self.end:
            # compute instructions
            instruction = self.instructions[self.ptr]
            op, reg, *_ = instruction

            if op == 'inc':
                self.regs[reg] += 1
                self.ptr += 1
            if op == 'hlf':
                self.regs[reg] /= 2
                self.ptr += 1
            elif op == 'tpl':
                self.regs[reg] *= 3
                self.ptr += 1
            elif op == 'jio':
                offset = int(instruction[2])
                if self.regs[reg] == 1:
                    self.ptr += offset
                else:
                    self.ptr += 1
            elif op == 'jie':
                offset = int(instruction[2])
                if self.regs[reg] % 2 == 0:
                    self.ptr += offset
                else:
                    self.ptr += 1
            elif op == 'jmp':
                offset = int(instruction[1])
                self.ptr += offset


def parse_input(filename: str):
    lines = [line.strip() for line in open(filename).readlines()]
    instructions = []
    for line in lines:
        op = line[0: 3]
        instructions.append([op] + line[4:].split(', '))
    return instructions


def part1(instructions: List[List], regs: dict) -> int:
    computer = Computer(instructions, regs)
    computer.run()
    return computer.regs['b']


def part2(instructions: List[List], regs: dict) -> int:
    computer = Computer(instructions, regs)
    computer.run()
    return computer.regs['b']


def main():
    instructions = parse_input('input/day23.txt')
    regs = {'a': 0, 'b': 0}
    print(f'Part 1: {part1(instructions, regs)}')
    regs = {'a': 1, 'b': 0}
    print(f'Part 2: {part2(instructions, regs)}')


if __name__ == "__main__":
    main()
