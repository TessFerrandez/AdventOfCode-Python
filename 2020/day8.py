from typing import List
from copy import deepcopy


def parse_input(filename: str) -> List[List]:
    instructions = []
    lines = [line.strip() for line in open(filename).readlines()]
    for line in lines:
        op, param = line.split()
        instructions.append([op, int(param)])
    return instructions


def run_program(instructions: List[List]) -> (int, bool):
    max_ptr = len(instructions)
    visited_instructions = set()
    in_ptr = 0
    accumulator = 0

    while in_ptr not in visited_instructions and in_ptr < max_ptr:
        visited_instructions.add(in_ptr)
        op, param = instructions[in_ptr]
        if op == 'acc':
            accumulator += param
            in_ptr += 1
        elif op == 'nop':
            in_ptr += 1
        elif op == 'jmp':
            in_ptr += param
    return accumulator, in_ptr == max_ptr


def part1(instructions: List[List]) -> int:
    accumulator, _ = run_program(instructions)
    return accumulator


def get_jmp_and_nop_instructions(instructions: List[List]) -> (List[int], List[int]):
    jmp_instructions = []
    nop_instructions = []
    for i, instruction in enumerate(instructions):
        op, _ = instruction
        if op == 'jmp':
            jmp_instructions.append(i)
        elif op == 'nop':
            nop_instructions.append(i)
    return jmp_instructions, nop_instructions


def part2(instructions: List[List]) -> int:
    jumps, no_ops = get_jmp_and_nop_instructions(instructions)
    for jump in jumps:
        instruction_copy = deepcopy(instructions)
        instruction_copy[jump][0] = 'nop'
        accumulator, finished = run_program(instruction_copy)
        if finished:
            return accumulator
    for noop in no_ops:
        instruction_copy = deepcopy(instructions)
        instruction_copy[noop][0] = 'jmp'
        accumulator, finished = run_program(instruction_copy)
        if finished:
            return accumulator
    return 0


def main():
    instructions = parse_input('input/day8.txt')
    print(f'Part 1: {part1(instructions)}')
    print(f'Part 2: {part2(instructions)}')


if __name__ == "__main__":
    main()
