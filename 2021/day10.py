from typing import List
from functools import reduce


sub_systems = [line.strip() for line in open('2021//input//day10.txt', 'r').readlines()]
matching = {"(": ")", "[": "]", "{": "}", "<": ">"}
score = {")": 3, "]": 57, "}": 1197, ">": 25137}


def find_illegal_chars(sub_system: str) -> str:
    open = []
    for ch in sub_system:
        if ch in matching:
            open.append(ch)
        elif len(open) > 0 and matching[open[-1]] == ch:
            open.pop()
        else:
            return ch
    return ""


def get_missing_chars(sub_system: str) -> str:
    open = []
    for ch in sub_system:
        if ch in matching:
            open.append(ch)
        elif len(open) > 0 and matching[open[-1]] == ch:
            open.pop()
        else:
            return ""

    return "".join([matching[open[-i]] for i in range(1, len(open) + 1)])


def calculate_missing_score(missing: str) -> int:
    ch_scores = {")": 1, "]": 2, "}": 3, ">": 4}
    return reduce(lambda score, ch_score: score * 5 + ch_score, [ch_scores[ch] for ch in missing])


def get_middle_missing_score(sub_systems: List[str]) -> int:
    missing_scores = []
    for sub_system in sub_systems:
        missing = get_missing_chars(sub_system)
        if missing:
            missing_scores.append(calculate_missing_score(missing))
    missing_scores.sort()
    return missing_scores[len(missing_scores) // 2]


print("Part 1:", sum(score[ch] for ch in "".join([find_illegal_chars(sub_system) for sub_system in sub_systems])))
print("Part 2:", get_middle_missing_score(sub_systems))
