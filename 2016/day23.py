from collections import defaultdict
from math import factorial


def read_input() -> list:
    instructions = [
        instruction.strip().split()
        for instruction in open("input/day23.txt").readlines()
    ]
    return instructions


def execute_program(instructions: list, r: dict):
    regs = "abcd"
    i = 0
    while i < len(instructions):
        instr = instructions[i]
        op = instr[0]
        p1 = instr[1]
        p2 = instr[2] if len(instr) > 2 else None

        if op == "cpy":
            if p2 in regs:
                p1 = r[p1] if p1 in regs else int(p1)
                r[p2] = p1
            i += 1
        elif op == "inc":
            if p1 in regs:
                r[p1] += 1
            i += 1
        elif op == "dec":
            if p1 in regs:
                r[p1] -= 1
            i += 1
        elif op == "jnz":
            p1 = r[p1] if p1 in regs else int(p1)
            p2 = r[p2] if p2 in regs else int(p2)
            if p1 != 0:
                i += p2
            else:
                i += 1
        elif op == "tgl":
            p1 = r[p1] if p1 in regs else int(p1)
            target_i = i + p1
            if 0 <= target_i < len(instructions):
                target = instructions[target_i]
                if len(target) == 2:
                    target[0] = "dec" if target[0] == "inc" else "inc"
                else:
                    target[0] = "cpy" if target[0] == "jnz" else "jnz"
            i += 1


def puzzles():
    registers = defaultdict()
    registers["a"] = 7
    instructions = read_input()
    execute_program(instructions, registers)
    print("reg a:", registers["a"])
    print("reg a:", 84 * 80 + factorial(12))


if __name__ == "__main__":
    puzzles()
