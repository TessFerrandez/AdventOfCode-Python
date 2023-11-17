from input_processing import read_data
from math import lcm
from collections import deque


class Monkey:
    def __init__(self, data):
        data = data.splitlines()
        self.id = int(data[0].split()[1][:-1])
        self.items = deque([int(i) for i in data[1][18:].split(", ")])
        self.test = int(data[3].split()[-1])
        self.true = int(data[4].split()[-1])
        self.false = int(data[5].split()[-1])
        operation = data[2][19:].split()
        if operation[1] == "+":
            self.op = "add"
            self.value = int(operation[2])
        if operation[1] == "*":
            if operation[2] == "old":
                self.op = "pow"
                self.value = 0
            else:
                self.op = "mul"
                self.value = int(operation[2])

    def __repr__(self):
        return f"Monkey({self.id}) {list(self.items)} {self.op} {self.value} {self.test} {self.true} {self.false}"

    def add(self, old):
        return old + self.value

    def mul(self, old):
        return old * self.value

    def pow(self, old):
        return old * old


def parse(data):
    monkey_data = data.split("\n\n")
    monkeys = [Monkey(d) for d in monkey_data]
    return monkeys


def part1(monkeys):
    inspections = [0] * len(monkeys)

    for _ in range(20):
        for monkey in monkeys:
            while monkey.items:
                inspections[monkey.id] += 1
                item = monkey.items.popleft()
                if monkey.op == "add":
                    item = monkey.add(item)
                elif monkey.op == "mul":
                    item = monkey.mul(item)
                elif monkey.op == "pow":
                    item = monkey.pow(item)
                item = item // 3
                if item % monkey.test == 0:
                    monkeys[monkey.true].items.append(item)
                else:
                    monkeys[monkey.false].items.append(item)
    inspections.sort()
    return inspections[-1] * inspections[-2]


def part2(monkeys):
    lcm_val = 1
    for monkey in monkeys:
        lcm_val = lcm(lcm_val, monkey.test)

    inspections = [0] * len(monkeys)

    for _ in range(10000):
        for monkey in monkeys:
            while monkey.items:
                inspections[monkey.id] += 1
                item = monkey.items.popleft()
                if monkey.op == "add":
                    item = monkey.add(item)
                elif monkey.op == "mul":
                    item = monkey.mul(item)
                elif monkey.op == "pow":
                    item = monkey.pow(item)
                item = item % lcm_val
                if item % monkey.test == 0:
                    monkeys[monkey.true].items.append(item)
                else:
                    monkeys[monkey.false].items.append(item)
    inspections.sort()
    return inspections[-1] * inspections[-2]


def test():
    sample = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""
    monkeys = parse(sample)
    assert part1(monkeys) == 10605
    monkeys = parse(sample)
    assert part2(monkeys) == 2713310158


test()
monkeys = parse(read_data(2022, 11))
print('Part1:', part1(monkeys))
monkeys = parse(read_data(2022, 11))
print('Part2:', part2(monkeys))
