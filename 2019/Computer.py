from typing import List
from collections import deque

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


class Computer:
    def __init__(self, code: List[int]):
        self.code = code + [0] * 1000
        self.ip = 0
        self.relative = 0
        self.max_ip = len(code)
        self.inputs = deque()
        self.outputs = deque()
        self.done = False

    def run(self):
        while True:
            op = self.code[self.ip]
            op, modes = self.decode_op(op)
            params = self.code[self.ip + 1: self.ip + 5]

            if op == ADD:
                p1 = self.get(modes[0], params[0])
                p2 = self.get(modes[1], params[1])
                out = params[2] if modes[2] != RELATIVE else self.relative + params[2]
                self.code[out] = p1 + p2
                self.ip += 4
            if op == MUL:
                p1 = self.get(modes[0], params[0])
                p2 = self.get(modes[1], params[1])
                out = params[2] if modes[2] != RELATIVE else self.relative + params[2]
                self.code[out] = p1 * p2
                self.ip += 4
            if op == INPUT:
                out = params[0] if modes[0] != RELATIVE else self.relative + params[0]
                try:
                    self.code[out] = self.inputs.popleft()
                except IndexError:
                    raise InputInterrupt
                else:
                    self.ip += 2
            if op == OUTPUT:
                p1 = self.get(modes[0], params[0])
                self.outputs.append(p1)
                self.ip += 2
                raise OutputInterrupt
            if op == JUMP_IF_TRUE:
                p1 = self.get(modes[0], params[0])
                p2 = self.get(modes[1], params[1])
                if p1:
                    self.ip = p2
                else:
                    self.ip += 3
            if op == JUMP_IF_FALSE:
                p1 = self.get(modes[0], params[0])
                p2 = self.get(modes[1], params[1])
                if not p1:
                    self.ip = p2
                else:
                    self.ip += 3
            if op == LESS_THAN:
                p1 = self.get(modes[0], params[0])
                p2 = self.get(modes[1], params[1])
                out = params[2] if modes[2] != RELATIVE else self.relative + params[2]
                self.code[out] = 1 if p1 < p2 else 0
                self.ip += 4
            if op == EQUALS:
                p1 = self.get(modes[0], params[0])
                p2 = self.get(modes[1], params[1])
                out = params[2] if modes[2] != RELATIVE else self.relative + params[2]
                self.code[out] = 1 if p1 == p2 else 0
                self.ip += 4
            if op == RELATIVE_BASE:
                p1 = self.get(modes[0], params[0])
                self.relative += p1
                self.ip += 2
            if op == HALT:
                self.done = True
                return

    @staticmethod
    def decode_op(op: int) -> (int, List[int]):
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
            return self.code[param]
        if mode == RELATIVE:
            return self.code[self.relative + param]
        assert False
