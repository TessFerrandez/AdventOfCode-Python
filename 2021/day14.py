from collections import defaultdict


template, rules_lines = open('2021//input//day14.txt').read().split('\n\n')
rules = {pair: insert for pair, insert in (line.split(' -> ') for line in rules_lines.strip().split('\n'))}


def grow_polymer(template: str, steps: int) -> int:
    # record the frequency of each letter in the polymer
    pairs = defaultdict(int)
    for i in range(len(template) - 1):
        pairs[template[i: i + 2]] += 1

    # record the frequency of each pair in the polymer
    characters = defaultdict(int)
    for character in template:
        characters[character] += 1

    for _ in range(steps):
        new_pairs = defaultdict(int)

        # expand the pairs to add new characters
        # and record the frequency of each pair
        # in the new polymer for the next step
        for pair, count in pairs.items():
            new_character = rules[pair]
            characters[new_character] += count
            new_pairs[pair[0] + new_character] += count
            new_pairs[new_character + pair[1]] += count

        pairs = new_pairs

    return max(characters.values()) - min(characters.values())


print("Part 1:", grow_polymer(template, 10))
print("Part 2:", grow_polymer(template, 40))
