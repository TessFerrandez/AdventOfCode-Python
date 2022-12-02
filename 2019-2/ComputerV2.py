from collections import deque


class Computer():
    def __init__(self, code: str) -> None:
        self.memory = [int(d) for d in code.strip().split(',')]
        self.maxip = len(self.memory)
        self.inputs = deque()

    def __str__(self) -> str:
        return ','.join(str(d) for d in self.memory)

    def get_instruction(self, ip):
        opx = self.memory[ip]
        op = opx % 10
        args = []
        if op in [1, 2, 7, 8]:
            p1, p2, p3 = self.memory[ip + 1: ip + 4]
            args.append(p1 if (opx % 1000) // 100 == 1 else self.memory[p1])
            args.append(p2 if opx // 1000 == 1 else self.memory[p2])
            args.append(p3)
        elif op in [5, 6]:
            p1, p2 = self.memory[ip + 1: ip + 3]
            args.append(p1 if (opx % 1000) // 100 == 1 else self.memory[p1])
            args.append(p2 if opx // 1000 == 1 else self.memory[p2])
        else:
            args.append(self.memory[ip + 1])
        return op, args

    def run(self):
        ip = 0

        while ip < self.maxip and self.memory[ip] != 99:
            op, args = self.get_instruction(ip)
            if op == 1:
                p1, p2, p3 = args
                self.memory[p3] = p1 + p2
                ip += 4
            elif op == 2:
                p1, p2, p3 = args
                self.memory[p3] = p1 * p2
                ip += 4
            elif op == 3:
                p1 = args[0]
                self.memory[p1] = self.inputs.popleft()
                ip += 2
            elif op == 4:
                p1 = args[0]
                print(self.memory[p1])
                ip += 2
            elif op == 5:
                p1, p2 = args
                if p1 != 0:
                    ip = p2
                else:
                    ip += 3
            elif op == 6:
                p1, p2 = args
                if p1 == 0:
                    ip = p2
                else:
                    ip += 3
            elif op == 7:
                p1, p2, p3 = args
                self.memory[p3] = 1 if p1 < p2 else 0
                ip += 4
            elif op == 8:
                p1, p2, p3 = args
                self.memory[p3] = 1 if p1 == p2 else 0
                ip += 4


def tests():
    computer = Computer('3,0,4,0,99')
    computer.inputs.append(5)
    computer.run()

    for initial, final in [('1,0,0,0,99', '2,0,0,0,99'),
                           ('2,3,0,3,99', '2,3,0,6,99'),
                           ('1002,4,3,4,33', '1002,4,3,4,99'),
                           ('1101,100,-1,4,0', '1101,100,-1,4,99')]:
        computer = Computer(initial)
        computer.run()
        assert str(computer) == final


tests()
