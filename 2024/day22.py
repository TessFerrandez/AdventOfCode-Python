# based on https://github.com/goggle/AdventOfCode2024.jl/blob/main/src/day22.jl
from input_processing import read_data
from collections import defaultdict, deque


def parse(data):
    return [int(x) for x in data.split('\n')]


def prune(num):
    return num % 16777216


def mix(num1, num2):
    return num1 ^ num2


def calculate_secret(secret):
    step1 = prune(mix(secret << 6, secret))
    step2 = prune(mix(step1 >> 5, step1))
    return prune(mix(step2 << 11, step2))


def part1(secrets):
    total = 0
    for secret in secrets:
        for _ in range(2000):
            secret = calculate_secret(secret)
        total += secret
    return total


def part2(secrets):
    num_bananas = defaultdict(int)

    for secret in secrets:
        seen = set()
        diffs = deque()
        next_secret = secret
        price = next_secret % 10

        for _ in range(3):
            next_secret = calculate_secret(next_secret)
            new_price = next_secret % 10
            diffs.append(new_price - price)
            price = new_price

        for _ in range(3, 2001):
            next_secret = calculate_secret(next_secret)
            new_price = next_secret % 10
            diffs.append(new_price - price)
            price = new_price

            diff_sequence = sum([(diffs[-4] + 9) << 15, (diffs[-3] + 9) << 10, (diffs[-2] + 9) << 5, diffs[-1] + 9])
            if diff_sequence not in seen:
                seen.add(diff_sequence)
                num_bananas[diff_sequence] += price

    return max(num_bananas.values())


def test():
    data = '''1
10
100
2024'''
    assert part1(parse(data)) == 37327623
    data = '''1
2
3
2024'''
    assert part2(parse(data)) == 23


test()
data = read_data(2024, 22)
print('Part1:', part1(parse(data)))
print('Part2:', part2(parse(data)))
