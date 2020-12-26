import pytest
from typing import List


def remove_exclamations(input_str: str) -> str:
    result = ''
    i = 0
    while i < len(input_str):
        if input_str[i] != '!':
            result += input_str[i]
        else:
            i += 1
        i += 1
    return result


@pytest.mark.parametrize('data, expected',
                         [
                             ('<{!>}>', '<{}>'),
                             ('<!!>', '<>'),
                             ('<!!!>>', '<>'),
                             ('<{o"i!a,<{i<a>', '<{o"i,<{i<a>'),
                         ])
def test_remove_exclamations(data: str, expected: str):
    assert remove_exclamations(data) == expected


def remove_garbage(input_str: str) -> (str, int):
    num_removed = 0
    while True:
        try:
            garbage_start = input_str.index('<')
        except ValueError:
            break
        garbage_end = input_str.index('>')
        before = input_str[:garbage_start]
        after = input_str[garbage_end + 1:]
        input_str = before + after
        num_removed += 1
    return input_str, num_removed


@pytest.mark.parametrize('data, expected',
                         [
                             ('<>', ''),
                             ('<random characters>', ''),
                             ('<<<<>', ''),
                             ('<{!>}>', ''),
                             ('<!!>', ''),
                             ('<!!!>>', ''),
                             ('<{o"i!a,<{i<a>', ''),
                             ('{<a>,<a>,<a>,<a>}', '{,,,}'),
                             ('{{<!!>},{<!!>},{<!!>},{<!!>}}', '{{},{},{},{}}'),
                             ('{{<a!>},{<a!>},{<a!>},{<ab>}}', '{{}}')
                         ])
def test_remove_garbage(data: str, expected: str):
    data = remove_exclamations(data)
    assert remove_garbage(data) == expected


def get_group_score(input_str: str) -> int:
    total = 0
    level = 0
    for ch in input_str:
        if ch == '{':
            level += 1
        elif ch == '}':
            total += level
            level -= 1
    return total


@pytest.mark.parametrize('data, expected',
                         [
                             ('{}', 1),
                             ('{{{}}}', 6),
                             ('{{},{}}', 5),
                             ('{{{},{},{{}}}}', 16),
                             ('{<a>,<a>,<a>,<a>}', 1),
                             ('{{<ab>},{<ab>},{<ab>},{<ab>}}', 9),
                             ('{{<!!>},{<!!>},{<!!>},{<!!>}}', 9),
                             ('{{<a!>},{<a!>},{<a!>},{<ab>}}', 3),
                         ])
def test_get_group_score(data: str, expected: int):
    data = remove_exclamations(data)
    data, _ = remove_garbage(data)
    assert get_group_score(data) == expected


def parse_input(filename: str) -> List[str]:
    return [line.strip() for line in open(filename).readlines()]


def part1(strings: List[str]) -> int:
    strings = [remove_exclamations(string) for string in strings]
    no_garbage = []
    for string in strings:
        clean, _ = remove_garbage(string)
        no_garbage.append(clean)
    return sum(get_group_score(string) for string in no_garbage)


def part2(strings: List[str]) -> int:
    strings = [remove_exclamations(string) for string in strings]
    total_garbage = 0
    for string in strings:
        clean, num_garbage = remove_garbage(string)
        garbage_amount = len(string) - len(clean) - 2 * num_garbage
        total_garbage += garbage_amount
    return total_garbage


def main():
    data = parse_input('input/day9.txt')
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == "__main__":
    main()
