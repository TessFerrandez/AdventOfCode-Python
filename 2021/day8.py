from collections import Counter, defaultdict


entries = [[[pattern for pattern in part.split(' ')] for part in line.strip().split(' | ')] for line in open('2021//input//day8.txt').readlines()]
number_of = {'ABCEFG': '0', 'CF': '1', 'ACDEG': '2', 'ACDFG': '3', 'BCDF': '4', 'ABDFG': '5', 'ABDEFG': '6', 'ACF': '7', 'ABCDEFG': '8', 'ABCDFG': '9'}


def get_segment_map(patterns) -> dict:
    """
    Translate the segments based on the frequency of the segments
    """
    map = {}
    freq_chars = {6: 'B', 4: 'E', 9: 'F'}
    frequencies = Counter(''.join(patterns))

    one = [pattern for pattern in patterns if len(pattern) == 2][0]
    four = [pattern for pattern in patterns if len(pattern) == 4][0]

    for char, frequency in frequencies.items():
        if frequency == 8:
            map[char] = 'C' if char in one else 'A'
        elif frequency == 7:
            map[char] = 'D' if char in four else 'G'
        else:
            map[char] = freq_chars[frequency]

    return map


def decode(entry):
    patterns, output = entry

    segment_map = get_segment_map(patterns)

    result = ''
    for number in output:
        decoded = ''.join(sorted(segment_map[char] for char in number))
        result += number_of[decoded]

    return(int(result))


def part1():
    return sum(sum(1 for pattern in entry[1] if len(pattern) <= 4 or len(pattern) == 7) for entry in entries)


print("part 1:", part1())
print("part 2:", sum(decode(entry) for entry in entries))
