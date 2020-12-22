def generate_dragon_curve(input_str: str, size: int) -> str:
    a = input_str
    while len(a) < size:
        b = a[::-1]
        b = b.replace('0', 'x').replace('1', '0').replace('x', '1')
        a += '0' + b
    return a[:size]


def generate_checksum(string: str) -> str:
    checksum = ''
    while len(checksum) % 2 == 0:
        checksum = ''
        for i in range(0, len(string) - 1, 2):
            if string[i: i + 2] in ['00', '11']:
                checksum += '1'
            else:
                checksum += '0'
        string = checksum
    return checksum


def part1(puzzle_input: str, disk_size: int) -> str:
    string = generate_dragon_curve(puzzle_input, disk_size)
    checksum = generate_checksum(string)
    return checksum


def main():
    puzzle_input = '10111100110001111'
    print(f'Part 1: {part1(puzzle_input, 272)}')
    print(f'Part 2: {part1(puzzle_input, 35651584)}')


if __name__ == "__main__":
    main()
