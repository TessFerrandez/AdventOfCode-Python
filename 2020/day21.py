from typing import List
from collections import defaultdict
from collections import OrderedDict


def parse_input(filename: str) -> List[List[str]]:
    meals = []
    lines = [line.strip() for line in open(filename).readlines()]

    for line in lines:
        ingredients, allergens = line.split('(')
        ingredients = ingredients.strip().split(' ')
        allergens = allergens.replace(')', '').replace('contains ', '').replace(',', '').split(' ')
        meals.append([ingredients, allergens])
    return meals


def intersection(lst1: List, lst2: List) -> List:
    return list(set(lst1).intersection(lst2))


def map_allergens(meals: List[List[str]]) -> dict:
    allergen_map = defaultdict(lambda: [])

    for ingredients, allergens in meals:
        for allergen in allergens:
            allergen_map[allergen].append(ingredients)
    return dict(allergen_map)


def solve_allergens(allergens: dict) -> dict:
    possible = {}
    solved_allergens = {}

    for allergen in allergens:
        ingredients = allergens[allergen]
        lst1 = ingredients.pop(0)
        while ingredients:
            lst2 = ingredients.pop(0)
            lst1 = intersection(lst1, lst2)
        possible[allergen] = lst1

    while possible:
        solved = [allergen for allergen in possible if len(possible[allergen]) == 1]
        for allergen in solved:
            ingredient = possible[allergen][0]
            solved_allergens[allergen] = ingredient
            for a in possible:
                if ingredient in possible[a]:
                    possible[a].remove(ingredient)
            del possible[allergen]

    return solved_allergens


def part1(meals: List[List[str]], allergens: dict) -> int:
    allergy_inducing_ingredients = [allergens[allergen] for allergen in allergens]

    sum_inert = 0
    for ingredients, _ in meals:
        for ingredient in ingredients:
            if ingredient not in allergy_inducing_ingredients:
                sum_inert += 1
    return sum_inert


def part2(allergens: dict) -> str:
    ordered_allergens = OrderedDict(sorted(allergens.items()))
    result = ''
    for allergen in ordered_allergens:
        result += ordered_allergens[allergen] + ','
    return result[:-1]


def main():
    meals = parse_input('input/day21.txt')
    allergens = map_allergens(meals)
    allergens = solve_allergens(allergens)
    print(f'Part 1: {part1(meals, allergens)}')
    print(f'Part 2: {part2(allergens)}')


if __name__ == "__main__":
    main()
