from IntCode import IntCode, OutputInterrupt, InputInterrupt


class Day13:
    def __init__(self, start_color=0):
        self.cpu = IntCode(open('input/day13.txt').readline())
        self.screen = [['.' for col in range(1000)] for row in range(1000)]
        self.instruction_index = 0
        self.instruction = []
        self.tiles = {0: '.', 1: 'X', 2: '#', 3: '_', 4: 'o'}
        self.max_row = 0
        self.max_col = 0

    def get_input(self):
        return 0

    def handle_output(self, output_val):
        self.instruction.append(output_val)
        if len(self.instruction) == 3:
            self.screen[self.instruction[1]][self.instruction[0]] = self.tiles[self.instruction[2]]
            self.max_col = max(self.max_col, self.instruction[0])
            self.max_row = max(self.max_row, self.instruction[1])
            self.instruction.clear()

    def run(self):
        while not self.cpu.done:
            try:
                self.cpu.run()
            except InputInterrupt:
                self.cpu.input_queue.append(self.get_input())
            except OutputInterrupt:
                self.handle_output(self.cpu.output_queue[-1])

    def display(self):
        for row in range(self.max_row + 1):
            print(*self.screen[row][0:self.max_col + 1], sep='')

    def count_blocks(self):
        blocks = 0
        for row in range(self.max_row + 1):
            for col in range(self.max_col + 1):
                if self.screen[row][col] == '#':
                    blocks += 1

        print("blocks:", blocks)


if __name__ == "__main__":
    puzzle = Day13(0)
    puzzle.run()
    puzzle.display()
    puzzle.count_blocks()
