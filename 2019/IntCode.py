"""
Int Code compiler -- based on https://topaz.github.io/paste/#XQAAAQBSFgAAAAAAAAARlMqGE8hv2NWPEewoYCd8oCytNCXbmEuStcmaV5YpDTQ8o8Y+QA7LSjLAFBimIxewZyBLni9af/VT2DTKIxw8icvCRsNsaOQdnopvXGHOQBRQ8JdP3+E22eIRv6ePbfcr2376qH+p4zlQr145ZWnGVzISXpfnu3V9xR3Tox0Ae2AhhG18ouFOSu3sBtDPZ+YAom8e1QCoyn1OeWH1x5sDzsTDTgx0fVuX6DNohMrSa41/WIOIW1e/qT5bnhbqRKAzBke/MDf6ACanF7lzHh0BVbOS8DKT7p57Vhql4HmKxI/VAp1490ZoDLDCoN817YvhnwEDIorgWt7+207bGo1ZZExdwCnUYwLSMe8AXNidLXdSoA5t1ydpGIC3hT299vBrfYcz6owrwQkxKL3vkEjWr36cLhCvXyL98qoYpHoaAAHDSZ2BoK96+2biFXMXUR0aoIDEzqzwuI5gOBbXkqdy1SW+kQ9zybNkHe8BWC9tYGL1yQBBr0CnZriZzqd/Jj7c8DhkENNqpcR3wcnRxrlpiIyu+8/uZvL4/tCFR9j8nllZPaoT65kP9z/AcA5s2E2lQGy86Wld0HfaBKldMYdGydH8xp2wNS+xFhayf7xUyVuoS4C61D6G8Ea2dClHe5ycs/qO5z7RreyakWxwNYMHg/Kvw0STwDba35+fhlvaMTd48Tmi2Fl9SLG66hHcjxJ6m5Vqqy3h9HXVQUwfSFGEeE2kn+zQnGv6JPDtV2Uz9HpxRdbIurE38HAYAAAl1ohjIBjAtC8AVj66/+eMpx1jCwL0g4l/a1LRIF0LQz2zQ8n0DbK2ad9a7/suEWgdZTC2BWDeTLewOl9pF4xZiSLyyIpDKs/H2I+5oK8WGhsbqRvfk661G/hcCdT7VaIALD5fbfUkKx6O43IDFh7zjPLZiTf0Aq4+MDsT2DnlrcO7sJdxlkFgq5tWTYvoiRXNFWzodCfbkIKx2URB0vN/tmRjTC+mSqQluRQ/pHez0A/EcstL+fGA+UjF8SuyfbNiB03x1iiPfOLMI8kpskV6lSbNbSPSRJpFEfqNcQFQvsCAnewM+UDYGoXTIQ6TzxNmyzYAwfAo17W1iz8ZCmpIgBsWJIlj5cVKT+RfeLoEpEnHf6xGo4s5xuE86HkPlExAOtR+xUqpd2xf3hGmrdljHi9+3wgp6C6l4IUcpukcJlOox2xycXfFHEOAGzYyEio2PYHruqo3tsNKQJwpokoSRUndWYJ/+mzPsycdlKCC6vKplgOsQVdngj1hriFxQGo/eo/pICcMdVTSYEW+sBtyJxZx62km+EJRL7CUeY7HFiskGNB5FUhD48HQeN9zHVsWUnXC5u5gBFD7WW56Vkj8xxQ+an0QiQJuNAt/Eu0A7yKUMlwIakfEP0RnJgzwbjiZfcfm4SOXjXKjy9iU7k9hzSp5soItePYWzMGYh0qZmOYmJb8nVnFafJ2KdTokD/Fg3dJF3hh+lWnt3YWHJuodh92UgWP/5s3xb7mMxUP+sylIKUQiwPg/zgRFjv8hO6LgdTg7LcDJ1T8y/I0FPGdYWb+4zXihXMa5TMLFRsbtc9Ej/ZctR15isLvQrdrVDETdY37xXQlvJav4T+teoeHrtcWPuLwts909eSg+dEokXwGXyppEiWK2nPkdxeqpuQap9NthLzI6thGtV3GPQ0AEwy9dTEdey9ndnKzw660sHTOOARGtqIc977Clc5c/d4VPgV0USHYeLPwHLtyFLpAxSYtcXU8VbplpPfR7MXI1OfpJc4UjimqNpqhYgqEcFHWomyqPOA44Qq+/ej0XvvVp8/WH/7jGXOs=
"""
from collections import deque


class Instruction:
    def __init__(self, op_count, func):
        self.op_count = op_count
        self.func = func


class State:
    def __init__(self, memory, instruction_ptr):
        self.memory = memory
        self.instruction_ptr = instruction_ptr


class InputInterrupt(Exception):
    pass


class OutputInterrupt(Exception):
    pass


class IntCode:
    def __init__(self, program):
        self.instruction_list = {
            1: self.add_func,
            2: self.multi_func,
            3: self.input_func,
            4: self.output_func,
            5: self.jmp_true_func,
            6: self.jmp_false_func,
            7: self.lt_func,
            8: self.eq_func,
        }

        self.program_string = program
        self.memory = IntCode.parse(self.program_string)
        self.instruction_ptr = 0
        self.done = False
        self.input_queue = deque()
        self.output_queue = deque()

    def mode_get(self, mode, operand):
        if mode:
            return operand
        else:
            return self.memory[operand]

    def add_func(self, modes, operands):
        a = self.mode_get(modes[0], operands[0])
        b = self.mode_get(modes[1], operands[1])
        self.memory[operands[2]] = a + b
        self.instruction_ptr += 4

    def multi_func(self, modes, operands):
        a = self.mode_get(modes[0], operands[0])
        b = self.mode_get(modes[1], operands[1])
        self.memory[operands[2]] = a * b
        self.instruction_ptr += 4

    def input_func(self, modes, operands):
        try:
            self.memory[operands[0]] = self.input_queue.popleft()
        except IndexError:
            raise InputInterrupt
        else:
            # only advance the instruction pointer if we have taken input
            self.instruction_ptr += 2

    def output_func(self, modes, operands):
        self.output_queue.append(self.mode_get(modes[0], operands[0]))
        self.instruction_ptr += 2
        raise OutputInterrupt

    def jmp_true_func(self, modes, operands):
        if self.mode_get(modes[0], operands[0]):
            self.instruction_ptr = self.mode_get(modes[1], operands[1])
        else:
            self.instruction_ptr += 3

    def jmp_false_func(self, modes, operands):
        if not self.mode_get(modes[0], operands[0]):
            self.instruction_ptr = self.mode_get(modes[1], operands[1])
        else:
            self.instruction_ptr += 3

    def lt_func(self, modes, operands):
        a = self.mode_get(modes[0], operands[0])
        b = self.mode_get(modes[1], operands[1])
        self.memory[operands[2]] = int(a < b)
        self.instruction_ptr += 4

    def eq_func(self, modes, operands):
        a = self.mode_get(modes[0], operands[0])
        b = self.mode_get(modes[1], operands[1])
        self.memory[operands[2]] = int(a == b)
        self.instruction_ptr += 4

    @staticmethod
    def instruction_parse(num, inputs):
        op_code = [num % 100]
        num //= 100
        for _ in range(inputs):
            op_code.append(num % 10)
            num //= 10
        return tuple(op_code)

    def run(self):
        while not self.done:
            curr = self.memory[self.instruction_ptr]
            if curr % 100 == 99:
                self.done = True
                break
            instruction = self.instruction_list[(curr % 100)]
            op_code = IntCode.instruction_parse(curr, 4)
            instruction(
                op_code[1:],
                self.memory[self.instruction_ptr + 1:self.instruction_ptr + 5]
            )

    @staticmethod
    def parse(program_string):
        return list(map(int, program_string.split(',')))
