from typing import Dict, List, Tuple


lines = [line.strip() for line in open('2021//input//day4.txt', 'r').readlines()]


def get_boards(lines: List[str]) -> List[List[List[int]]]:
    boards = []
    current_board = []

    for line in lines[1:]:
        if line == "":
            if current_board:
                boards.append(current_board)
            current_board = []
        else:
            current_board.append([int(number) for number in line.split(' ') if number != ''])

    if current_board:
        boards.append(current_board)

    return boards


def get_numbers(lines: List[str]) -> Dict[int, int]:
    numbers: List[int] = [int(number) for number in lines[0].split(',')]
    call_order: Dict[int, int] = {}
    for i, number in enumerate(numbers):
        call_order[number] = i

    return call_order


def calculate_worst_board(boards, call_order) -> Tuple[int, int]:
    wins_at = -1
    loosing_board = -1

    for board_i, board in enumerate(boards):
        min_board_call = len(call_order.keys())

        # rows
        for row in board:
            max_row_call = max(call_order[number] for number in row)
            min_board_call = min(min_board_call, max_row_call)

        # columns
        for column in zip(*board):
            max_column_call = max(call_order[number] for number in column)
            min_board_call = min(min_board_call, max_column_call)

        if min_board_call > wins_at:
            wins_at = min_board_call
            loosing_board = board_i

    return wins_at, loosing_board


def calculate_board(board, wins_at, call_order):
    num_called = list(call_order.keys())[list(call_order.values()).index(wins_at)]
    sum_not_called = sum(number for row in board for number in row if call_order[number] > wins_at)
    return num_called * sum_not_called


boards = get_boards(lines)
call_order = get_numbers(lines)
wins_at, worst_board = calculate_worst_board(boards, call_order)
print(calculate_board(boards[worst_board], wins_at, call_order))
