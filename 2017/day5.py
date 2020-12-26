from typing import List


def parse_input(filename: str) -> List[int]:
    return [int(line.strip()) for line in open(filename).readlines()]


def part1(instructions: List[int]) -> int:
    in_ptr = 0
    steps = 0
    while in_ptr < len(instructions):
        steps += 1
        jump = instructions[in_ptr]
        instructions[in_ptr] += 1
        in_ptr += jump
    return steps


def part2(instructions: List[int]) -> int:
    in_ptr = 0
    steps = 0
    while in_ptr < len(instructions):
        steps += 1
        jump = instructions[in_ptr]
        if jump >= 3:
            instructions[in_ptr] -= 1
        else:
            instructions[in_ptr] += 1
        in_ptr += jump
    return steps


def main():
    instructions = parse_input('input/day5.txt')
    print(f'Part 1: {part1(instructions)}')
    instructions = parse_input('input/day5.txt')
    print(f'Part 2: {part2(instructions)}')


if __name__ == "__main__":
    main()
