from typing import List
import pytest


def is_valid_passphrase(passphrase: str) -> bool:
    words = passphrase.split(' ')
    unique_words = set(words)
    return len(words) == len(unique_words)


@pytest.mark.parametrize('passphrase, expected',
                         [
                             ('aa bb cc dd ee', True),
                             ('aa bb cc dd aa', False),
                             ('aa bb cc dd aaa', True),
                         ])
def test_is_valid_passphrase(passphrase: str, expected: bool):
    assert is_valid_passphrase(passphrase) == expected


def is_valid_passphrase2(passphrase: str) -> bool:
    words = [''.join(sorted(word)) for word in passphrase.split(' ')]
    unique_words = set(words)
    return len(words) == len(unique_words)


@pytest.mark.parametrize('passphrase, expected',
                         [
                             ('abcde fghij', True),
                             ('abcde xyz ecdab', False),
                             ('a ab abc abd abf abj', True),
                             ('iiii oiii ooii oooi oooo', True),
                             ('oiii ioii iioi iiio', False),
                         ])
def test_is_valid_passphrase2(passphrase: str, expected: bool):
    assert is_valid_passphrase2(passphrase) == expected


def parse_input(filename: str) -> List[str]:
    return [line.strip() for line in open(filename)]


def part1(passphrases: List[str]) -> int:
    return sum(1 for passphrase in passphrases if is_valid_passphrase(passphrase))


def part2(passphrases: List[str]) -> int:
    return sum(1 for passphrase in passphrases if is_valid_passphrase2(passphrase))


def main():
    passphrases = parse_input('input/day4.txt')
    print(f'Part 1: {part1(passphrases)}')
    print(f'Part 2: {part2(passphrases)}')


if __name__ == "__main__":
    main()
