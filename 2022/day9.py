from input_processing import read_data


def parse(data):
    return data.splitlines()


def follow(tail, head):
    new_x, new_y = tail
    if abs(tail[0] - head[0]) == 2 or abs(tail[1] - head[1]) == 2:
        diff_x, diff_y = head[0] - tail[0], head[1] - tail[1]
        if diff_x != 0:
            new_x = tail[0] + diff_x // abs(diff_x)
        if diff_y != 0:
            new_y = tail[1] + diff_y // abs(diff_y)
    return new_x, new_y


def move(pos, direction):
    steps = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    return pos[0] + steps[direction][0], pos[1] + steps[direction][1]


def part1(instructions):
    visited = set([(0, 0)])
    head = (0, 0)
    tail = (0, 0)

    for instruction in instructions:
        direction, steps = instruction.split()
        steps = int(steps)
        for _ in range(steps):
            head = move(head, direction)
            tail = follow(tail, head)
            visited.add(tail)

    return len(visited)


def part2(instructions):
    visited = set([(0, 0)])
    rope = [(0, 0) for _ in range(10)]

    for instruction in instructions:
        direction, steps = instruction.split()
        steps = int(steps)
        for _ in range(steps):
            rope[0] = move(rope[0], direction)
            for i in range(1, 10):
                rope[i] = follow(rope[i], rope[i - 1])
            visited.add(rope[-1])

    return len(visited)


def test():
    sample = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

    sample2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
    assert part1(parse(sample)) == 13
    assert part2(parse(sample)) == 1
    assert part2(parse(sample2)) == 36


test()
instructions = parse(read_data(2022, 9))
print('Part1:', part1(instructions))
print('Part2:', part2(instructions))
