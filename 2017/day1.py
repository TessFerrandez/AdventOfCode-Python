import pytest


@pytest.mark.parametrize('data, expected',
                         [
                             ('1122', 3),
                             ('1111', 4),
                             ('1234', 0),
                             ('91212129', 9),
                         ])
def test_part1(data: str, expected: int):
    assert part1(data) == expected


@pytest.mark.parametrize('data, expected',
                         [
                             ('1212', 6),
                             ('1221', 0),
                             ('123425', 4),
                             ('123123', 12),
                             ('12131415', 4),
                         ])
def test_part2(data: str, expected: int):
    assert part2(data) == expected


def parse_input(filename: str) -> str:
    return open(filename).read().strip()


def part1(data: str) -> int:
    captcha = 0
    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            captcha += int(data[i])
    if data[-1] == data[0]:
        captcha += int(data[0])
    return captcha


def part2(data: str) -> int:
    num_items = len(data)
    half = num_items // 2

    captcha = 0
    for i in range(len(data)):
        if data[i] == data[(i + half) % num_items]:
            captcha += int(data[i])
    return captcha


def main():
    data = parse_input('input/day1.txt')
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == "__main__":
    main()
