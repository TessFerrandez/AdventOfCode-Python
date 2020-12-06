import pytest
from typing import List


@pytest.mark.parametrize('data, expected',
                         [
                             (['ugknbfddgicrmopn'], 1),
                             (['aaa'], 1),
                             (['jchzalrnumimnmhp'], 0),
                             (['haegwjzuvuyypxyu'], 0),
                             (['dvszwmarrgswjxmb'], 0),
                             (['ugknbfddgicrmopn', 'aaa'], 2),
                         ])
def test_part1(data: List[str], expected: int):
    assert part1(data) == expected


@pytest.mark.parametrize('data, expected',
                         [
                             (['qjhvhtzxzqqjkmpb'], 1),
                             (['xxyxx'], 1),
                             (['uurcxstgmygtbstg'], 0),
                             (['ieodomkazucvgmuy'], 0),
                             (['qjhvhtzxzqqjkmpb', 'xxyxx'], 2),
                         ])
def test_part2(data: List[str], expected: int):
    assert part2(data) == expected


def parse_input(filename: str) -> List[str]:
    return [line.strip() for line in open(filename).readlines()]


def contains_3_vowels(password: str) -> bool:
    vowels = []
    for ch in password:
        if ch in 'aeiou':
            vowels.append(ch)
    return len(vowels) >= 3


def contains_double_letter(password: str) -> bool:
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            return True
    return False


def contains_forbidden_strings(password: str) -> bool:
    for forbidden in ['ab', 'cd', 'pq', 'xy']:
        if forbidden in password:
            return True
    return False


def is_valid_password1(password: str) -> bool:
    if not contains_3_vowels(password):
        return False
    if not contains_double_letter(password):
        return False
    if contains_forbidden_strings(password):
        return False
    return True


def has_two_pairs(password: str) -> bool:
    for i in range(len(password) - 2):
        if password[i: i + 2] in password[i + 2:]:
            return True
    return False


def has_a_sandwich(password: str) -> bool:
    for i in range(len(password) - 2):
        if password[i] == password[i + 2]:
            return True
    return False


def is_valid_password2(password: str) -> bool:
    if not has_two_pairs(password):
        return False
    if not has_a_sandwich(password):
        return False
    return True


def part1(data: List[str]) -> int:
    return sum(1 if is_valid_password1(password) else 0 for password in data)


def part2(data: List[str]) -> int:
    return sum(1 if is_valid_password2(password) else 0 for password in data)


def main():
    data = parse_input('input/day5.txt')
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == "__main__":
    main()
