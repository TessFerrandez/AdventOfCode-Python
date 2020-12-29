from typing import List


def parse_input(filename: str) -> List[int]:
    return [int(d) for d in open(filename).read().strip().split(',')]


def knot_hash(numbers: List[int], lengths: List[int]) -> List[int]:
    num_elements = len(numbers)

    current = 0
    skip = 0

    for length in lengths:
        sub_list = numbers[current: current + length]
        sl_length = len(sub_list)
        if sl_length < length:
            sub_list += numbers[:length - sl_length]
        sub_list.reverse()

        if sl_length < length:
            before = sub_list[-(length - sl_length):]
            after = sub_list[:sl_length]
            mid = numbers[length - sl_length: -sl_length]
        else:
            before = numbers[:current]
            after = numbers[current + length:]
            mid = sub_list
        numbers = before + mid + after
        current = (current + length + skip) % num_elements
        skip += 1
    return numbers


def part1(num_elements: int, lengths: List[int]) -> int:
    numbers = [i for i in range(num_elements)]
    numbers = knot_hash(numbers, lengths)
    return numbers[0] * numbers[1]


def part2(input_str: str) -> str:
    lengths = []
    for ch in input_str:
        lengths.append(ord(ch))
    lengths += [17, 31, 73, 47, 23]

    num_elements = 256
    numbers = [i for i in range(num_elements)]

    current = 0
    skip = 0

    for i in range(64):
        for length in lengths:
            sub_list = numbers[current: current + length]
            sl_length = len(sub_list)
            if sl_length < length:
                sub_list += numbers[:length - sl_length]
            sub_list.reverse()

            if sl_length < length:
                before = sub_list[-(length - sl_length):]
                after = sub_list[:sl_length]
                mid = numbers[length - sl_length: -sl_length]
            else:
                before = numbers[:current]
                after = numbers[current + length:]
                mid = sub_list
            numbers = before + mid + after
            current = (current + length + skip) % num_elements
            skip += 1

    dense_hash = []
    for i in range(16):
        hash_val = numbers.pop(0)
        for j in range(15):
            hash_val ^= numbers.pop(0)
        dense_hash.append(hash_val)

    hex_output = ''
    for digit in dense_hash:
        hex_output += str(hex(digit))[2:]
    return hex_output


def main():
    lengths = parse_input('input/day10.txt')
    print(f'Part 1: {part1(256, lengths)}')
    input_str = open('input/day10.txt').read().strip()
    print(f'Part 2: {part2(input_str)}')


if __name__ == "__main__":
    main()
