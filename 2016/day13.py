def count_set_bits(n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def is_on(square: list, offset: int) -> bool:
    val = (
        square[0] * square[0]
        + 3 * square[0]
        + 2 * square[0] * square[1]
        + square[1]
        + square[1] * square[1]
        + offset
    )
    bits = count_set_bits(val)
    if bits % 2 == 0:
        return False
    return True


def generate_board(rows: int, cols: int, offset: int):
    board = []
    for row_no in range(rows):
        row = []
        for col_no in range(cols):
            row.append("#" if is_on([col_no, row_no], offset) else ".")
        board.append(row)
    return board


def get_moves(board: list, point: list) -> list:
    poss_moves = [
        [point[0], point[1] - 1],
        [point[0] + 1, point[1]],
        [point[0], point[1] + 1],
        [point[0] - 1, point[1]],
    ]
    moves = []
    max_row = len(board)
    max_col = len(board[0])
    for move in poss_moves:
        if move[0] < 0 or move[1] < 0:
            pass
        elif move[0] == max_col or move[1] == max_row:
            pass
        elif board[move[1]][move[0]] == "#":
            pass
        else:
            moves.append(move)
    return moves


def bfs_shortest_path(board: list, start: list, goal: list) -> list:
    visited = []
    to_visit = [[start]]

    if start == goal:
        return []

    while to_visit:
        path = to_visit.pop(0)
        square = path[-1]
        if square not in visited:
            moves = get_moves(board, square)
            for move in moves:
                new_path = list(path)
                new_path.append(move)
                to_visit.append(new_path)
                if move == goal:
                    return new_path
            visited.append(square)
    return []


def bfs_visited(board: list, start: list, max_path=10) -> list:
    visited = []
    to_visit = [start]
    next_steps = []

    for i in range(max_path):
        for node in to_visit:
            moves = get_moves(board, node)
            for move in moves:
                if move not in visited:
                    next_steps.append(move)
                    visited.append(move)
        to_visit = next_steps.copy()
        next_steps.clear()

    return visited


def puzzles():
    board = generate_board(50, 50, 1364)
    path = bfs_shortest_path(board, [1, 1], [31, 39])
    print("lowest number of steps:", len(path) - 1)
    visited = bfs_visited(board, [1, 1], 50)
    print("squares visited in less than 50 moves:", len(visited))


if __name__ == "__main__":
    puzzles()
