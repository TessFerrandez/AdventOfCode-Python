from collections import defaultdict
from itertools import permutations


def parse_input(filename: str) -> dict:
    rules = defaultdict(dict)
    lines = [line.strip() for line in open(filename).readlines()]

    for line in lines:
        parts = line.split(' ')
        person1 = parts[0]
        person2 = parts[10][:-1]
        happiness = int(parts[3]) if parts[2] == 'gain' else -int(parts[3])
        rules[person1][person2] = happiness
    return rules


def calculate_happines(rules: dict) -> int:
    people = rules.keys()
    arrangements = permutations(people)
    max_happiness = 0
    for arrangement in arrangements:
        happiness = 0
        for i in range(len(arrangement) - 1):
            happiness += rules[arrangement[i]][arrangement[i + 1]]
            happiness += rules[arrangement[i + 1]][arrangement[i]]
        happiness += rules[arrangement[-1]][arrangement[0]]
        happiness += rules[arrangement[0]][arrangement[-1]]
        max_happiness = max(max_happiness, happiness)
    return max_happiness


def part1(rules: dict) -> int:
    return calculate_happines(rules)


def part2(rules: dict) -> int:
    people = list(rules.keys())
    for person in people:
        rules[person]['me'] = 0
    for person in people:
        rules['me'][person] = 0
    return calculate_happines(rules)


def main():
    rules = parse_input('input/day13.txt')
    print(f'Part 1: {part1(rules)}')
    print(f'Part 2: {part2(rules)}')


if __name__ == "__main__":
    main()
