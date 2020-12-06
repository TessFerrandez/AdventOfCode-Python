from typing import List
from collections import defaultdict


def parse_input(filename: str) -> List[List[str]]:
    groups = [[line for line in group.split('\n')] for group in open(filename).read().split('\n\n')]
    return groups


def record_group_answers(group: List[str]) -> defaultdict:
    unique_answers = defaultdict(int)
    for answers in group:
        for answer in answers:
            unique_answers[answer] += 1
    return unique_answers


def puzzle1(groups: List[List[str]]) -> int:
    return sum(len(record_group_answers(group)) for group in groups)


def puzzle2(groups: List[List[str]]) -> int:
    sum_count_all = 0
    for group in groups:
        people_in_group = len(group)
        unique_answers = record_group_answers(group)
        count_all = sum(1 if unique_answers[answer] == people_in_group else 0 for answer in unique_answers)
        sum_count_all += count_all
    return sum_count_all


def main():
    groups = parse_input('input/day6.txt')
    puzzle1_result = puzzle1(groups)
    print(f'Puzzle 1: {puzzle1_result}')
    puzzle2_result = puzzle2(groups)
    print(f'Puzzle 2: {puzzle2_result}')


if __name__ == "__main__":
    main()
