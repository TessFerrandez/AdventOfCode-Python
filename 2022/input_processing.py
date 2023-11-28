import re


def read_data(year, day):
    return open(f"{year}\\input\\day{day}.in").read().strip()


def read_data_no_strip(year, day):
    return open(f"{year}\\input\\day{day}.in").read()


def read_sample_data(year, day):
    return open(f"{year}\\input\\day{day}-sample.in").read().strip()


def lines_as_num_array(data):
    return [int(line) for line in data.split()]


def get_numbers_from_lines(data):
    return [[int(d) for d in re.findall(r'-?\d+', line)] for line in data.splitlines()]


# groups separated by empty lines
def get_groups(data):
    return [group for group in data.split('\n\n')]
