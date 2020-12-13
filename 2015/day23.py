from typing import List


class Computer:
    def __init__(self, instructions):
        self.ptr = 0
        self.regs = [0, 0]
        self.instructions = instructions
        self.end = len(self.instructions)

    def run(self):
        while self.ptr != self.end:
            # compute instructions
            op, reg, offset = self.instructions[self.ptr]
            if op == 'hlf':
                self.regs[reg] /= 2
                self.ptr += 1
            elif op == 'tpl':
                self.regs[reg] *= 3
                self.ptr += 1
            elif op == 'inc':
                self.regs[reg] += 1
                self.ptr += 1
            elif op == 'jmp':
                self.ptr += offset
            elif op == 'jie':
                if self.regs[reg] % 2 == 0:
                    self.ptr += offset
                else:
                    self.ptr += 1
            elif op == 'jio':
                if self.regs[reg] % 2 == 1:
                    self.ptr += offset
                else:
                    self.ptr += 1


def parse_input(filename: str):
    return ''


def part1(instructions: List[List]) -> int:
    computer = Computer(instructions)
    computer.run()
    return computer.regs[0]


def part2(instructions: List[List]) -> int:
    return 0


def main():
    # data = parse_input('input/dayX.txt')
    instructions = [['inc', 0, 0], ['jio', 0, 2], ['tpl', 0, 0], ['inc', 0, 0]]
    print(f'Part 1: {part1(instructions)}')
    print(f'Part 2: {part2(instructions)}')


if __name__ == "__main__":
    main()
