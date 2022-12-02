from collections import defaultdict
from typing import DefaultDict
from math import ceil


reactions = {
    "FUEL": (1, [(7, "A"), (1, "E")]),
    "E": (1, [(7, "A"), (1, "D")]),
    "D": (1, [(7, "A"), (1, "C")]),
    "C": (1, [(7, "A"), (1, "B")]),
    "B": (1, [(1, "ORE")]),
    "A": (10, [(10, "ORE")]),
}


def make_reactions():
    reactions = {}
    lines = [line.strip() for line in open('2019/input/day14.txt').readlines()]

    for line in lines:
        required, made = line.split(' => ')
        required = required.split(', ')
        made_amt, chem_made = made.split(' ')
        made_amt = int(made_amt)
        required = [(int(req.split(' ')[0]), req.split(' ')[1]) for req in required]
        reactions[chem_made] = (made_amt, required)

    return reactions


def make_fuel(reactions, fuel_needed):
    available: DefaultDict[str, int] = defaultdict(lambda: 0)
    ore_needed = 0

    todo = [(fuel_needed, "FUEL")]

    while todo:
        amt_needed, chemical = todo.pop()

        if chemical == "ORE":
            ore_needed += amt_needed
            continue

        # take what we can from available
        amt_available = min(amt_needed, available[chemical])
        amt_needed -= amt_available
        available[chemical] -= amt_available

        if amt_needed == 0:
            continue

        # add the new reactions needed on the todo list
        amt_produced, chem_needed = reactions[chemical]
        reactions_needed = ceil(amt_needed / amt_produced)
        extra = (reactions_needed * amt_produced) - amt_needed
        for chem in chem_needed:
            amt, ch = chem
            todo.append((amt * reactions_needed, ch))

        available[chemical] += extra

    return ore_needed


reactions = make_reactions()

# PART 1
ore_used = make_fuel(reactions, 1)

print("Part 1:", ore_used)

# PART 2
upper_bound, lower_bound = None, 1

while lower_bound + 1 != upper_bound:
    if upper_bound is None:
        guess = lower_bound * 2
    else:
        guess = (upper_bound + lower_bound) // 2
    ore_used = make_fuel(reactions, guess)
    if ore_used > 1000000000000:
        upper_bound = guess
    else:
        lower_bound = guess

print("Part 2:", lower_bound)
