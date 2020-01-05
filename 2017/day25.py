from collections import defaultdict


states = {
    "A": [[1, 1, "B"], [0, -1, "C"]],
    "B": [[1, -1, "A"], [1, 1, "D"]],
    "C": [[1, 1, "A"], [0, -1, "E"]],
    "D": [[1, 1, "A"], [0, 1, "B"]],
    "E": [[1, -1, "F"], [1, -1, "C"]],
    "F": [[1, 1, "D"], [1, 1, "A"]],
}

tape = defaultdict(int)


def puzzles(steps: int):
    state = "A"
    ptr = 0
    for i in range(steps):
        curr_val = tape[ptr]
        next_val, next_move, next_state = states[state][curr_val]
        tape[ptr] = next_val
        ptr += next_move
        state = next_state

    check_sum = 0
    for slot in tape:
        check_sum += tape[slot]
    print("check sum:", check_sum)


if __name__ == "__main__":
    puzzles(12173597)
