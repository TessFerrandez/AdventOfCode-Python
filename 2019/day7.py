import pytest
from typing import List, Tuple
from itertools import permutations
from Computer import Computer, OutputInterrupt, InputInterrupt
from copy import copy


@pytest.mark.parametrize('code, expected',
                         [
                             ([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0], 43210),
                             ([3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0], 54321),
                             ([3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0], 65210),
                         ])
def test_part1(code: List[int], expected: int):
    assert part1(code) == expected


@pytest.mark.parametrize('code, expected',
                         [
                             ([3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5], 139629729),
                             ([3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54, -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4, 53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10], 18216),
                         ])
def test_part2(code: List[int], expected: int):
    assert part2(code) == expected


def parse_input(filename: str) -> List[int]:
    return [int(d) for d in open(filename).read().strip().split(',')]


def part1(code: List[int]) -> int:
    max_thruster_signal = 0
    best_phase = (0, 0, 0, 0, 0)

    combos = permutations([0, 1, 2, 3, 4], 5)
    for phases in combos:
        next_input = 0
        for phase in phases:
            comp = Computer(copy(code))
            comp.inputs.append(phase)
            comp.inputs.append(next_input)
            try:
                comp.run()
            except OutputInterrupt:
                next_input = comp.outputs[-1]
        if next_input > max_thruster_signal:
            max_thruster_signal = next_input
            best_phase = phases
    print(best_phase)
    return max_thruster_signal


def run_computers(phases: Tuple, code: List[int]) -> int:
    computers = []
    for phase in phases:
        computer = Computer(copy(code))
        computer.inputs.append(phase)
        computers.append(computer)

    i = -1
    computers[0].inputs.append(0)
    while True:
        i = (i + 1) % 5
        while not computers[i].done:
            try:
                computers[i].run()
            except OutputInterrupt:
                next_val = computers[i].outputs[-1]
                computers[(i + 1) % 5].inputs.append(next_val)
                continue
            except InputInterrupt:
                break
        if all(map(lambda comp: comp.done, computers)):
            break
    return computers[0].inputs[-1]


def part2(code: List[int]) -> int:
    combos = permutations([5, 6, 7, 8, 9], 5)
    max_thruster_signal = max(run_computers(combo, code) for combo in combos)
    return max_thruster_signal


def main():
    code = parse_input('input/day7.txt')
    print(f'Part 1: {part1(code)}')
    print(f'Part 2: {part2(code)}')


if __name__ == "__main__":
    main()
