from typing import List
from copy import copy


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


def parse_input(filename: str) -> (int, List[List]):
    lines = open(filename).read().splitlines()
    _, ip_reg = lines[0].split(' ')
    ip_reg = int(ip_reg)

    instructions = []
    for line in lines[1:]:
        op, a, b, c = line.split(' ')
        instructions.append([op, int(a), int(b), int(c)])

    return ip_reg, instructions


def part1_original(ip_reg: int, instructions: List[List], regs: List[int]) -> int:
    ip = 0
    max_ip = len(instructions)

    i = 0
    while ip < max_ip and i < 100:
        i += 1
        op, a, b, c = instructions[ip]
        before = copy(regs)
        regs[c] = OPERATIONS[op](regs, a, b)
        print(f'ip={ip} {before} {op} {a} {b} {c} {regs}')
        regs[ip_reg] += 1
        ip = regs[ip_reg]

    return regs[0]


def get_divisors(n: int) -> List[int]:
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            yield i
    yield n


def get_sum_of_divisors(input_number: int) -> int:
    divisors = list(get_divisors(input_number))
    return sum(divisors)


def part2_reverse_engineer() -> int:
    v0 = 0
    v1 = 10551309       # v1 = (2 * 2 * 19 * 11) + (3 * 22 + 7) + ((27 * 28 + 29) * 30 * 14 * 32)

    v5 = 1
    while True:
        v3 = 1
        while True:
            if v5 * v3 == v1:
                v0 += v5
            v3 += 1
            if v3 > v1:
                break
        v5 += 1
        if v5 > v1:
            break

    return v0


def main():
    ip_reg, instructions = parse_input('input/day19.txt')
    # print(f'Part 1: {part1_original(ip_reg, instructions, [0, 0, 0, 0, 0, 0])}')
    # print(f'Part 2: {part1_original(ip_reg, instructions, [1, 0, 0, 0, 0, 0])}')

    # after reverse engineering
    part1_number = 909          # (2 * 2 * 19 * 11) + (3 * 22 + 7)
    print(f'Part 1: {get_sum_of_divisors(part1_number)}')
    part2_number = 10551309     # (2 * 2 * 19 * 11) + (3 * 22 + 7) + ((27 * 28 + 29) * 30 * 14 * 32)
    print(f'Part 2: {get_sum_of_divisors(part2_number)}')


if __name__ == "__main__":
    main()
