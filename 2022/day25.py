from input_processing import read_data


def dec_to_snafu(decimal_number):
    snafu = ''

    symbols = '012=-'
    worth = [0, 1, 2, -2, -1]

    while decimal_number > 0:
        rest = decimal_number % 5
        snafu += symbols[rest]
        decimal_number = (decimal_number - worth[rest]) // 5

    return snafu[::-1]


def snafu_to_dec(snafu_number):
    snafu_number = list(snafu_number)
    pow = 0
    decimal_number = 0

    symbol_to_mul = {'0': 0, '1': 1, '2': 2, '=': -2, '-': -1}

    while snafu_number:
        ch = snafu_number.pop()
        decimal_number += symbol_to_mul[ch] * (5 ** pow)
        pow += 1

    return decimal_number


def parse(data):
    return data.splitlines()


def part1(snafu_numbers):
    decimal_sum = sum(snafu_to_dec(num) for num in snafu_numbers)
    return dec_to_snafu(decimal_sum)


def test():
    sample = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""
    assert dec_to_snafu(20) == '1-0'
    assert dec_to_snafu(2022) == '1=11-2'
    assert dec_to_snafu(12345) == '1-0---0'
    assert dec_to_snafu(314159265) == '1121-1110-1=0'
    assert snafu_to_dec('1121-1110-1=0') == 314159265
    data = parse(sample)
    assert part1(data) == '2=-1=0'


test()
data = read_data(2022, 25)
print('Part1:', part1(parse(data)))
