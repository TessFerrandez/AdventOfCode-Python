from common.helpers import extract_numbers
from typing import List
from collections import defaultdict


OPERATIONS = {
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


def parse_input(filename: str) -> [List, List]:
    with open(filename) as f:
        *sample_blocks, _, program = f.read().split('\n\n')

    samples = [[extract_numbers(line) for line in sample_block.split('\n')] for sample_block in sample_blocks]
    program_lines = [extract_numbers(line) for line in program.split('\n')]

    return samples, program_lines


def find_matching(sample: List[List[int]]) -> List[str]:
    before, instruction, after = sample
    matching = []
    for op in OPERATIONS:
        _, a, b, c = instruction
        result = OPERATIONS[op](before, a, b)
        if after[c] == result:
            matching.append(op)
    return matching


def part1(samples: List[List[List[int]]]) -> int:

    matches_3_or_more = 0
    for sample in samples:
        matching = find_matching(sample)
        if len(matching) >= 3:
            matches_3_or_more += 1
    return matches_3_or_more


def reduce_ops(ops: dict) -> dict:
    reduced = {}
    while ops:
        to_reduce = [op for op in ops if len(ops[op]) == 1]
        for op_number in to_reduce:
            op_name = ops[op_number].pop()
            reduced[op_number] = op_name
            del ops[op_number]
            for op in ops:
                if op_name in ops[op]:
                    ops[op].remove(op_name)
    return reduced


def part2(samples: List[List[List[int]]], program_lines: List[List[int]]) -> int:
    # figure out what operations match what numbers
    ops = defaultdict(lambda: set())
    for sample in samples:
        _, op, _ = sample
        matching = find_matching(sample)
        for operation in matching:
            ops[op[0]].add(operation)

    # reduce until we map numbers and operations
    reduced = reduce_ops(ops)

    # execute program
    registers = [0, 0, 0, 0]
    for instruction in program_lines:
        op, a, b, c = instruction
        registers[c] = OPERATIONS[reduced[op]](registers, a, b)

    return registers[0]


def main():
    samples, program_lines = parse_input('input/day16.txt')
    print(f'Part 1: {part1(samples)}')
    print(f'Part 2: {part2(samples, program_lines)}')


if __name__ == "__main__":
    main()
