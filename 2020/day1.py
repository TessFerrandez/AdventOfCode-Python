from typing import List


def puzzle1(expenses: List[int]) -> int:
    for i, expense in enumerate(expenses):
        expense2 = 2020 - expense
        if expense2 in expenses[i:]:
            return expense * expense2


def puzzle2(expenses: List[int]) -> int:
    for i, expense1 in enumerate(expenses):
        for j, expense2 in enumerate(expenses[i:]):
            expense3 = 2020 - expense1 - expense2
            if expense3 in expenses[i + j :]:
                return expense1 * expense2 * expense3


def main():
    with open("input/day1.txt") as f:
        expenses = [int(line.strip()) for line in f.readlines()]
    puzzle1_result = puzzle1(expenses)
    print(f"Puzzle1: {puzzle1_result}")
    puzzle2_result = puzzle2(expenses)
    print(f"Puzzle2: {puzzle2_result}")


if __name__ == "__main__":
    main()
