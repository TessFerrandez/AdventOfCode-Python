import re
from typing import List, Tuple


def get_ops() -> dict:
    return {
        "addr": lambda r, a, b: r[a] + r[b],
        "addi": lambda r, a, b: r[a] + b,
        "mulr": lambda r, a, b: r[a] * r[b],
        "muli": lambda r, a, b: r[a] * b,
        "banr": lambda r, a, b: r[a] & r[b],
        "bani": lambda r, a, b: r[a] & b,
        "borr": lambda r, a, b: r[a] | r[b],
        "bori": lambda r, a, b: r[a] | b,
        "setr": lambda r, a, b: r[a],
        "seti": lambda r, a, b: a,
        "gtir": lambda r, a, b: 1 if a > r[b] else 0,
        "gtri": lambda r, a, b: 1 if r[a] > b else 0,
        "gtrr": lambda r, a, b: 1 if r[a] > r[b] else 0,
        "eqir": lambda r, a, b: 1 if a == r[b] else 0,
        "eqri": lambda r, a, b: 1 if r[a] == b else 0,
        "eqrr": lambda r, a, b: 1 if r[a] == r[b] else 0,
    }


def parse_input(filename: str) -> (List, int):
    lines = [line.strip() for line in open(filename).readlines()]

    instructions = []
    first_line = lines.pop(0)
    ip = int(first_line.split(' ')[1])

    for line in lines:
        parts = line.split(' ')
        instructions.append((parts[0], int(parts[1]), int(parts[2]), int(parts[3])))

    return instructions, ip


def run_program(instructions: List, ip: int) -> List[int]:
    max_ip = len(instructions)
    ops = get_ops()
    regs = [ip, 0, 0, 0, 0, 0]

    i = 0
    while i < 35:
        # while True:
        op, a, b, c = instructions[ip]
        print(op, a, b, c)
        regs[c] = ops[op](regs, a, b)
        print(regs)
        ip = regs[0] + 1
        if ip >= max_ip:
            break
        regs[0] = regs[0] + 1
        i += 1

    return regs


def puzzle1(instructions: List, ip: int) -> int:
    regs = run_program(instructions, ip)
    return regs[0]


def puzzle2(instructions: List, ip: int) -> int:
    return 0


def main():
    instructions, ip = parse_input('input/day19.txt')
    puzzle1_result = puzzle1(instructions, ip)
    print(f"Puzzle 1: {puzzle1_result}")
    puzzle2_result = puzzle2(instructions, ip)
    print(f"Puzzle 2: {puzzle2_result}")


if __name__ == "__main__":
    main()
