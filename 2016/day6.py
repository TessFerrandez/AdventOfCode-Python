from typing import List
from collections import Counter


def parse_input(filename: str) -> List[str]:
    return [line.strip() for line in open(filename).readlines()]


def part1(messages: List[str]) -> str:
    num_cols = len(messages[0])
    column_letters = [[] for _ in range(num_cols)]

    for message in messages:
        for column in range(num_cols):
            column_letters[column].append(message[column])

    corrected_message = ''
    for column in range(num_cols):
        corrected_message += Counter(column_letters[column]).most_common()[0][0]
    return corrected_message


def part2(messages: List[str]) -> str:
    num_cols = len(messages[0])
    column_letters = [[] for _ in range(num_cols)]

    for message in messages:
        for column in range(num_cols):
            column_letters[column].append(message[column])

    corrected_message = ''
    for column in range(num_cols):
        corrected_message += Counter(column_letters[column]).most_common()[-1][0]
    return corrected_message


def main():
    # messages = parse_input('input/day6_test.txt')
    messages = parse_input('input/day6.txt')
    print(f'Part 1: {part1(messages)}')
    print(f'Part 2: {part2(messages)}')


if __name__ == "__main__":
    main()
