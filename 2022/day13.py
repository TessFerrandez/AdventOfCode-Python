import json
from functools import cmp_to_key
from input_processing import read_data


def compare(left_list, right_list):
    i = 0
    len_left, len_right = len(left_list), len(right_list)

    while i < len_left and i < len_right:
        left, right = left_list[i], right_list[i]
        i += 1

        if isinstance(left, int) and isinstance(right, int):
            if left == right:
                continue
            return 1 if left > right else -1

        left = [left] if isinstance(left, int) else left
        right = [right] if isinstance(right, int) else right

        result = compare(left, right)
        if result == 0:
            continue
        return result

    return 1 if len_left > len_right else 0 if len_left == len_right else -1


def parse(data):
    pairs = [[json.loads(string) for string in pair.splitlines()] for pair in data.split('\n\n')]
    return pairs


def parse_packets(data):
    lists = [json.loads(string) for string in data.splitlines() if string != '']
    return lists


def part1(pairs):
    sum_indices = 0
    for i, pair in enumerate(pairs):
        left, right = pair
        if compare(left, right) < 1:
            sum_indices += i + 1

    return sum_indices


def part2(packets):
    packets.append([[2]])
    packets.append([[6]])

    packets.sort(key=cmp_to_key(compare))
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


def test():
    sample = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""
    pairs = parse(sample)
    assert part1(pairs) == 13
    packets = parse_packets(sample)
    assert part2(packets) == 140


test()
pairs = parse(read_data(2022, 13))
print('Part1:', part1(pairs))
packets = parse_packets(read_data(2022, 13))
print('Part2:', part2(packets))
