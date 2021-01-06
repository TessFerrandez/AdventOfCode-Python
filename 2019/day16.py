from typing import List


def parse_input(filename: str) -> str:
    return open(filename).read().strip()


def get_pattern(i: int) -> List[int]:
    base_pattern = [0, 1, 0, -1]
    return [digit for digit in base_pattern for _ in range(i)]


def get_number(input_signal: List[int], pattern: List[int]) -> int:
    digit_sum = sum(input_signal[index] * pattern[(index + 1) % len(pattern)] for index in range(len(input_signal)))
    number = abs(digit_sum) % 10
    return number


def iterate(input_signal: List[int]):
    result = []
    for i in range(1, len(input_signal) + 1):
        pattern = get_pattern(i)
        number = get_number(input_signal, pattern)
        result.append(number)
    return result


def part1(input_signal: str) -> str:
    input_signal = [int(digit) for digit in input_signal]
    for phase in range(100):
        input_signal = iterate(input_signal)
    return ''.join(str(digit) for digit in input_signal[:8])


def part2(data: str) -> int:
    return 0


def main():
    data = parse_input('input/day16.txt')
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == "__main__":
    main()
