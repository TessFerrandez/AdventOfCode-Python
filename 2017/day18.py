from typing import List, Tuple
from collections import defaultdict


OK = 0
RECEIVING = 1
DONE = 2


class ReceiveException(Exception):
    pass


class SendException(Exception):
    pass


class Computer:
    def __init__(self, instructions: List[Tuple]):
        self.registers = defaultdict(int)
        self.instructions = instructions
        self.instr_ptr = 0
        self.max_ptr = len(self.instructions)
        self.sound = 0

    def get_value(self, param):
        if param in 'abcdefghijklmnopqrstuvw':
            return self.registers[param]
        else:
            return int(param)

    def run(self) -> int:
        while self.instr_ptr < self.max_ptr:
            op, p1, p2 = self.instructions[self.instr_ptr]
            if op == 'snd':
                self.instr_ptr += 1
                self.sound = self.get_value(p1)
            elif op == 'set':
                self.registers[p1] = self.get_value(p2)
                self.instr_ptr += 1
            elif op == 'add':
                self.registers[p1] += self.get_value(p2)
                self.instr_ptr += 1
            elif op == 'mul':
                self.registers[p1] *= self.get_value(p2)
                self.instr_ptr += 1
            elif op == 'mod':
                self.registers[p1] %= self.get_value(p2)
                self.instr_ptr += 1
            elif op == 'rcv':
                self.instr_ptr += 1
                if self.get_value(p1) != 0:
                    return self.sound
            elif op == 'jgz':
                if self.get_value(p1) > 0:
                    self.instr_ptr += self.get_value(p2)
                else:
                    self.instr_ptr += 1
        return self.sound


class Computer2:
    def __init__(self, instructions: List[Tuple], identifier: int):
        self.registers = defaultdict(int)
        self.instructions = instructions
        self.instr_ptr = 0
        self.max_ptr = len(self.instructions)
        self.input = []
        self.output = 0
        self.status = OK
        self.identifier = identifier
        self.num_sent = 0

    def get_value(self, param):
        if param in 'abcdefghijklmnopqrstuvw':
            return self.registers[param]
        else:
            return int(param)

    def run(self):
        while self.instr_ptr < self.max_ptr:
            op, p1, p2 = self.instructions[self.instr_ptr]
            if op == 'snd':
                self.instr_ptr += 1
                self.output = self.get_value(p1)
                self.num_sent += 1
                raise SendException
            elif op == 'set':
                self.registers[p1] = self.get_value(p2)
                self.instr_ptr += 1
            elif op == 'add':
                self.registers[p1] += self.get_value(p2)
                self.instr_ptr += 1
            elif op == 'mul':
                self.registers[p1] *= self.get_value(p2)
                self.instr_ptr += 1
            elif op == 'mod':
                self.registers[p1] %= self.get_value(p2)
                self.instr_ptr += 1
            elif op == 'rcv':
                if self.input:
                    # other program has sent
                    self.registers[p1] = self.input.pop(0)
                    self.status = OK
                    self.instr_ptr += 1
                else:
                    self.status = RECEIVING
                    raise ReceiveException
            elif op == 'jgz':
                if self.get_value(p1) > 0:
                    self.instr_ptr += self.get_value(p2)
                else:
                    self.instr_ptr += 1
        self.status = DONE


def parse_input(filename: str) -> List[Tuple]:
    lines = [line.strip() for line in open(filename).readlines()]
    instructions = []
    for line in lines:
        instruction = line.split(' ')
        op = instruction[0]
        reg = instruction[1]
        val = 0
        if instruction[0] not in ['snd', 'rcv']:
            val = instruction[2]
        instructions.append((op, reg, val))
    return instructions


def part1(instructions: List[Tuple]) -> int:
    computer = Computer(instructions)
    return computer.run()


def part2(instructions: List[Tuple]) -> int:
    computers = [Computer2(instructions, 0), Computer2(instructions, 1)]
    computers[1].registers['p'] = 1

    current, other = 0, 1
    while True:
        if computers[current].status == DONE and computers[other] == DONE:
            break
        elif computers[current].status == RECEIVING and computers[other].status == RECEIVING:
            break
        try:
            computers[current].run()
        except SendException:
            computers[other].input.append(computers[current].output)
            if computers[other].status == RECEIVING:
                computers[other].status = OK
        except ReceiveException:
            if not computers[current].input:
                current, other = other, current
    return computers[1].num_sent


def main():
    instructions = parse_input('input/day18.txt')
    print(f'Part 1: {part1(instructions)}')
    print(f'Part 2: {part2(instructions)}')


if __name__ == "__main__":
    main()
