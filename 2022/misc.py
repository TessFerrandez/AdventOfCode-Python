import parse
from dataclasses import dataclass
from colorama import Cursor
import numpy as np


# parsing
pattern = parse.compile("turn off {a:d},{b:d} through {c:d},{d:d}")
match = pattern.search('turn off 660,55 through 986,197')
# print(match.named)


# using data classes
@dataclass
class StateMachine:
    memory: dict[str, int]
    program: list[str]

    def run(self):
        current_line = 0
        while current_line < len(self.program):
            instruction = self.program[current_line]

            if instruction.startswith('set '):
                register, value = instruction[4], int(instruction[6:])
                self.memory[register] = value
            elif instruction.startswith('inc '):
                register = instruction[4]
                self.memory[register] += 1
            current_line += 1


state_machine = StateMachine(memory={"g": 0}, program=["set g 45", "inc g"])
state_machine.run()
# print(state_machine.memory)


# pretty print with colorama
grid = np.array([
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 2, 1],
    [1, 1, 1, 1, 1],
])

rows, cols = grid.shape
for row in range(rows):
    for col in range(cols):
        symbol = " *o"[grid[row, col]]
        print(f"{Cursor.POS(col + 1, row + 2)}{symbol}")
