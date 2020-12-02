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


def parse_input() -> Tuple[List, List]:
    with open("input/day16.txt") as f:
        *sample_blocks, _, program = f.read().split("\n\n")

    samples = []
    for sample_block in sample_blocks:
        sample = [
            [int(digit) for digit in re.findall(r"-?\d+", line)]
            for line in sample_block.split("\n")
        ]
        samples.append(sample)

    program_lines = [
        [int(digit) for digit in re.findall(r"-?\d+", line)]
        for line in program.split("\n")
    ]

    return samples, program_lines


def find_matching(sample: List[List[int]], ops: dict) -> List[str]:
    before, instruction, after = sample
    matching = []
    for op in ops:
        operand, a, b, c = instruction
        result = ops[op](before, a, b)
        if after[c] == result:
            matching.append(op)
    return matching


def puzzle1(samples: List[List[List[int]]]) -> int:
    ops = get_ops()
    over_or_equal_to_3 = 0
    for sample in samples:
        matching = find_matching(sample, ops)
        if len(matching) >= 3:
            over_or_equal_to_3 += 1
    return over_or_equal_to_3


def decode_operators(samples: List[List[List[int]]]) -> dict:
    ops = get_ops()
    possible = {}
    for sample in samples:
        op_number = sample[1][0]
        matching = find_matching(sample, ops)
        if op_number in possible:
            possible[op_number] = possible[op_number] - (
                possible[op_number] - set(matching)
            )
        else:
            possible[op_number] = set(matching)

    # decode numbers
    op_map = {}
    while possible:
        decoded_op = ""
        for op in possible:
            if len(possible[op]) == 1:
                decoded_op = op
                op_map[op] = possible[op].pop()
                for op2 in possible:
                    if op_map[op] in possible[op2]:
                        possible[op2].remove(op_map[op])
                break
        del possible[decoded_op]
    return op_map


def run_program(program: List[List[int]], op_map: dict) -> List[int]:
    regs = [0, 0, 0, 0]
    ops = get_ops()

    for line in program:
        op, a, b, c = line
        c_out = ops[op_map[op]](regs, a, b)
        regs[c] = c_out
    return regs


def puzzle2(samples: List[List[List[int]]], program: List[List[int]]) -> int:
    op_map = decode_operators(samples)
    regs = run_program(program, op_map)
    return regs[0]


def main():
    samples, program = parse_input()
    puzzle1_result = puzzle1(samples)
    print(f"Puzzle 1: {puzzle1_result}")
    puzzle2_result = puzzle2(samples, program)
    print(f"Puzzle 2: {puzzle2_result}")


if __name__ == "__main__":
    main()
