import numpy as np
from progressbar import ProgressBar


def power_up(serial_number: int) -> np.array:
    grid = np.zeros((302, 302))
    for y in range(1, 301):
        for x in range(1, 301):
            rack_id = x + 10
            power = rack_id * y
            power += serial_number
            power *= rack_id
            power_string = str(power)
            if len(power_string) >= 3:
                power = int(power_string[-3])
            else:
                power = 0
            power -= 5
            grid[y][x] = power
    return grid


def find_best_powered_square(grid: np.array, size: int) -> (int, int, int):
    max_power = 0
    best_square = (0, 0)
    for y in range(1, 301 - size):
        for x in range(1, 301 - size):
            power = np.sum(grid[y: y + size, x: x + size])
            if power > max_power:
                max_power = power
                best_square = (x, y)
    return best_square[0], best_square[1], max_power


def part1(serial_number: int) -> str:
    grid = power_up(serial_number)
    x, y, _ = find_best_powered_square(grid, 3)
    return f'({x},{y})'


def part2(serial_number: int) -> str:
    grid = power_up(serial_number)
    max_power = 0
    best_x, best_y, best_size = 0, 0, 0

    with ProgressBar(max_value=300) as p:
        for size in range(1, 301):
            p.update(size)
            x, y, power = find_best_powered_square(grid, size)
            if power > max_power:
                max_power = power
                best_x, best_y, best_size = x, y, size

    return f'{best_x},{best_y},{best_size}'


def main():
    serial_number = 5535
    print(f'Part 1: {part1(serial_number)}')
    print(f'Part 2: {part2(serial_number)}')


if __name__ == "__main__":
    main()
