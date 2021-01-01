def parse_input(filename: str) -> (str, dict):
    lines = [line.strip() for line in open(filename).readlines()]
    initial = lines[0][15:]

    rules = {}
    for line in lines[2:]:
        before, after = line.split(' => ')
        rules[before] = after

    return initial, rules


def apply_rules(pots: str, rules: dict) -> str:
    original = pots
    for i in range(len(original) - 5):
        if original[i: i + 5] in rules:
            pots = pots[: i + 2] + rules[original[i: i + 5]] + pots[i + 3:]
        else:
            pots = pots[: i + 2] + '.' + pots[i + 3:]
    return pots


def part1(initial: str, rules: dict) -> int:
    pots = ('.' * 3) + initial + ('.' * 30)
    for i in range(20):
        pots = apply_rules(pots, rules)
        # print(pots)

    pot_sum = 0
    for i in range(len(pots)):
        if pots[i] == '#':
            pot_sum += i - 3
    return pot_sum


def count_pots(pots: str):
    pot_sum = 0
    for i in range(len(pots)):
        if pots[i] == '#':
            pot_sum += i - 3
    return pot_sum


def part2(initial: str, rules: dict) -> int:
    # from iteration 91 and forward it just repeats
    # moving one step forward

    # calculate pots 0-90
    pots = ('.' * 3) + initial + ('.' * 300)
    for i in range(90):
        pots = apply_rules(pots, rules)

    # check diff between two consecutive
    print(90, count_pots(pots), pots)
    pots = apply_rules(pots, rules)
    sum91 = count_pots(pots)
    print(91, sum91, pots)
    pots = apply_rules(pots, rules)
    sum92 = count_pots(pots)
    print(92, sum92, pots)

    # calculate what the value would be for 50 billion
    diff = sum92 - sum91
    fifty_bill = (50000000000 - 91) * diff + sum91

    return fifty_bill


def main():
    initial, rules = parse_input('input/day12.txt')
    print(f'Part 1: {part1(initial, rules)}')
    print(f'Part 2: {part2(initial, rules)}')


if __name__ == "__main__":
    main()
