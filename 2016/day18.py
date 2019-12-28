def is_safe(row, pos):
    section = row[pos - 1 : pos + 2]
    if section == "^^." or section == ".^^" or section == "^.." or section == "..^":
        return False
    return True


def generate_board(first_row: str, rows: int) -> list:
    board = [first_row]
    row_len = len(first_row)
    current_row = "." + first_row + "."
    for i in range(rows - 1):
        next_row = ""
        for j in range(1, row_len + 1):
            next_row += "." if is_safe(current_row, j) else "^"

        board.append(next_row)
        current_row = "." + next_row + "."
    return board


def puzzles():
    board = generate_board(
        ".^^^.^.^^^^^..^^^..^..^..^^..^.^.^.^^.^^....^.^...^.^^.^^.^^..^^..^.^..^^^.^^...^...^^....^^.^^^^^^^",
        40,
    )
    num_safe = 0
    for row in board:
        num_safe += row.count(".")
        # print(row)
    print("safe:", num_safe)
    board = generate_board(
        ".^^^.^.^^^^^..^^^..^..^..^^..^.^.^.^^.^^....^.^...^.^^.^^.^^..^^..^.^..^^^.^^...^...^^....^^.^^^^^^^",
        400000,
    )
    num_safe = 0
    for row in board:
        num_safe += row.count(".")
        # print(row)
    print("safe:", num_safe)


if __name__ == "__main__":
    puzzles()
