from collections import defaultdict


def part1(number: int) -> int:
    position = 0
    direction = -1j
    for i in range(1, number):
        x, y = position.real, position.imag
        # turn at the corners
        if x == y or (x == -y and x < 0) or (x == 1 - y and x > 0):
            direction *= 1j

        # move forward
        position += direction

    return abs(int(position.real)) + abs(int(position.imag))


def part2(number: int) -> int:
    neighbors = [-1, -1 + 1j, 1j, 1 + 1j, 1, 1 - 1j, -1j, -1 - 1j]
    values = defaultdict(int)

    position = 0
    values[0] = 1
    direction = -1j

    while True:
        x, y = position.real, position.imag
        # turn at the corners
        if x == y or (x == -y and x < 0) or (x == 1 - y and x > 0):
            direction *= 1j

        # move forward
        position += direction

        # calculate value based on neighbor positions
        pos_value = 0
        for neighbor in neighbors:
            pos_value += values[position + neighbor]
        if pos_value > number:
            return pos_value
        else:
            values[position] = pos_value


def main():
    puzzle_input = 368078
    print(f'Part 1: {part1(puzzle_input)}')
    print(f'Part 2: {part2(puzzle_input)}')


if __name__ == "__main__":
    main()
