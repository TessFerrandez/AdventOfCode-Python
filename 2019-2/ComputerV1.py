inputs = '''1,9,10,3,2,3,11,0,99,30,40,50'''


class Computer():
    def __init__(self, code: str, noun: int = -1, verb: int = -1) -> None:
        self.memory = [int(d) for d in code.strip().split(',')]
        if noun != -1:
            self.memory[1] = noun
            self.memory[2] = verb
        self.maxip = len(self.memory)

    def __str__(self) -> str:
        return ','.join(str(d) for d in self.memory)

    def run(self):
        ip = 0

        while self.memory[ip] != 99 and ip < self.maxip:
            op, p1, p2, p3 = self.memory[ip: ip + 4]
            if op == 1:
                self.memory[p3] = self.memory[p1] + self.memory[p2]
            elif op == 2:
                self.memory[p3] = self.memory[p1] * self.memory[p2]
            ip += 4


def tests():
    for initial, final in [('1,0,0,0,99', '2,0,0,0,99'),
                           ('2,3,0,3,99', '2,3,0,6,99'),
                           ('2,4,4,5,99,0', '2,4,4,5,99,9801'),
                           ('1,1,1,4,99,5,6,0,99', '30,1,1,4,2,5,6,0,99')]:
        computer = Computer(initial)
        computer.run()
        assert str(computer) == final


tests()
