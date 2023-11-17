from input_processing import read_data


def parse(data):
    return data.splitlines()


def calculate_values(instructions):
    values = [1]
    for instruction in instructions:
        if instruction == "noop":
            values.append(values[-1])
        elif instruction.startswith("addx"):
            values.append(values[-1])
            values.append(values[-1] + int(instruction.split()[1]))
    return values


def part1(instructions):
    values = calculate_values(instructions)

    total = 0
    for i in range(19, len(values), 40):
        total += values[i] * (i + 1)

    return total


def part2(instructions):
    values = calculate_values(instructions)
    rows = len(values) // 40
    for row in range(rows):
        for i in range(40):
            val = values[row * 40 + i]
            if val - 1 <= i <= val + 1:
                print("#", end="")
            else:
                print(".", end="")
        print()


def test():
    sample = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""
    instructions = sample.splitlines()
    assert part1(instructions) == 13140


test()
instructions = parse(read_data(2022, 10))
print('Part1:', part1(instructions))
print('Part2:', part2(instructions))
