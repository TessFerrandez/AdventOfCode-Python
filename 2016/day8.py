from typing import List
import numpy as np


DEBUG = False


class Display:
    def __init__(self, instructions: List[List[str]], width: int, height: int):
        self.instructions = instructions
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width))

    def run(self):
        for instruction in self.instructions:
            if instruction[0] == 'rect':
                w, h = (int(val) for val in instruction[1].split('x'))
                self.grid[0:h, 0:w] = 1
            elif instruction[1] == 'column':
                x = int(instruction[2].split('=')[1])
                by = int(instruction[4])
                column = self.grid[:, x]
                rotated_column = list(column[-by:]) + list(column[:-by])
                self.grid[:, x] = rotated_column
            elif instruction[1] == 'row':
                y = int(instruction[2].split('=')[1])
                by = int(instruction[4])
                row = self.grid[y, :]
                rotated_row = list(row[-by:]) + list(row[:-by])
                self.grid[y, :] = rotated_row
            if DEBUG:
                self.draw()

    def draw(self):
        print('_' * self.width)
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == 0:
                    print('.', end='')
                else:
                    print('#', end='')
            print('')

    def count_lit(self):
        return int(np.sum(self.grid))


def parse_input(filename: str) -> List[List[str]]:
    return [line.strip().split() for line in open(filename).readlines()]


def part1(instructions: List[List[str]], width: int, height: int) -> int:
    display = Display(instructions, width, height)
    display.run()
    return display.count_lit()


def part2(instructions: List[List[str]], width: int, height: int) -> int:
    display = Display(instructions, width, height)
    display.run()
    display.draw()


def main():
    instructions = parse_input('input/day8.txt')
    print(f'Part 1: {part1(instructions, 50, 6)}')
    print('Part 2:')
    part2(instructions, 50, 6)


if __name__ == "__main__":
    main()
