# based on solution from jfb1337
from functools import cache

polymer, rules_lines = open('2021//input//day14.txt').read().split('\n\n')
rules = {pair: insert for pair, insert in (line.split(' -> ') for line in rules_lines.strip().split('\n'))}


@cache
# cache saves the result of the function,
# so we don't recalculate the result of seen pairs
def count(character, polymer, steps):
    if steps == 0:
        return polymer.count(character)

    total = 0
    # for all pairs in the polymer
    # calculate the frequency of the character in the expansion
    # and add to the total
    for a, b in zip(polymer, polymer[1:]):
        acb = a + rules[a + b] + b
        total += count(character, acb, steps - 1)
        # don't double count the last character in the pair
        total -= (b == character)

    # finally add on the last character in the polymer
    total += (b == character)

    return total


def answer(steps):
    all_characters = set(polymer)
    c = [count(character, polymer, steps) for character in all_characters]
    return max(c) - min(c)


print("Part 1:", answer(10))
print("Part 2:", answer(40))
