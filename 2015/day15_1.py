import pytest


@pytest.mark.parametrize('data, expected',
                         [
                             ('', 0),
                         ])
def test_part1(data: str, expected: int):
    assert part1(data) == expected


@pytest.mark.parametrize('data, expected',
                         [
                             ('', 0),
                         ])
def test_part2(data: str, expected: int):
    assert part2(data) == expected


def parse_input(filename: str):
    return ''


def part1(data: str) -> int:
    return 0


def part2(data: str) -> int:
    return 0


def main():
    data = parse_input('input/dayX.txt')
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == "__main__":
    main()
