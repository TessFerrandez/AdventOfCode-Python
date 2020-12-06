import pytest
import time


@pytest.mark.parametrize('data, expected',
                         [
                             ('1', '11'),
                             ('11', '21'),
                             ('21', '1211'),
                             ('1211', '111221'),
                             ('111221', '312211'),
                         ])
def test_look_and_say(data: str, expected: str):
    assert look_and_say(data) == expected


def look_and_say(digits: str) -> str:
    current_digit = ''
    current_streak = 0
    result = []

    for digit in digits:
        current_streak += 1
        if current_digit != digit:
            if current_digit != '':
                result.append(str(current_streak))
                result.append(current_digit)
            current_streak = 0
        current_digit = digit
    result.append(str(current_streak + 1))
    result.append(current_digit)
    return ''.join(result)


def part1(input_digits: str) -> int:
    start_time = time.perf_counter()
    digits = input_digits
    for i in range(40):
        digits = look_and_say(digits)
    print(time.perf_counter() - start_time, "seconds")
    return len(digits)


def part2(input_digits: str) -> int:
    start_time = time.perf_counter()
    digits = input_digits
    for i in range(50):
        digits = look_and_say(digits)
    print(time.perf_counter() - start_time, "seconds")
    return len(digits)


def main():
    input_digits = '1113122113'
    print(f'Part 1: {part1(input_digits)}')
    print(f'Part 2: {part2(input_digits)}')


if __name__ == "__main__":
    main()
