def execute_program(registers: dict):
    instructions = [
        line.strip().split() for line in open("input/day12.txt").readlines()
    ]
    instr_ptr = 0
    while instr_ptr < len(instructions):
        instruction = instructions[instr_ptr]
        op = instruction[0]
        if op == "cpy":
            fr = instruction[1]
            to = instruction[2]
            if fr in registers:
                registers[to] = registers[fr]
            else:
                registers[to] = int(fr)
            instr_ptr += 1
        elif op == "inc":
            registers[instruction[1]] += 1
            instr_ptr += 1
        elif op == "dec":
            registers[instruction[1]] -= 1
            instr_ptr += 1
        elif op == "jnz":
            if instruction[1] in registers:
                cmp = registers[instruction[1]]
            else:
                cmp = int(instruction[1])

            if cmp != 0:
                instr_ptr += int(instruction[2])
            else:
                instr_ptr += 1


def puzzles():
    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    execute_program(registers)
    print("register a:", registers["a"])
    registers = {"a": 0, "b": 0, "c": 1, "d": 0}
    execute_program(registers)
    print("register a:", registers["a"])


if __name__ == "__main__":
    puzzles()
