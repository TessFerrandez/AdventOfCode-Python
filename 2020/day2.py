import pytest
from typing import Tuple, List


@pytest.mark.parametrize(
    "password_info, expected",
    [
        ((1, 3, "a", "abcde"), True),
        ((1, 3, "b", "cdefg"), False),
        ((2, 9, "c", "ccccccccc"), True),
    ],
)
def test_is_valid_password(password_info, expected):
    assert is_valid_password(password_info) == expected


@pytest.mark.parametrize(
    "password_info, expected",
    [
        ((1, 3, "a", "abcde"), True),
        ((1, 3, "b", "cdefg"), False),
        ((2, 9, "c", "ccccccccc"), False),
    ],
)
def test_is_valid_password2(password_info, expected):
    assert is_valid_password2(password_info) == expected


def is_valid_password(password_info: Tuple[int, int, chr, str]) -> bool:
    min_letters, max_letters, letter, password = password_info
    count_letter = password.count(letter)
    return min_letters <= count_letter <= max_letters


def is_valid_password2(password_info: Tuple[int, int, chr, str]) -> bool:
    pos1, pos2, letter, password = password_info
    if password[pos1 - 1] == letter and not password[pos2 - 1] == letter:
        return True
    if password[pos2 - 1] == letter and not password[pos1 - 1] == letter:
        return True
    return False


def parse_input() -> List[Tuple[int, int, chr, str]]:
    with open("input/day2.txt") as f:
        lines = f.readlines()
    password_infos = []
    for line in lines:
        parts = line.split(" ")
        min_letters, max_letters = (int(number) for number in parts[0].split("-"))
        letter = parts[1][:-1]
        password = parts[2].strip()
        password_infos.append((min_letters, max_letters, letter, password))
    return password_infos


def puzzle1(password_infos: List[Tuple[int, int, chr, str]]) -> int:
    return sum(
        1 if is_valid_password(password_info) else 0 for password_info in password_infos
    )


def puzzle2(password_infos: List[Tuple[int, int, chr, str]]) -> int:
    return sum(
        1 if is_valid_password2(password_info) else 0
        for password_info in password_infos
    )


def main():
    password_infos = parse_input()
    puzzle1_results = puzzle1(password_infos)
    print(f"Puzzle 1: {puzzle1_results}")
    puzzle2_results = puzzle2(password_infos)
    print(f"Puzzle 2: {puzzle2_results}")


if __name__ == "__main__":
    main()
