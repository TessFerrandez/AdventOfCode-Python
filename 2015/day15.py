import pytest
from common.helpers import extract_numbers
from typing import List


@pytest.mark.parametrize('data, expected', [([[-1, -2, 6, 3, 8], [2, 3, -2, -1, 3]], 62842880)])
def test_part1(data: List[List[int]], expected: int):
    assert part1(data) == expected


@pytest.mark.parametrize('data, expected', [([[-1, -2, 6, 3, 8], [2, 3, -2, -1, 3]], 57600000)])
def test_part2(data: List[List[int]], expected: int):
    assert part2(data) == expected


def parse_input(filename: str) -> List[List[int]]:
    lines = [line.strip() for line in open(filename).readlines()]
    ingredients = [extract_numbers(line) for line in lines]
    return ingredients


def mixtures(n: int, total: int):
    if n == 1:
        start = total
    else:
        start = 0

    for i in range(start, total + 1):
        left = total - i
        if n - 1:
            for y in mixtures(n - 1, left):
                yield [i] + y
        else:
            yield [i]


def get_score(spoons, ingredients, restrict_calories=False) -> int:
    n_items = len(spoons)

    if restrict_calories:
        calorie_count = 0
        for ingredient in range(n_items):
            calorie_count += spoons[ingredient] * ingredients[ingredient][4]
        if calorie_count != 500:
            return 0

    total_score = 1
    for prop in range(4):
        score = 0
        for ingredient in range(n_items):
            score += spoons[ingredient] * ingredients[ingredient][prop]
        score = max(score, 0)
        total_score *= score
    return total_score


def part1(ingredients: List[List[int]]) -> int:
    max_score = 0
    n_ingredients = len(ingredients)
    for mixture in mixtures(n_ingredients, 100):
        max_score = max(max_score, get_score(mixture, ingredients))
    return max_score


def part2(ingredients: List[List[int]]) -> int:
    max_score = 0
    n_ingredients = len(ingredients)
    for mixture in mixtures(n_ingredients, 100):
        max_score = max(max_score, get_score(mixture, ingredients, True))
    return max_score


def main():
    ingredients = parse_input('input/day15.txt')
    print(ingredients)
    print(f'Part 1: {part1(ingredients)}')
    print(f'Part 2: {part2(ingredients)}')


if __name__ == "__main__":
    main()
