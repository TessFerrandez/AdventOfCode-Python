from typing import List
from collections import Counter


def parse_input(filename: str) -> List[str]:
    return [line.strip() for line in open(filename).readlines()]


def part1(box_ids: List[str]) -> int:
    two_counts = 0
    three_counts = 0

    for box_id in box_ids:
        counts = Counter(box_id)
        if 2 in counts.values():
            two_counts += 1
        if 3 in counts.values():
            three_counts += 1
    return two_counts * three_counts


def diff_by_one(str1: str, str2: str) -> str:
    result = ''
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if result != '':
                return ''
            result = str1[:i] + str1[i + 1:]
    return result


def part2(box_ids: List[str]) -> str:
    for box_id in box_ids:
        for other in box_ids:
            if other == box_id:
                continue
            result = diff_by_one(box_id, other)
            if result != '':
                return result
    return ''


def main():
    box_ids = parse_input('input/day2.txt')
    print(f'Part 1: {part1(box_ids)}')
    print(f'Part 2: {part2(box_ids)}')


if __name__ == "__main__":
    main()
