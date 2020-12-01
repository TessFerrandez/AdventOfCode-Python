from typing import List


def puzzle1(input_values: List[int]) -> int:
    for i in range(len(input_values)):
        value1 = input_values[i]
        if 2020 - value1 in input_values[i:]:
            return value1 * (2020 - value1)


def puzzle2(input_values: List[int]) -> int:
    return 0


def main():
    with open("input/day1.txt") as f:
        input_values = [int(line.strip()) for line in f.readlines()]
    puzzle1_result = puzzle1(input_values)
    print(f"Puzzle1: {puzzle1_result}")
    puzzle2_result = puzzle2(input_values)
    print(f"Puzzle2: {puzzle2_result}")


if __name__ == "__main__":
    main()
