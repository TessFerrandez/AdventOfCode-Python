from ComputerV4 import Computer, OutputInterrupt


def get_boost_code(code) -> int:
    computer = Computer(code)
    computer.inputs.append(1)

    while not computer.done:
        try:
            computer.run()
        except OutputInterrupt:
            return computer.outputs.pop()

    return 0


def get_distress_signal(code) -> int:
    computer = Computer(code)
    computer.inputs.append(2)

    while not computer.done:
        try:
            computer.run()
        except OutputInterrupt:
            return computer.outputs.pop()

    return 0


code = open('2019/input/day9.txt').read().strip()
print("Part 1:", get_boost_code(code))
print("Part 1:", get_distress_signal(code))
