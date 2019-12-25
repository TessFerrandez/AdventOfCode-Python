def read_instructions() -> list:
    lines = open("input/day23.txt").readlines()
    instructions = []
    for line in lines:
        line = line.strip()
        op = line[0:3]
        instruction = [op] + line[4:].split(", ")
        instructions.append(instruction)
    return instructions


def execute_instructions(instructions: list, registers: dict):
    instr_ptr = 0
    while instr_ptr < len(instructions):
        instruction = instructions[instr_ptr]
        op = instruction[0]
        if op == "inc":
            registers[instruction[1]] += 1
            instr_ptr += 1
        elif op == "tpl":
            registers[instruction[1]] *= 3
            instr_ptr += 1
        elif op == "hlf":
            registers[instruction[1]] /= 2
            instr_ptr += 1
        elif op == "jio":
            offset = int(instruction[2])
            reg = instruction[1]
            if registers[reg] == 1:
                instr_ptr += offset
            else:
                instr_ptr += 1
        elif op == "jmp":
            offset = int(instruction[1])
            instr_ptr += offset
        elif op == "jie":
            offset = int(instruction[2])
            reg = instruction[1]
            if registers[reg] % 2 == 0:
                instr_ptr += offset
            else:
                instr_ptr += 1
        else:
            print(instruction)
            raise Exception


def puzzles():
    instructions = read_instructions()
    registers = {"a": 0, "b": 0}
    execute_instructions(instructions, registers)
    print("b register:", registers["b"])
    registers = {"a": 1, "b": 0}
    execute_instructions(instructions, registers)
    print("b register:", registers["b"])


if __name__ == "__main__":
    puzzles()
