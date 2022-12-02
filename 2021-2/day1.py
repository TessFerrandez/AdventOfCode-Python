from typing import List


def part1(numbers: List[int]) -> int:
    return sum(1 if numbers[i] > numbers[i - 1] else 0 for i in range(1, len(numbers)))


def part2(numbers: List[int]) -> int:
    prev = sum(numbers[:3])
    count = 0

    for i in range(3, len(numbers)):
        current = prev - numbers[i - 3] + numbers[i]
        if current > prev:
            count += 1
        prev = current

    return count


assert part1([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 7
assert part2([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 5

numbers = [int(d.strip()) for d in open('./2021/input/day1.txt').readlines()]
print('Part1:', part1(numbers))
print('Part2:', part2(numbers))
