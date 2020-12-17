from typing import List, Tuple


def is_wall(square: Tuple[int, int], offset: int) -> bool:
    x, y = square
    val = x * x + 3 * x + 2 * x * y + y + y * y + offset
    ones = '{0:b}'.format(val).count('1')
    return ones % 2 != 0


def generate_board(rows: int, cols: int, offset: int) -> List[List[str]]:
    return [['#' if is_wall((x, y), offset) else '.' for x in range(cols)]
            for y in range(rows)]


def get_moves(board: List[List[str]], point: Tuple[int, int]) -> List:
    x, y = point
    possible_moves = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
    moves = []

    height, width = len(board), len(board[0])
    for move in possible_moves:
        x, y = move
        if x < 0 or y < 0:
            pass
        elif x == width or y == height:
            pass
        elif board[y][x] == '#':
            pass
        else:
            moves.append(move)
    return moves


def bfs_shortest_path(board: List[List[str]], start: Tuple[int, int], goal: Tuple[int, int]) -> List:
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


def bfs_visited(board: List[List[str]], start: Tuple[int, int], max_path) -> List:
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


def part1(board: List[List[str]]) -> int:
    path = bfs_shortest_path(board, (1, 1), (31, 39))
    return len(path) - 1


def part2(board: List[List[str]]) -> int:
    visited = bfs_visited(board, (1, 1), 50)
    return len(visited)


def main():
    board = generate_board(50, 50, 1364)
    print(f'Part 1: {part1(board)}')
    print(f'Part 2: {part2(board)}')


if __name__ == "__main__":
    main()
