import pytest


def react(polymer: str) -> str:
    # 'a' 97 - 'A' 65 = 32
    lower = 'abcdefghijklmnopqrstuvwxyz'
    higher = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    changed = True
    while changed:
        changed = False
        original = polymer
        for i in range(len(lower)):
            polymer = polymer.replace(lower[i] + higher[i], '')
            polymer = polymer.replace(higher[i] + lower[i], '')
        if original != polymer:
            changed = True
    return polymer


@pytest.mark.parametrize('data, expected',
                         [
                             ('aA', ''),
                             ('abBA', ''),
                             ('abAB', 'abAB'),
                             ('aabAAB', 'aabAAB'),
                             ('dabAcCaCBAcCcaDA', 'dabCBAcaDA'),
                         ])
def test_react(data: str, expected: str):
    assert react(data) == expected


def react2(polymer: str) -> int:
    lower = 'abcdefghijklmnopqrstuvwxyz'
    higher = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    min_len = float('inf')
    for i in range(len(lower)):
        p_copy = polymer
        p_copy = p_copy.replace(lower[i], '').replace(higher[i], '')
        reacted = react(p_copy)
        if len(reacted) < min_len:
            min_len = len(reacted)
    return min_len


@pytest.mark.parametrize('data, expected',
                         [
                             ('dabAcCaCBAcCcaDA', 4),
                         ])
def test_react2(data: str, expected: int):
    assert react2(data) == expected


def parse_input(filename: str):
    return open(filename).read().strip()


def part1(polymer: str) -> int:
    return len(react(polymer))


def part2(polymer: str) -> int:
    return react2(polymer)


def main():
    polymer = parse_input('input/day5.txt')
    print(f'Part 1: {part1(polymer)}')
    print(f'Part 2: {part2(polymer)}')


if __name__ == "__main__":
    main()
