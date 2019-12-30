from collections import defaultdict
from itertools import permutations
from sys import maxsize


def read_input() -> list:
    rows = [row.strip() for row in open("input/day24.txt").readlines()]
    return rows


def get_number_positions(board: list) -> dict:
    numbers = defaultdict()

    rows = len(board)
    cols = len(board[0])

    for r in range(rows):
        for c in range(cols):
            if board[r][c] != "#" and board[r][c] != ".":
                numbers[board[r][c]] = (c, r)

    return numbers


def get_moves(board: list, square: list) -> list:
    x, y = square
    moves = []
    if board[y + 1][x] != "#":
        moves.append((x, y + 1))
    if board[y - 1][x] != "#":
        moves.append((x, y - 1))
    if board[y][x + 1] != "#":
        moves.append((x + 1, y))
    if board[y][x - 1] != "#":
        moves.append((x - 1, y))
    return moves


def shortest_path(board: list, start: list, goal: list) -> list:
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


def get_steps(board: list, numbers: dict) -> dict:
    combo_steps = defaultdict()

    for num_i in numbers:
        for num_j in numbers:
            s_path = shortest_path(board, numbers[num_i], numbers[num_j])
            steps = max(0, len(s_path) - 1)
            combo_steps[(num_i, num_j)] = steps
            combo_steps[(num_j, num_i)] = steps

    return combo_steps


def get_least_steps(numbers: dict, combo_steps: dict, end_at_0=False) -> (int, list):
    num_list = sorted([number for number in numbers])[1:]
    min_steps = maxsize
    min_path = []
    nums = len(num_list)
    for perm in permutations(num_list):
        steps = combo_steps[("0", perm[0])]
        for i in range(nums - 1):
            steps += combo_steps[(perm[i], perm[i + 1])]
        if end_at_0:
            steps += combo_steps[(perm[-1], "0")]
        if steps < min_steps:
            min_steps = steps
            min_path = perm
    return min_steps, min_path


def puzzles():
    board = read_input()
    numbers = get_number_positions(board)
    combo_steps = get_steps(board, numbers)
    least_steps, min_path = get_least_steps(numbers, combo_steps)
    print("least steps:", least_steps, min_path)
    least_steps, min_path = get_least_steps(numbers, combo_steps, end_at_0=True)
    print("least steps:", least_steps, min_path)


if __name__ == "__main__":
    puzzles()
