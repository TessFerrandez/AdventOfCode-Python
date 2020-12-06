import pytest


@pytest.mark.parametrize('input_str, expected',
                         [
                             ('(())', 0),
                             ('()()', 0),
                             ('(((', 3),
                             ('(()(()(', 3),
                             ('))(((((', 3),
                             ('())', -1),
                             ('))(', -1),
                             (')))', -3),
                             (')())())', -3),
                         ])
def test_calculate_floor(input_str: str, expected: int):
    assert calculate_floor(input_str) == expected


@pytest.mark.parametrize('input_str, expected',
                         [
                             (')', 1),
                             ('()())', 5),
                         ])
def test_calculate_first_basement(input_str: str, expected: int):
    assert calculate_first_basement(input_str) == expected


def calculate_floor(instructions: str) -> int:
    return instructions.count('(') - instructions.count(')')


def calculate_first_basement(instructions: str) -> int:
    floor = 0
    for i, ch in enumerate(instructions):
        floor += 1 if ch == '(' else -1
        if floor == -1:
            return i + 1
    return -1


def puzzle1(instructions: str) -> int:
    return calculate_floor(instructions)


def puzzle2(instructions: str) -> int:
    return calculate_first_basement(instructions)


def main():
    instructions = open('input/day1.txt').read().strip()
    print(f'Puzzle 1: {puzzle1(instructions)}')
    print(f'Puzzle 2: {puzzle2(instructions)}')


if __name__ == "__main__":
    main()
