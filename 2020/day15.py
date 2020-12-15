import pytest
import progressbar
from typing import List
from collections import defaultdict


@pytest.mark.parametrize('data, turn, expected',
                         [
                             ([0, 3, 6], 10, 0),
                             ([0, 3, 6], 2020, 436),
                             ([1, 3, 2], 2020, 1),
                             ([2, 1, 3], 2020, 10),
                             ([1, 2, 3], 2020, 27),
                             ([2, 3, 1], 2020, 78),
                             ([3, 2, 1], 2020, 438),
                             ([3, 1, 2], 2020, 1836),
                         ])
def test_part1(data: List[int], turn: int, expected: int):
    assert part1(data, turn) == expected


@pytest.mark.parametrize('data, turn, expected',
                         [
                             ([0, 3, 6], 10, 0),
                             ([0, 3, 6], 2020, 436),
                             ([0, 3, 6], 30000000, 175594),
                             ([1, 3, 2], 30000000, 2578),
                             ([2, 1, 3], 30000000, 3544142),
                             ([1, 2, 3], 30000000, 261214),
                             ([2, 3, 1], 30000000, 6895259),
                             ([3, 2, 1], 30000000, 18),
                             ([3, 1, 2], 30000000, 362),
                         ])
def test_part2(data: List[int], turn: int, expected: int):
    assert part2(data, turn) == expected


def last_index(the_list: List[int], value: int) -> int:
    try:
        return the_list[:-1][::-1].index(value) + 1
    except ValueError:
        return 0


def part1(input_numbers: List[int], turn: int) -> int:
    with progressbar.ProgressBar(max_value=turn, redirect_stdout=True) as p:
        numbers = input_numbers.copy()
        current_turn = len(numbers)
        while current_turn < turn:
            numbers.append(last_index(numbers, numbers[-1]))
            current_turn += 1
            p.update(current_turn)
    return numbers[-1]


def part2(input_numbers: List[int], turn: int) -> int:
    turns = defaultdict(int)
    for i, number in enumerate(input_numbers):
        turns[number] = i + 1

    with progressbar.ProgressBar(max_value=turn, redirect_stdout=True) as p:
        current_turn = len(input_numbers) + 1
        current_number = 0
        while current_turn < turn:
            if turns[current_number] == 0:
                turns[current_number] = current_turn
                current_number = 0
            else:
                next_number = current_turn - turns[current_number]
                turns[current_number] = current_turn
                current_number = next_number
            current_turn += 1
            p.update(current_turn)
    return current_number


def main():
    input_numbers = [0, 8, 15, 2, 12, 1, 4]
    print(f'Part 1: {part1(input_numbers, 2020)}')
    print(f'Part 2: {part2(input_numbers, 30000000)}')


if __name__ == "__main__":
    main()
