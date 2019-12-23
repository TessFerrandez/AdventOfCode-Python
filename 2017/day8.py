from Instruction import Instruction


def get_register(registers, register) -> int:
    if register in registers:
        return registers[register]
    else:
        return 0


def compare(left: int, op: str, right: int) -> bool:
    if op == ">":
        return left > right
    if op == "<":
        return left < right
    if op == ">=":
        return left >= right
    if op == "<=":
        return left <= right
    if op == "==":
        return left == right
    if op == "!=":
        return left != right
    return False


def result_of(left: int, op: str, right: int) -> int:
    if op == "inc":
        return left + right
    else:
        return left - right


def execute_instructions(instructions: list) -> (dict, int):
    registers = dict()

    total_max = 0
    for instr in instructions:
        left_reg = get_register(registers, instr.left_comp)
        if compare(left_reg, instr.comp, instr.right_comp):
            dest_reg = get_register(registers, instr.dest)
            result = result_of(dest_reg, instr.op, instr.by)
            registers[instr.dest] = result
            total_max = max(total_max, result)

    return registers, total_max


def puzzles():
    instructions = [Instruction(line) for line in open("input/day8.txt").readlines()]
    registers, total_max = execute_instructions(instructions)
    print("max register:", max([registers[reg] for reg in registers]))
    print("all time max register:", total_max)


if __name__ == "__main__":
    puzzles()
