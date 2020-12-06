import pytest
import hashlib


@pytest.mark.parametrize('data, expected',
                         [
                             ('abcdef', 609043),
                             ('pqrstuv', 1048970),
                         ])
def test_part1(data: str, expected: int):
    assert part1(data) == expected


def hash_starts_with(number: int, secret_key: str, starts_with='00000') -> int:
    string_to_hash = secret_key + str(number)
    hashed = hashlib.md5(str(string_to_hash).encode('utf-8')).hexdigest()
    return hashed.startswith(starts_with)


def part1(data: str) -> int:
    number = 0
    while not hash_starts_with(number, data, '00000'):
        number += 1
    return number


def part2(data: str) -> int:
    number = 0
    while not hash_starts_with(number, data, '000000'):
        number += 1
    return number


def main():
    data = 'ckczppom'
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == "__main__":
    main()
