from utils import knot_hash


def assemble_board(data: str) -> list:
    board = []
    for i in range(128):
        row_hash = knot_hash(data + "-" + str(i))
        integer = int(row_hash, 16)
        board.append(format(integer, "0>128b"))
    return board


def count_filled(board: list) -> int:
    row_sum = 0
    for row in board:
        row_sum += sum([1 if num == "1" else 0 for num in row])
    return row_sum


def find_regions(board: list) -> list:
    regions = []
    for y in range(len(board)):
        for x in range(len(board[0])):
            combine = []
            if board[y][x] == "1":
                for j in range(len(regions)):
                    if (x - 1, y) in regions[j]:
                        combine.append(j)
                        break
                for j in range(len(regions)):
                    if (x, y - 1) in regions[j]:
                        combine.append(j)
                        break
                if not combine:
                    regions.append([(x, y)])
                else:
                    regions[combine[0]] += [(x, y)]
                    if len(combine) == 2 and combine[0] != combine[1]:
                        regions[combine[0]] += regions[combine[1]]
                        regions.pop(combine[1])

    return regions


def puzzles():
    board = assemble_board("stpzcrnm")
    #    for row in board:
    #        print(row)
    print("filled:", count_filled(board))
    regions = find_regions(board)
    print("number of regions:", len(regions))


if __name__ == "__main__":
    puzzles()
