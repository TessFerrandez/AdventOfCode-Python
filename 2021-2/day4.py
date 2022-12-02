from collections import defaultdict


def parse_input(sample_input):
    lines = sample_input.splitlines()
    numbers = [int(d) for d in lines[0].split(',')]

    i = 2
    boards = []
    while i < len(lines):
        boards.append([])
        for j in range(5):
            boards[-1].append([int(d) for d in lines[i].split(' ') if d != ''])
            i += 1
        i += 1

    return boards, numbers


def get_board_scores(boards, numbers):
    call_order = defaultdict(lambda: 10 ** 9)
    for i, num in enumerate(numbers):
        call_order[num] = i

    board_scores = []

    for board in boards:
        best = 10 ** 9
        for row in board:
            score = max(call_order[num] for num in row)
            best = min(best, score)
        for col in range(5):
            score = max(call_order[board[row][col]] for row in range(5))
            best = min(best, score)
        board_scores.append(best)

    return call_order, board_scores


def score_board(board, call_order, last_call):
    sum_unmarked = 0
    for row in board:
        for num in row:
            if call_order[num] > last_call:
                sum_unmarked += num
    return sum_unmarked


def part1(boards, numbers) -> int:
    call_order, board_scores = get_board_scores(boards, numbers)

    best_board, last_call = 0, 10 ** 9
    for i, score in enumerate(board_scores):
        if score < last_call:
            best_board = i
            last_call = score

    board_score = score_board(boards[best_board], call_order, last_call)

    return board_score * numbers[last_call]


def part2(boards, numbers) -> int:
    call_order, board_scores = get_board_scores(boards, numbers)

    best_board, last_call = 0, 0
    for i, score in enumerate(board_scores):
        if score > last_call:
            best_board = i
            last_call = score

    board_score = score_board(boards[best_board], call_order, last_call)

    return board_score * numbers[last_call]


sample_input = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''


boards, numbers = parse_input(sample_input)
assert part1(boards, numbers) == 4512
assert part2(boards, numbers) == 1924

boards, numbers = parse_input(open('./2021/input/day4.txt').read().strip())
print("Part1:", part1(boards, numbers))
print("Part2:", part2(boards, numbers))
