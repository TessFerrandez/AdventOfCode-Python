from collections import defaultdict
from input_processing import read_data
from functools import cache


def parse(data):
    return data.split(',')


@cache
def get_hash(step):
    result = 0

    for char in step:
        result += ord(char)
        result *= 17
        result %= 256

    return result


def part1(steps):
    total = 0

    for step in steps:
        hash = get_hash(step)
        total += hash

    return total


def part2(steps):
    boxes = defaultdict(dict)

    for step in steps:
        if '-' in step:
            label = step.split('-')[0]
            op = "del"
            val = 0
        else:
            label, val = step.split('=')
            op = "set"

        box = get_hash(label)

        if op == "set":
            boxes[box][label] = int(val)
        else:
            if label in boxes[box]:
                del boxes[box][label]

    total = 0
    for box in boxes:
        if len(boxes[box]) != 0:
            for i, label in enumerate(boxes[box]):
                label_value = (box + 1) * (i + 1) * boxes[box][label]
                total += label_value

    return total


def test():
    sample = '''rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'''
    steps = parse(sample)
    assert part1(steps) == 1320
    assert part2(steps) == 145


test()
data = read_data(2023, 15)
steps = parse(data)
print('Part1:', part1(steps))
print('Part2:', part2(steps))
