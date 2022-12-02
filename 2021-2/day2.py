def part1(instructions) -> int:
    horizontal, vertical = 0, 0

    for instruction in instructions:
        direction, value = instruction.split(' ')
        if direction == 'forward':
            horizontal += int(value)
        elif direction == 'down':
            vertical += int(value)
        else:
            vertical -= int(value)

    return horizontal * vertical


def part2(instructions) -> int:
    horizontal, depth, aim = 0, 0, 0

    for instruction in instructions:
        direction, value = instruction.split(' ')
        value = int(value)

        if direction == 'forward':
            horizontal += value
            depth += aim * value
        elif direction == 'down':
            aim += value
        else:
            aim -= value

    return horizontal * depth


assert part1(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']) == 150
assert part2(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']) == 900

lines = [line.strip() for line in open('./2021/input/day2.txt').readlines()]
print("Part1:", part1(lines))
print("Part2:", part2(lines))
