from collections import defaultdict
from queue import Queue
from math import ceil


def parse_ingredient(ingredient: str) -> dict:
    parts = ingredient.split()
    return {"ingredient": parts[1], "amount": int(parts[0])}


def parse_reactions(lines: list) -> dict:
    reactions = dict()
    for line in lines:
        inputs, result_str = line.split(" => ")
        ingredients = []
        for ingredient in inputs.split(", "):
            ingredients.append(parse_ingredient(ingredient))
        result = parse_ingredient(result_str)
        reactions[result["ingredient"]] = {
            "servings": result["amount"],
            "ingredients": ingredients,
        }
    return reactions


def make_fuel(amount: int, reactions: dict) -> int:
    supply = defaultdict(int)
    orders = Queue()

    orders.put({"ingredient": "FUEL", "amount": amount})
    ore_needed = 0

    while not orders.empty():
        order = orders.get()
        if order["ingredient"] == "ORE":
            ore_needed += order["amount"]
        elif order["amount"] <= supply[order["ingredient"]]:
            supply[order["ingredient"]] -= order["amount"]
        else:
            amount_needed = order["amount"] - supply[order["ingredient"]]
            reaction = reactions[order["ingredient"]]
            batches = ceil(amount_needed / reaction["servings"])
            for ingredient in reaction["ingredients"]:
                orders.put(
                    {
                        "ingredient": ingredient["ingredient"],
                        "amount": ingredient["amount"] * batches,
                    }
                )
                leftover_amount = batches * reaction["servings"] - amount_needed
                supply[order["ingredient"]] = leftover_amount

    return ore_needed


def puzzles():
    lines = [line.strip() for line in open("input/day14.txt").readlines()]
    reactions = parse_reactions(lines)
    ore_needed = make_fuel(1, reactions)
    print("ore:", ore_needed)

    upper_bound = None
    lower_bound = 1
    ore_capacity = 1000000000000

    while lower_bound + 1 != upper_bound:
        if upper_bound is None:
            guess = lower_bound * 2
        else:
            guess = (upper_bound + lower_bound) // 2

        ore_needed = make_fuel(guess, reactions)
        if ore_needed > ore_capacity:
            upper_bound = guess
        else:
            lower_bound = guess

    print("max fuel", lower_bound)


if __name__ == "__main__":
    puzzles()
