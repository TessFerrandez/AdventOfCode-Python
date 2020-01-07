import numpy as np


def calculate_power(x: int, y: int, serial: int) -> int:
    rack_id = x + 10
    power = (rack_id * y + serial) * rack_id
    power = (power // 100) % 10 - 5
    return power


def calculate_max(grid: np.ndarray, size: int) -> (int, int, int):
    max_power = 0
    best_x, best_y = 0, 0
    for y in range(1, 301 - size):
        for x in range(1, 301 - size):
            power = np.sum(grid[y : y + size, x : x + size])
            if power > max_power:
                max_power = power
                best_x = x
                best_y = y

    return max_power, best_x, best_y


def puzzles():
    grid = np.zeros((301, 301))
    for y in range(1, 301):
        for x in range(1, 301):
            grid[y][x] = calculate_power(x, y, 5535)

    _, x, y = calculate_max(grid, 3)
    print("3x3:", x, y)

    max_power, max_size, max_x, max_y = 0, 0, 0, 0
    for i in range(1, 301):
        if i % 10 == 0:
            print(i)
        power, x, y = calculate_max(grid, i)
        if power > max_power:
            max_power = power
            max_size = i
            max_x = x
            max_y = y

    print("multi:", max_x, max_y, max_size)


if __name__ == "__main__":
    puzzles()
