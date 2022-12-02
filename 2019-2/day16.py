from unicodedata import digit
from alive_progress import alive_bar


ORIGINAL_PATTERN = [0, 1, 0, -1]


def calculate_phase(signal):
    output_signal = ""
    signal = [int(d) for d in signal]
    signal_len = len(signal)

    for pos in range(1, signal_len + 1):
        pattern = [ORIGINAL_PATTERN[n] for n in range(4) for _ in range(pos)]
        patter_len = len(pattern)
        sum_pos = 0

        for i in range(signal_len):
            sum_pos += signal[i] * pattern[(i + 1) % patter_len]
        output_signal += str(abs(sum_pos) % 10)

    return output_signal


def part1(signal):
    with alive_bar(100) as bar:
        for _ in range(100):
            signal = calculate_phase(signal)
            bar()
    return signal


def part2(original_signal):
    signal = original_signal * 10000
    index = int(signal[:7])
    digits = signal[index:]

    output = ''

    with alive_bar(100) as bar:
        for _ in range(100):
            output = ''
            total, di = 0, 0

            while di < len(digits):
                # sum the last x digits (phase is largely 0...01...1)
                if di == 0:
                    total += sum(int(d) for d in digits)
                elif di > 0:
                    total -= int(digits[di - 1])
                output += str(total % 10)
                di += 1

            digits = output
            bar()

    return digits[:8]


original_signal = open('2019/input/day16.txt').read().strip()
print("Part 1:", part1(original_signal)[:8])
print("Part 2:", part2(original_signal))
