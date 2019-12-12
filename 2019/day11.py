# based on topaz
import numpy as np
import matplotlib.pyplot as plt
from IntCode import IntCode, OutputInterrupt, InputInterrupt


class Day11:
    def __init__(self, start_color=0):
        self.cpu = IntCode(open('input/day11.txt').readline())
        self.position = (0, 0)
        self.direction = (0, 1)
        self.squares = {}
        self.squares_painted = 0
        self.paint = True
        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0
        self.start_color = start_color

    def get_input(self):
        return self.start_color if self.position not in self.squares else self.squares[self.position]

    def handle_output(self, output_val):
        if self.paint:
            # paint (output_val = color)
            if self.position not in self.squares:
                self.squares_painted += 1
                self.min_x = min(self.min_x, self.position[0])
                self.max_x = max(self.max_x, self.position[0])
                self.min_y = min(self.min_y, self.position[1])
                self.max_y = max(self.max_x, self.position[1])
            self.squares[self.position] = output_val
        else:
            if output_val == 0:
                # turn left
                x, y = self.direction
                self.direction = (-y, x)
            elif output_val == 1:
                # turn right
                x, y = self.direction
                self.direction = (y, -x)
            # move
            self.position = tuple(map(sum, zip(self.position, self.direction)))
            self.cpu.input_queue.append(self.get_input())

        self.paint = not self.paint

    def run(self):
        while not self.cpu.done:
            try:
                self.cpu.run()
            except InputInterrupt:
                self.cpu.input_queue.append(self.get_input())
            except OutputInterrupt:
                self.handle_output(self.cpu.output_queue[-1])

    def display(self):
        num_cols = self.max_x - self.min_x
        num_rows = self.max_y - self.min_y
        x_offset = 0 if self.min_x > 0 else -self.min_x
        y_offset = 0 if self.min_y > 0 else -self.min_y
        screen = np.zeros((num_cols + 1, num_rows + 1))
        for square in self.squares.keys():
            screen[square[0] + x_offset, square[1] + y_offset] = self.squares[square]
        plt.imshow(screen)
        plt.show()


if __name__ == "__main__":
    puzzle = Day11(0)
    puzzle.run()
    print("squares painted:", puzzle.squares_painted)
    puzzle = Day11(1)
    puzzle.run()
    puzzle.display()
