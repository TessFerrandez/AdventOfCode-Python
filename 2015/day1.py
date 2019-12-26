def calculate_floor(instructions):
    return instructions.count("(") - instructions.count(")")


def calculate_first_basement(instructions):
    floor = 0
    index = 1
    for char in instructions:
        if char == "(":
            floor += 1
        if char == ")":
            floor -= 1
        if floor < 0:
            return index
        index += 1
    return -1


def puzzles():
    print("floor:", calculate_floor(open("input/day1.txt").read()))
    print(
        "first time in basement:",
        calculate_first_basement(open("input/day1.txt").read()),
    )


if __name__ == "__main__":
    puzzles()
