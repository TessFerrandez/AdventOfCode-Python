from collections import defaultdict


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
                # peephole optimize inc/dec/jnz loops
                """
                cpy a d
                cpy 14 c
                cpy 182 b
                0 >> inc d
                dec b
                jnz b -2
                dec c
                jnz c -5
                """
                if ((i + 3) < len(instructions) and i - 1 >= 0 and instructions[i - 1][0] == "cpy" and instructions[i + 1][0] == "dec" and instructions[i + 2][0] == "jnz" and instructions[i + 3][0] == "dec" and instructions[i + 4][0] == "jnz"):
                    cpysrc, cpydest = instructions[i - 1][1], instructions[i - 1][2]
                    dec1op = instructions[i + 1][1]
                    jnz1cond, jnz1off = instructions[i + 2][1], instructions[i + 2][2]
                    dec2op = instructions[i + 3][1]
                    jnz2cond, jnz2off = instructions[i + 4][1], instructions[i + 4][2]

                    if (cpydest == dec1op and dec1op == jnz1cond and dec2op == jnz2cond and jnz1off == "-2" and jnz2off == "-5"):
                        cpysrc = r[cpysrc] if cpysrc in regs else int(cpysrc)
                        r[p1] += cpysrc * r[dec2op]
                        r[dec2op] = 0
                        r[dec1op] = 0
                        i += 5
                        continue

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
    registers = defaultdict()
    registers["a"] = 12
    instructions = read_input()
    execute_program(instructions, registers)
    print("reg a:", registers["a"])


if __name__ == "__main__":
    puzzles()
