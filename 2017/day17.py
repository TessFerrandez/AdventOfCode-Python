from progressbar import ProgressBar


def print_circle(next_val, current):
    circle_len = len(next_val)
    base = 0
    circle_str = ''
    for _ in range(circle_len):
        if base == current:
            circle_str += '(' + str(base) + ') '
        else:
            circle_str += str(base) + ' '
        base = next_val[base]
    print(circle_str)


def spin(skip: int, num_items: int) -> dict:
    next_val = {0: 0}
    current = 0

    for i in range(num_items + 1):
        for j in range(skip):
            current = next_val[current]
        next_val[current], next_val[i] = i, next_val[current]
        current = next_val[current]
    return next_val


def part1(skip: int) -> int:
    circle = spin(skip, 2017)
    return circle[2017]


def spin_part2(skip: int, num_items: int) -> int:
    # nothing is ever inserted at pos 1
    # since we always add 1 to the modulo
    # so num after 0 is last item placed in pos 1
    at_pos_1 = 0

    current_pos = 0
    for step in range(1, num_items + 1):
        current_pos = (current_pos + skip) % step + 1
        if current_pos == 1:
            # print(step, at_pos_1)
            at_pos_1 = step

    return at_pos_1


def part2(skip: int) -> int:
    return spin_part2(skip, 50000000)


def main():
    puzzle_input = 345
    # puzzle_input = 3
    print(f'Part 1: {part1(puzzle_input)}')
    print(f'Part 2: {part2(puzzle_input)}')


if __name__ == "__main__":
    main()
