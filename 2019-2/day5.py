from ComputerV2 import Computer


code = open('2019/input/day5.txt').read().strip()

# PART 1
computer = Computer(code)
computer.inputs.append(1)
computer.run()

# PART 2
computer = Computer(code)
computer.inputs.append(5)
computer.run()
