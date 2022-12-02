from ComputerV3 import Computer, OutputInterrupt, InputInterrupt
from itertools import permutations


def read_input():
    return open('2019/input/day7.txt').read().strip()


def run_circuit(code, phases) -> int:
    out = 0

    for phase in phases:
        computer = Computer(code)
        computer.inputs.append(phase)
        computer.inputs.append(out)
        try:
            computer.run()
        except OutputInterrupt:
            out = computer.outputs.pop()

    return out


def run_feedback_loop(code, phases) -> int:
    computers = []

    for phase in phases:
        computer = Computer(code)
        computer.inputs.append(phase)
        computers.append(computer)

    done = False
    out = 0
    compi = 0
    while not done:
        current_computer = computers[compi]
        current_computer.inputs.append(out)
        try:
            current_computer.run()
            done = True
        except InputInterrupt:
            pass
        except OutputInterrupt:
            out = current_computer.outputs.pop()
        compi = (compi + 1) % 5

    return out


def tests():
    code = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
    assert run_circuit(code, [4, 3, 2, 1, 0]) == 43210
    code = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'
    assert run_circuit(code, [0, 1, 2, 3, 4]) == 54321
    code = '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0'
    assert run_circuit(code, [1, 0, 4, 3, 2]) == 65210
    code = '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'
    assert run_feedback_loop(code, [9, 8, 7, 6, 5]) == 139629729
    code = '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10'
    assert run_feedback_loop(code, [9, 7, 8, 5, 6]) == 18216


def part1(code):
    return max(run_circuit(code, phases) for phases in permutations([0, 1, 2, 3, 4]))


def part2(code):
    return max(run_feedback_loop(code, phases) for phases in permutations([5, 6, 7, 8, 9]))


tests()


code = read_input()
print("Part 1:", part1(code))
print("Part 2:", part2(code))
