from typing import List
from progressbar import ProgressBar


def parse_input(filename: str) -> str:
    return open(filename).read().strip()


def get_pattern(i: int) -> List[int]:
    base_pattern = [0, 1, 0, -1]
    return [digit for digit in base_pattern for _ in range(i)]


def get_number(input_signal: List[int], pattern: List[int]) -> int:
    digit_sum = sum(input_signal[index] * pattern[(index + 1) % len(pattern)] for index in range(len(input_signal)))
    number = abs(digit_sum) % 10
    return number


def iterate(input_signal: List[int]):
    result = []
    for i in range(1, len(input_signal) + 1):
        pattern = get_pattern(i)
        number = get_number(input_signal, pattern)
        result.append(number)
    return result


def part1(input_signal: str) -> str:
    input_signal = [int(digit) for digit in input_signal]
    with ProgressBar(max_value=100) as p:
        for phase in range(100):
            input_signal = iterate(input_signal)
            p.update(phase)
    return ''.join(str(digit) for digit in input_signal[:8])


def part2(input_signal: str) -> str:
    """ Poem by DFreiberg
    From the last digit first, do a cumsum reversed,
    then reverse it all back and add 1 to the stack,
    and make sure your offset hasn't drifted as yet
    and then do it again till the Mod[]s hurt your brain
    and go back and unplug when your-off-by-one bug
    wrecks your program until you've just lost all the thrill
    and you've fallen behind with about half a mind
    to just quit and go drowning your sorrow,

    But the program is done, and the second star's won!
    And the poem's complete, and the challenge is beat

    ...right until we get Intcode tomorrow!
    """
    input_signal = input_signal * 10000
    digits = (input_signal[int(input_signal[: 7]):])
    with ProgressBar(max_value=100) as p:
        for phase in range(100):
            string = ''
            total = 0
            digit_index = 0
            while digit_index < len(digits):
                # sum up the last x digits (the phase will be largely 0.......01.......1)
                if digit_index == 0:
                    total = 0
                    for digit in digits:
                        total += int(digit)
                elif digit_index > 0:
                    total -= int(digits[digit_index - 1])
                # get the last digit in the sum
                string += str(total)[-1]
                digit_index += 1
            digits = string
            p.update(phase)
    return digits[:8]


def main():
    data = parse_input('input/day16.txt')
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == "__main__":
    main()
