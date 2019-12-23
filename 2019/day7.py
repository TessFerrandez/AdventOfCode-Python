from IntCode import IntCode, OutputInterrupt, InputInterrupt
from itertools import permutations
from collections import deque


def run_sequence(sequence):
    amp = 0
    for phase in sequence:
        computer = IntCode(open('input/day7.txt').readline())
        computer.input_queue = deque([phase, amp])
        while not computer.done:
            try:
                computer.run()
            except OutputInterrupt:
                pass

        amp = computer.output_queue.popleft()

    return amp


def run_sequence_v2(sequence, program):
    computers = list()

    for phase in sequence:
        computers.append(IntCode(program))
        computers[-1].input_queue.append(phase)

    i = -1
    computers[0].input_queue.append(0)
    while True:
        i = (i + 1) % 5
        while not computers[i].done:
            try:
                computers[i].run()
            except OutputInterrupt:
                computers[(i + 1) % 5].input_queue.append(
                    computers[i].output_queue[-1])
                continue
            except InputInterrupt:
                break

        if all(map(lambda x: x.done, computers)):
            break

    return computers[0].input_queue[-1]


def puzzle1():
    sequences = permutations(range(5))
    max_sequence = max(sequences, key=lambda x: run_sequence(x))
    print(max_sequence)
    print("generates:", run_sequence(max_sequence))


def puzzle2():
    sequences = permutations(range(5, 10))
    program = open('input/day7.txt').readline()
    max_sequence = max(sequences, key=lambda x: run_sequence_v2(x, program))
    print(max_sequence)
    print("generates:", run_sequence_v2(max_sequence, program))


if __name__ == "__main__":
    puzzle1()
    puzzle2()
