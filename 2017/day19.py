def read_input() -> list:
    rows = [line[:-1] for line in open("input/day19.txt").readlines()]
    max_len = max([len(row) for row in rows])
    for row_n in range(len(rows)):
        for i in range(max_len - len(rows[row_n])):
            rows[row_n] += " "
    return rows


def follow_path(board: list) -> (str, int):
    max_col = len(board[0])

    letters = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
    path = ""
    dirs = {"D": (0, 1), "U": (0, -1), "L": (-1, 0), "R": (1, 0)}

    pos = board[0].index("|"), 0
    d = "D"
    i = 0
    while True:
        i += 1
        x, y = pos
        next_x, next_y = x + dirs[d][0], y + dirs[d][1]
        if not 0 <= x < max_col or not 0 <= y < len(board):
            print(x, y, "out of bounds")
            break
        if board[y][x] == " ":
            print(x, y, "space")
            break
        elif board[y][x] == "+":
            # change direction
            if d == "U" or d == "D":
                d = "R"
                if x - 1 >= 0:
                    if board[y][x - 1] == "-" or board[y][x - 1] in letters:
                        d = "L"
            else:
                d = "D"
                if y - 1 >= 0:
                    if board[y - 1][x] == "|" or board[y - 1][x] in letters:
                        d = "U"
            next_x, next_y = x + dirs[d][0], y + dirs[d][1]
        elif board[y][x] in letters:
            path += board[y][x]
        pos = next_x, next_y

    return path, i - 1


def puzzles():
    board = read_input()
    # for row in board:
    #     print(row)
    chars, steps = follow_path(board)
    print("path:", chars)
    print("steps:", steps)


if __name__ == "__main__":
    puzzles()
