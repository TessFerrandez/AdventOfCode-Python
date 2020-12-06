import pytest
from typing import List


@pytest.mark.parametrize('data, expected',
                         [
                             ([r'""'], 2),
                             ([r'"abc"'], 2),
                             ([r'"aaa\"aaa"'], 3),
                             ([r'"\x27"'], 5),
                             ([r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"'], 12),
                         ])
def test_part1(data: List[str], expected: int):
    assert part1(data) == expected


@pytest.mark.parametrize('data, expected',
                         [
                             ([r'""'], 4),
                             ([r'"abc"'], 4),
                             ([r'"aaa\"aaa"'], 6),
                             ([r'"\x27"'], 5),
                             ([r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"'], 19),
                         ])
def test_part2(data: List[str], expected: int):
    assert part2(data) == expected


def parse_input(filename: str) -> List[str]:
    return [line.strip() for line in open(filename).readlines()]


def part1(data: List[str]) -> int:
    sums = 0
    for code in data:
        original_len = len(code)
        decoded_len = len(bytes(code[1:-1], "utf-8").decode('unicode-escape'))
        sums += original_len - decoded_len
    return sums


def part2(data: List[str]) -> int:
    sums = 0
    for code in data:
        original_len = len(code)
        encoded_string = code.replace('\\', '\\\\').replace('"', '\\"')
        encoded_string = '"' + encoded_string + '"'
        encoded_len = len(encoded_string)
        sums += encoded_len - original_len
    return sums


def main():
    data = parse_input('input/day8.txt')
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == "__main__":
    main()
