import matplotlib.pyplot as plt


def parse_initial_state():
    lines = [line.strip() for line in open("input/day18.txt").readlines()]
    board = [[1 if char is "#" else 0 for char in line] for line in lines]
    return board


def in_bounds(row, col, board) -> bool:
    if row < 0 or col < 0:
        return False
    if row > len(board) - 1 or col > len(board[0]) - 1:
        return False
    return True


def get_neighbors_on(current_row: int, current_col: int, board: int) -> int:
    lights_on = 0
    for row in range(current_row - 1, current_row + 2):
        for col in range(current_col - 1, current_col + 2):
            if in_bounds(row, col, board):
                lights_on += board[row][col]

    # disregard the current one
    if board[current_row][current_col] == 1:
        lights_on -= 1

    return lights_on


def is_corner(row: int, col: int, board: list) -> bool:
    if row == 0 and col == 0:
        return True
    elif row == 0 and col == (len(board[0]) - 1):
        return True
    elif col == 0 and row == (len(board) - 1):
        return True
    elif col == (len(board[0]) - 1) and row == (len(board) - 1):
        return True
    return False


def animate(board: list, corner_on: bool = False):
    original_board = [row[:] for row in board]
    for row_no, row in enumerate(board):
        for col_no, light in enumerate(row):
            if corner_on and is_corner(row_no, col_no, board):
                board[row_no][col_no] = 1
            else:
                neighbors_on = get_neighbors_on(row_no, col_no, original_board)
                if light == 1:
                    if not (neighbors_on == 2 or neighbors_on == 3):
                        board[row_no][col_no] = 0
                else:
                    if neighbors_on == 3:
                        board[row_no][col_no] = 1


def count_lights(board: list) -> int:
    sum_lights = 0
    for row in board:
        sum_lights += sum(row)
    return sum_lights


def puzzles():
    board = parse_initial_state()
    for i in range(100):
        animate(board)
    plt.imshow(board)
    plt.show()
    print("num lights", count_lights(board))

    board = parse_initial_state()
    board[0][0] = 1
    board[0][99] = 1
    board[99][0] = 1
    board[99][99] = 1
    for i in range(100):
        animate(board, corner_on=True)
    plt.imshow(board)
    plt.show()
    print("num lights", count_lights(board))


if __name__ == "__main__":
    puzzles()
