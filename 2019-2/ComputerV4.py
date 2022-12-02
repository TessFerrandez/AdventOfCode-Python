from collections import deque
from typing import Tuple, List


ADD = 1
MUL = 2
INPUT = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
RELATIVE_BASE = 9
HALT = 99

POSITION = 0
IMMEDIATE = 1
RELATIVE = 2


class InputInterrupt(Exception):
    pass


class OutputInterrupt(Exception):
    pass


class Computer():
    def __init__(self, code: str) -> None:
        self.memory = [int(d) for d in code.strip().split(',')]
        self.memory += [0 for _ in range(10000)]

        self.ip = 0
        self.relative = 0
        self.max_ip = len(self.memory)

        self.inputs = deque()
        self.outputs = deque()

        self.done = False

    def __str__(self) -> str:
        return ','.join(str(d) for d in self.memory)

    @staticmethod
    def decode_op(op: int) -> Tuple[int, List[int]]:
        # get op and modes
        mode3 = op // 10000
        op -= mode3 * 10000
        mode2 = op // 1000
        op -= mode2 * 1000
        mode1 = op // 100
        op -= mode1 * 100
        return op, [mode1, mode2, mode3]

    def get(self, mode, param) -> int:
        if mode == IMMEDIATE:
            return param
        if mode == POSITION:
            return self.memory[param]
        if mode == RELATIVE:
            return self.memory[self.relative + param]
        assert False

    def run(self):
        while True:
            opx = self.memory[self.ip]
            op, modes = self.decode_op(opx)
            params = self.memory[self.ip + 1: self.ip + 5]

            p2, out = 0, 0
            if op != HALT:
                p1 = self.get(modes[0], params[0])
            if op in [ADD, MUL, JUMP_IF_TRUE, JUMP_IF_FALSE, LESS_THAN, EQUALS]:
                p2 = self.get(modes[1], params[1])
                out = params[2] if modes[2] != RELATIVE else self.relative + params[2]
            if op == ADD:
                self.memory[out] = p1 + p2
                self.ip += 4
            if op == MUL:
                self.memory[out] = p1 * p2
                self.ip += 4
            if op == INPUT:
                out = params[0] if modes[0] != RELATIVE else self.relative + params[0]
                try:
                    self.memory[out] = self.inputs.popleft()
                except IndexError:
                    raise InputInterrupt
                else:
                    self.ip += 2
            if op == OUTPUT:
                self.outputs.append(p1)
                self.ip += 2
                raise OutputInterrupt
            if op == JUMP_IF_TRUE:
                self.ip = p2 if p1 != 0 else self.ip + 3
            if op == JUMP_IF_FALSE:
                self.ip = p2 if p1 == 0 else self.ip + 3
            if op == LESS_THAN:
                self.memory[out] = 1 if p1 < p2 else 0
                self.ip += 4
            if op == EQUALS:
                self.memory[out] = 1 if p1 == p2 else 0
                self.ip += 4
            if op == RELATIVE_BASE:
                self.relative += p1
                self.ip += 2
            if op == HALT:
                self.done = True
                return

        while self.ip < self.max_ip and self.memory[self.ip] != 99:
            op, args = self.get_instruction(self.ip)
            if op == 1:
                p1, p2, p3 = args
                self.memory[p3] = p1 + p2
                self.ip += 4
            elif op == 2:
                p1, p2, p3 = args
                self.memory[p3] = p1 * p2
                self.ip += 4
            elif op == 3:
                p1 = args[0]
                if not self.inputs:
                    raise InputInterrupt
                self.memory[p1] = self.inputs.popleft()
                self.ip += 2
            elif op == 4:
                p1 = args[0]
                self.outputs.append(p1)
                self.ip += 2
                raise OutputInterrupt
            elif op == 5:
                p1, p2 = args
                if p1 != 0:
                    self.ip = p2
                else:
                    self.ip += 3
            elif op == 6:
                p1, p2 = args
                if p1 == 0:
                    self.ip = p2
                else:
                    self.ip += 3
            elif op == 7:
                p1, p2, p3 = args
                self.memory[p3] = 1 if p1 < p2 else 0
                self.ip += 4
            elif op == 8:
                p1, p2, p3 = args
                self.memory[p3] = 1 if p1 == p2 else 0
                self.ip += 4
            elif op == 9:
                p1 = args[0]
                self.relative += p1
                self.ip += 2


def test_input_output() -> int:
    computer = Computer('3,0,4,0,99')
    computer.inputs.append(5)

    try:
        computer.run()
    except OutputInterrupt:
        return computer.outputs.pop()

    return -1


def test_initial_final(initial, final):
    computer = Computer(initial)
    try:
        computer.run()
    except OutputInterrupt:
        print(computer.outputs.pop())

    assert str(computer).startswith(final)


def test_relative() -> int:
    code = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'
    code = '1102,34915192,34915192,7,4,7,99,0'
    code = '104,1125899906842624,99'
    computer = Computer(code)
    done = False
    while not done:
        try:
            computer.run()
            done = True
        except OutputInterrupt:
            return computer.outputs.pop()

    return 0


def tests():
    assert test_input_output() == 5
    test_initial_final('1,0,0,0,99', '2,0,0,0,99')
    test_initial_final('2,3,0,3,99', '2,3,0,6,99')
    test_initial_final('1002,4,3,4,33', '1002,4,3,4,99')
    test_initial_final('1101,100,-1,4,0', '1101,100,-1,4,99')
    assert test_relative() == 1125899906842624


tests()
