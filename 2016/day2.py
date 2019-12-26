PAD = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


PAD2 = [
    ["X", "X", "1", "X", "X"],
    ["X", "2", "3", "4", "X"],
    ["5", "6", "7", "8", "9"],
    ["X", "A", "B", "C", "X"],
    ["X", "X", "D", "X", "X"],
]


INSTR = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


def is_valid(x, y):
    if 0 <= x < 5:
        if 0 <= y < 5:
            if PAD2[x][y] != "X":
                return True
    return False


def puzzle1():
    # start at 5
    cur = (1, 1)

    code = ""
    with open("input/day2.txt") as f:
        for line in f:
            for direction in line.strip():
                x = clamp(cur[0] + INSTR[direction][0], 0, 2)
                y = clamp(cur[1] + INSTR[direction][1], 0, 2)
                cur = (x, y)
            code += str(PAD[cur[1]][cur[0]])
    print("code:", code)


def puzzle2():
    # start at 5
    cur = (0, 2)

    code = ""
    with open("input/day2.txt") as f:
        for line in f:
            for direction in line.strip():
                x = cur[0] + INSTR[direction][0]
                y = cur[1] + INSTR[direction][1]
                if is_valid(x, y):
                    cur = (x, y)

            code += str(PAD2[cur[1]][cur[0]])
        print("code:", code)


if __name__ == "__main__":
    puzzle1()
    puzzle2()
