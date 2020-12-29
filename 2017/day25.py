from collections import defaultdict


def parse_input():
    return {'A': [[1, 1, 'B'], [0, -1, 'C']],
            'B': [[1, -1, 'A'], [1, 1, 'D']],
            'C': [[1, 1, 'A'], [0, -1, 'E']],
            'D': [[1, 1, 'A'], [0, 1, 'B']],
            'E': [[1, -1, 'F'], [1, -1, 'C']],
            'F': [[1, 1, 'D'], [1, 1, 'A']]}


def part1(states: dict, steps: int) -> int:
    tape = defaultdict(int)
    ptr = 0
    state = 'A'

    for _ in range(steps):
        value, delta, next_state = states[state][tape[ptr]]
        tape[ptr] = value
        ptr += delta
        state = next_state

    check_sum = sum(tape[ptr] for ptr in tape)
    return check_sum


def main():
    states = parse_input()
    steps = 12173597
    # states = {'A': [[1, 1, 'B'], [0, -1, 'B']], 'B': [[1, -1, 'A'], [1, 1, 'A']]}
    # steps = 6
    print(f'Part 1: {part1(states, steps)}')


if __name__ == "__main__":
    main()
