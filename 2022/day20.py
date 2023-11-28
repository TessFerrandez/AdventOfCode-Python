from collections import deque
from input_processing import read_data


def parse(data):
    return [int(line) for line in data.splitlines()]


def part1(numbers):
    # there are duplicate numbers in data, so need to diff them
    # by adding their indices
    numbers = list(enumerate(numbers))
    circle = deque(numbers)

    for num in numbers:
        idx = circle.index(num)
        circle.rotate(-idx)
        circle.popleft()
        circle.rotate(-num[1])
        circle.appendleft(num)

    num_zero = next(num_obj for num_obj in numbers if num_obj[1] == 0)
    idx_0 = circle.index(num_zero)
    circle_len = len(circle)
    return sum([circle[(idx_0 + offset) % circle_len][1] for offset in [1000, 2000, 3000]])


def part2(numbers):
    # there are duplicate numbers in data, so need to diff them
    # by adding their indices
    numbers = list(enumerate([number * 811589153 for number in numbers]))
    circle = deque(numbers[:])

    for _ in range(10):
        for num in numbers:
            idx = circle.index(num)
            circle.rotate(-idx)
            circle.popleft()
            circle.rotate(-num[1])
            circle.appendleft(num)

    num_zero = next(num_obj for num_obj in numbers if num_obj[1] == 0)
    idx_0 = circle.index(num_zero)
    circle_len = len(circle)
    return sum([circle[(idx_0 + offset) % circle_len][1] for offset in [1000, 2000, 3000]])


def test():
    sample = """1
2
-3
3
-2
0
4"""
    assert part1(parse(sample)) == 3
    assert part2(parse(sample)) == 1623178306


test()
data = parse(read_data(2022, 20))
print('Part1:', part1(data))
print('Part2:', part2(data))
