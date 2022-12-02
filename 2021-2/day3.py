from typing import List


def part1(lines: List[str]):
    n = len(lines[0])
    ones = [0 for _ in range(n)]

    for line in lines:
        for i in range(n):
            ones[i] += 1 if line[i] == '1' else 0

    count = len(lines)
    half = count // 2

    gamma = ''
    epsilon = ''

    for one in ones:
        if one > half:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    igamma = int(gamma, 2)
    iepsilon = int(epsilon, 2)

    return igamma * iepsilon


def part2(lines: List[str]) -> int:
    oxygen = lines[::]
    bit = 0
    while len(oxygen) > 1:
        ones = sum(1 if num[bit] == '1' else 0 for num in oxygen)
        all = len(oxygen)
        zeros = all - ones
        if ones >= zeros:
            oxygen = [number for number in oxygen if number[bit] == '1']
        else:
            oxygen = [number for number in oxygen if number[bit] == '0']
        bit += 1

    oxygen = int(oxygen[0], 2)

    co2 = lines[::]
    bit = 0
    while len(co2) > 1:
        ones = sum(1 if num[bit] == '1' else 0 for num in co2)
        all = len(co2)
        zeros = all - ones
        if zeros <= ones:
            co2 = [number for number in co2 if number[bit] == '0']
        else:
            co2 = [number for number in co2 if number[bit] == '1']
        bit += 1

    co2 = int(co2[0], 2)

    return co2 * oxygen


lines = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''.splitlines()

assert part1(lines) == 198
assert part2(lines) == 230

lines = [line.strip() for line in open('./2021/input/day3.txt').readlines()]
print('Part1:', part1(lines))
print('Part1:', part2(lines))
