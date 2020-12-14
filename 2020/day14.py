import pytest
from typing import List


@pytest.mark.parametrize('before, mask, expected',
                         [
                             (11, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 73),
                             (101, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 101),
                             (0, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 64),
                         ])
def test_apply_mask(before: int, mask: str, expected: int):
    assert apply_mask(before, mask) == expected


@pytest.mark.parametrize('reg, mask, expected',
                         [
                             (26, '00000000000000000000000000000000X0XX', [16, 17, 18, 19, 24, 25, 26, 27]),
                         ])
def test_apply_mask2(reg: int, mask: str, expected: List[int]):
    assert apply_mask2(reg, mask) == expected


def parse_input(filename: str):
    return [line.strip() for line in open(filename).readlines()]


def apply_mask(input_value: int, mask: str) -> int:
    digits = list(format(input_value, 'b').zfill(36))
    for i, m in enumerate(mask):
        if m != 'X':
            digits[i] = m
    return int(''.join(digits), 2)


def apply_mask2(reg: int, mask: str) -> List[int]:
    digits = list(format(reg, 'b').zfill(36))
    floating = []
    for i, m in enumerate(mask):
        if m == 'X':
            floating.append(i)
        if m == '1':
            digits[i] = '1'

    regs = []
    num_floating = len(floating)
    combos = [list(format(i, 'b').zfill(num_floating)) for i in range(2 ** num_floating)]
    for combo in combos:
        digit_copy = digits.copy()
        for i in range(num_floating):
            digit_copy[floating[i]] = combo[i]
        regs.append(int(''.join(digit_copy), 2))
    return regs


def part1(instructions: List[str]) -> int:
    regs = {}
    mask = ''
    for instruction in instructions:
        left, right = instruction.split(' = ')
        if left == 'mask':
            mask = right
        else:
            reg = int(left[4:-1])
            value = int(right)
            regs[reg] = apply_mask(value, mask)
    return sum(regs.values())


def part2(instructions: List[str]) -> int:
    regs = {}
    mask = ''
    for instruction in instructions:
        left, right = instruction.split(' = ')
        if left == 'mask':
            mask = right
        else:
            reg = int(left[4:-1])
            value = int(right)
            regs_to_modify = apply_mask2(reg, mask)
            for r in regs_to_modify:
                regs[r] = value
    return sum(regs.values())


def main():
    instructions = parse_input('input/day14.txt')
    print(f'Part 1: {part1(instructions)}')
    print(f'Part 2: {part2(instructions)}')


if __name__ == "__main__":
    main()
