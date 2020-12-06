import pytest
from string import ascii_lowercase
from itertools import groupby


@pytest.mark.parametrize('data, expected',
                         [
                             ('hijklmmn', False),
                             ('abbceffg', False),
                             ('abbcdgjk', False),
                             ('abcdffaa', True),
                             ('ghjaabcc', True)
                         ])
def test_is_valid(data: str, expected: int):
    assert is_valid(data) == expected


@pytest.mark.parametrize('data, expected',
                         [
                             ('abcdefgh', 'abcdffaa'),
                             ('ghijklmn', 'ghjaabcc'),
                         ])
def test_part1(data: str, expected: int):
    assert part1(data) == expected


def is_valid(password: str) -> bool:
    if len(set('iol') & set(password)) > 0:
        return False
    if not any([ascii_lowercase[n: n + 3] in password for n in range(24)]):
        return False
    if sum([2 if len(list(y)) >= 4 else 1 for x, y in groupby(password) if len(list(y)) >= 2]) < 2:
        return False
    return True


def inc(password: str) -> str:
    if password == '':
        return ''
    elif password[-1] < 'z':
        return password[0: -1] + chr(ord(password[-1]) + 1)
    else:
        return inc(password[: -1]) + 'a'


def part1(password: str) -> str:
    while not is_valid(password):
        password = inc(password)
    return password


def part2(password: str) -> str:
    password = inc(password)
    while not is_valid(password):
        password = inc(password)
    return password


def main():
    part1_result = part1('hepxcrrq')
    print(f'Part 1: {part1_result}')
    print(f'Part 2: {part2(part1_result)}')


if __name__ == "__main__":
    main()
