from typing import List


def parse_input(filename: str) -> List[int]:
    return [int(d.strip()) for d in open(filename).readlines()]


def part1(changes: List[int]) -> int:
    return sum(changes)


def part2(changes: List[int]) -> int:
    seen = []
    i = 0
    max_i = len(changes)
    frequency = 0
    while True:
        frequency += changes[i]
        if frequency in seen:
            return frequency
        seen.append(frequency)
        i += 1
        if i == max_i:
            i = 0


def main():
    changes = parse_input('input/day1.txt')
    print(f'Part 1: {part1(changes)}')
    print(f'Part 2: {part2(changes)}')


if __name__ == "__main__":
    main()
