from typing import List, Tuple


def parse_input(filename: str) -> List[Tuple]:
    instruction_strings = open(filename).read().strip().split(',')
    instructions = []
    for instruction in instruction_strings:
        op = instruction[0]
        if op == 's':
            p1 = int(instruction[1:])
            p2 = 0
        if op == 'x':
            p1, p2 = [int(d) for d in instruction[1:].split('/')]
        if op == 'p':
            p1, p2 = instruction[1:].split('/')
        instructions.append((op, p1, p2))
    return instructions


def spin(programs: List[str], p: int) -> List[str]:
    return programs[-p:] + programs[:-p]


def swap(programs: List[str], a: int, b: int):
    programs[a], programs[b] = programs[b], programs[a]


def swap_by_name(programs: List[str], p1: str, p2: str):
    i1 = programs.index(p1)
    i2 = programs.index(p2)
    swap(programs, i1, i2)


def run(instructions: List[Tuple], programs: List[str]) -> List[str]:
    for instruction in instructions:
        op, p1, p2 = instruction
        if op == 's':
            programs = spin(programs, p1)
        if op == 'x':
            swap(programs, p1, p2)
        if op == 'p':
            swap_by_name(programs, p1, p2)
    return programs


def part1(instructions: List[Tuple], programs: List[str]) -> str:
    programs = run(instructions, programs)
    return ''.join(programs)


def part2(instructions: List[Tuple], programs: List[str]) -> str:
    seen = []
    i = 0
    while True:
        state = ''.join(programs)
        if state in seen:
            break
        seen.append(state)
        programs = run(instructions, programs)
        i += 1

    for j in range(1000000000 % i):
        programs = run(instructions, programs)

    return ''.join(programs)


def main():
    # instructions = parse_input('input/day16_test.txt')
    # programs = list('abcde')
    instructions = parse_input('input/day16.txt')
    programs = list('abcdefghijklmnop')
    print(f'Part 1: {part1(instructions, programs)}')
    programs = list('abcdefghijklmnop')
    print(f'Part 2: {part2(instructions, programs)}')


if __name__ == "__main__":
    main()
