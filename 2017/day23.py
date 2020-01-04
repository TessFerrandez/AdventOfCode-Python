from collections import defaultdict
from sympy import isprime


def read_input() -> list:
    instructions = [
        instruction.strip().split(" ")
        for instruction in open("input/day23.txt").readlines()
    ]
    return instructions


def execute_instructions(instructions: list, r: dict) -> int:
    regs = "abcdefgh"
    ptr = 0
    num_muls = 0

    while ptr < len(instructions):
        op, p1, p2 = instructions[ptr]
        p2 = r[p2] if p2 in regs else int(p2)

        if op == "set":
            r[p1] = p2
        if op == "sub":
            r[p1] -= p2
        if op == "mul":
            r[p1] *= p2
            num_muls += 1
        if op == "jnz":
            p1 = r[p1] if p1 in regs else int(p1)
            if p1 != 0:
                ptr += p2 - 1
        ptr += 1

    return num_muls


def puzzle2():
    b = 65 * 100 + 100000  # 106500
    c = b + 17000  # 123500
    h = 0

    for b in range(106500, c + 1, 17):
        if not isprime(b):
            h += 1
    print("h:", h)


def puzzles():
    instructions = read_input()
    regs = defaultdict(int)
    num_muls = execute_instructions(instructions, regs)
    print("multiplications:", num_muls)
    puzzle2()


if __name__ == "__main__":
    puzzles()
