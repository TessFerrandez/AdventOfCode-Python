from typing import List
from collections import defaultdict
from progressbar import ProgressBar


class Computer:
    def __init__(self, instructions: List[List[str]]):
        self.ptr = 0
        self.instructions = instructions
        self.max_ptr = len(instructions)
        self.registers = defaultdict(int)

    def run(self) -> int:
        num_mul = 0

        while self.ptr < self.max_ptr:
            op, x, y = self.instructions[self.ptr]
            # print(self.ptr, op, x, y)
            if op == 'set':
                self.registers[x] = self.val(y)
                self.ptr += 1
            elif op == 'sub':
                self.registers[x] -= self.val(y)
                self.ptr += 1
            elif op == 'mul':
                self.registers[x] *= self.val(y)
                self.ptr += 1
                num_mul += 1
            elif op == 'jnz':
                if self.val(x) != 0:
                    self.ptr += self.val(y)
                else:
                    self.ptr += 1

        return num_mul

    def val(self, y):
        if y in 'abcdefgh':
            return self.registers[y]
        else:
            return int(y)


def parse_input(filename: str):
    return [line.strip().split(' ') for line in open(filename).readlines()]


def part1(instructions: List[List[str]]) -> int:
    c = Computer(instructions)
    num_mul = c.run()
    return num_mul


def part2() -> int:
    """
    b = 65 * 100 + 100000  # 106500
    c = b + 17000
    h = 0

    for b in range(106500, c + 1, 17):
        f = 1
        # check for prime
        for d in range(2, b + 1):
            for e in range(2, b + 1):
                if d * e == b:
                    f = 0
        if f == 0:
            h += 1
    """
    h = 0
    for b in range(106500, 106500 + 17000 + 1, 17):
        for i in range(2, b):
            if b % i == 0:
                h += 1
                break
    return h


def main():
    instructions = parse_input('input/day23.txt')
    print(f'Part 1: {part1(instructions)}')
    print(f'Part 2: {part2()}')


if __name__ == "__main__":
    main()
