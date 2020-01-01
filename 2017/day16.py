def read_input() -> list:
    instruction_strings = open("input/day16.txt").readline().strip().split(",")
    instructions = []

    for s in instruction_strings:
        if s[0] == "x":
            instruction = ["x"] + [int(p) for p in s[1:].split("/")]
        if s[0] == "p":
            instruction = ["p"] + [p for p in s[1:].split("/")]
        if s[0] == "s":
            instruction = ["s", int(s[1:]), None]
        instructions.append(instruction)

    return instructions


def execute_instructions(state: list, reps: int, instructions: list) -> str:
    seen = []

    for rep in range(reps):
        s = "".join(state)
        if s in seen:
            return seen[reps % rep]
        seen.append(s)

        for i in instructions:
            op, p1, p2 = i
            if op == "s":
                state = state[-p1:] + state[:-p1]
            if op == "x":
                state[p1], state[p2] = state[p2], state[p1]
            if op == "p":
                p1_index, p2_index = state.index(p1), state.index(p2)
                state[p1_index], state[p2_index] = state[p2_index], state[p1_index]

    return "".join(state)


def puzzles():
    instructions = read_input()
    programs = "abcdefghijklmnop"
    programs = [ch for ch in programs]
    result = execute_instructions(programs, 1, instructions)
    print(result)
    programs = "abcdefghijklmnop"
    programs = [ch for ch in programs]
    result = execute_instructions([ch for ch in programs], 1000000000, instructions)
    print(result)


if __name__ == "__main__":
    puzzles()
