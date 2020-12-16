import pytest


@pytest.mark.parametrize('input_str, expected',
                         [
                             ('ADVENT', 'ADVENT'),
                             ('A(1x5)BC', 'ABBBBBC'),
                             ('(3x3)XYZ', 'XYZXYZXYZ'),
                             ('A(2x2)BCD(2x2)EFG', 'ABCBCDEFEFG'),
                             ('(6x1)(1x3)A', '(1x3)A'),
                             ('X(8x2)(3x3)ABCY', 'X(3x3)ABC(3x3)ABCY')
                         ])
def test_decompress(input_str: str, expected: str):
    assert decompress(input_str) == expected


@pytest.mark.parametrize('input_str, expected',
                         [
                             ('(3x3)XYZ', 9),
                             ('X(8x2)(3x3)ABCY', 20),
                             ('(27x12)(20x12)(13x14)(7x10)(1x12)A', 241920),
                             ('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', 445),
                         ])
def test_decompress_count(input_str: str, expected: int):
    assert decompress_count(input_str) == expected


def decompress(input_str: str) -> str:
    try:
        marker_start = input_str.index('(')
        marker_end = input_str.index(')')
        before = input_str[:marker_start]
        marker = input_str[marker_start + 1: marker_end]
        after = input_str[marker_end + 1:]

        n_values, n_times = [int(val) for val in marker.split('x')]

        decompressed = before + after[:n_values] * n_times + decompress(after[n_values:])
    except ValueError:
        decompressed = input_str
    return decompressed


def decompress_count(input_str: str) -> int:
    try:
        marker_start = input_str.index('(')
        marker_end = input_str.index(')')
        before = input_str[:marker_start]
        marker = input_str[marker_start + 1: marker_end]
        after = input_str[marker_end + 1:]

        n_values, n_times = [int(val) for val in marker.split('x')]

        decompressed_count = len(before) + decompress_count(after[:n_values]) * n_times + decompress_count(after[n_values:])
    except ValueError:
        decompressed_count = len(input_str)
    return decompressed_count


def parse_input(filename: str):
    return open(filename).read().strip()


def part1(data: str) -> int:
    return len(decompress(data))


def part2(data: str) -> int:
    return decompress_count(data)


def main():
    data = parse_input('input/day9.txt')
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == "__main__":
    main()
