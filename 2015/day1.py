import pytest


@pytest.mark.parametrize('data, expected',
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
def test_part1(data: str, expected: int):
    assert part1(data) == expected


@pytest.mark.parametrize('data, expected',
                         [
                             (')', 1),
                             ('()())', 5),
                         ])
def test_part2(data: str, expected: int):
    assert part2(data) == expected


def parse_input(filename: str) -> str:
    return open(filename).read().strip()


def part1(directions: str) -> int:
    return directions.count('(') - directions.count(')')


def part2(directions: str) -> int:
    floor = 0
    for i, ch in enumerate(directions):
        floor += 1 if ch == '(' else -1
        if floor == -1:
            return i + 1
    return -1


def main():
    directions = parse_input('input/day1.txt')
    print(f'Part 1: {part2(directions)}')
    print(f'Part 2: {part2(directions)}')


if __name__ == "__main__":
    main()
