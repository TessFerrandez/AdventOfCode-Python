from input_processing import read_data
import numpy as np


EMPTY = 0
ROCK = 1
SETTLED = 2
FALLING = 3
FALLING_CURRENT = 4
CAVE_MOUTH = 5


class Caves:
    def __init__(self, data):
        rocks = self.get_rocks(data)
        min_x, max_x, max_y = self.get_bounds(rocks)

        width = max_x - min_x + 3
        height = max_y + 1
        self.map = np.zeros((height + 1, width + 1), dtype=int)
        self.x_offset = min_x - 1
        self.map[0, 500 - self.x_offset + 1] = CAVE_MOUTH

        for x, y in rocks:
            self.map[y, x - self.x_offset + 1] = ROCK

        self.mouth = (500 - self.x_offset + 1, 0)
        self.current_sand = self.mouth

    def extend_map(self):
        height, width = self.map.shape
        x_offset = height - self.mouth[0]
        new_map = np.zeros((height + 1, 2 * height + 1), dtype=int)
        new_map[height: height + 1, :] = ROCK
        new_map[0: height, x_offset: x_offset + width] = self.map
        self.mouth = (height, 0)
        self.current_sand = self.mouth
        self.x_offset = x_offset
        self.map = new_map

    @staticmethod
    def get_rocks(data):
        chains = [[[int(part) for part in pair.split(',')] for pair in line.split(' -> ')] for line in data.splitlines()]
        rocks = set()
        for chain in chains:
            for i in range(len(chain) - 1):
                x0, x1 = sorted([chain[i][0], chain[i + 1][0]])
                y0, y1 = sorted([chain[i][1], chain[i + 1][1]])
                for x in range(x0, x1 + 1):
                    for y in range(y0, y1 + 1):
                        rocks.add((x, y))
        return rocks

    @staticmethod
    def get_bounds(rocks):
        min_x = min(x for x, _ in rocks)
        max_x = max(x for x, _ in rocks)
        max_y = max(y for _, y in rocks)
        return min_x, max_x, max_y

    def print_map(self):
        for row in self.map:
            print(''.join(['.' if cell == EMPTY else '#' if cell == ROCK else 'o' if cell == SETTLED else '~' if cell == FALLING else '~' if cell == FALLING_CURRENT else '+' if cell == CAVE_MOUTH else '?' for cell in row]))

    def pour_sand(self):
        x, y = self.current_sand

        # if we reached the bottom, stop pouring
        if y == self.map.shape[0] - 1:
            self.map[y][x] = FALLING
            self.current_sand = None
        elif self.map[y + 1][x] in [EMPTY, FALLING]:
            self.map[y + 1][x] = FALLING_CURRENT
            self.map[y][x] = FALLING
            self.current_sand = [x, y + 1]
        elif self.map[y + 1][x - 1] in [EMPTY, FALLING]:
            self.map[y + 1][x - 1] = FALLING_CURRENT
            self.map[y][x] = FALLING
            self.current_sand = [x - 1, y + 1]
        elif self.map[y + 1][x + 1] in [EMPTY, FALLING]:
            self.map[y + 1][x + 1] = FALLING_CURRENT
            self.map[y][x] = FALLING
            self.current_sand = [x + 1, y + 1]
        else:
            # can't move down
            self.map[y][x] = SETTLED
            # if we settle at the mouth, stop pouring
            if (x, y) == self.mouth:
                self.current_sand = None
            else:
                self.current_sand = self.mouth

    def run_simulation(self):
        while self.current_sand:
            self.pour_sand()

    def get_settled(self):
        return sum(sum(1 for cell in row if cell == SETTLED) for row in self.map)


def part1(data):
    caves = Caves(data)
    caves.run_simulation()
    return caves.get_settled()


def part2(data):
    caves = Caves(data)
    caves.extend_map()
    caves.run_simulation()
    return caves.get_settled()


def test():
    sample = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
    assert part1(sample) == 24
    assert part2(sample) == 93


test()
data = read_data(2022, 14)
print('Part1:', part1(data))
print('Part2:', part2(data))
