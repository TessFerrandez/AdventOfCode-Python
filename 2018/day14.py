def puzzle1(puzzle_input: str) -> str:
    scores = "37"
    pos1 = 0
    pos2 = 1

    for i in range(int(puzzle_input) + 10):
        score = str(int(scores[pos1]) + int(scores[pos2]))
        scores += score
        score_len = len(scores)
        pos1 = (pos1 + 1 + int(scores[pos1])) % score_len
        pos2 = (pos2 + 1 + int(scores[pos2])) % score_len
    return scores[int(puzzle_input) : int(puzzle_input) + 10]


def puzzle2(puzzle_input: str) -> int:
    scores = "37"
    pos1 = 0
    pos2 = 1

    puzzle_len = len(puzzle_input) + 1
    while puzzle_input not in scores[-puzzle_len:]:
        score = str(int(scores[pos1]) + int(scores[pos2]))
        scores += score
        score_len = len(scores)
        pos1 = (pos1 + 1 + int(scores[pos1])) % score_len
        pos2 = (pos2 + 1 + int(scores[pos2])) % score_len
    return scores.index(puzzle_input)


def main():
    puzzle_input = "320851"
    puzzle1_result = puzzle1(puzzle_input)
    print(f"Puzzle 1: {puzzle1_result}")
    puzzle2_result = puzzle2(puzzle_input)
    print(f"Puzzle 2: {puzzle2_result}")


if __name__ == "__main__":
    main()
