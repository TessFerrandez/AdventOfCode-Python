import re
from input_processing import read_data


def parse_card(card_row):
    card, numbers = card_row.split(': ')
    card_number = int(card.split(' ')[-1])
    winning_numbers, card_numbers = numbers.split(' | ')
    winning_numbers = set(int(number) for number in re.findall(r'\d+', winning_numbers))
    card_numbers = set(int(number) for number in re.findall(r'\d+', card_numbers))
    return card_number, winning_numbers, card_numbers


def parse(data):
    card_rows = data.splitlines()
    return [parse_card(card_row) for card_row in card_rows]


def part1(cards):
    num_winning_by_card = [len(winning_numbers & card_numbers) for _, winning_numbers, card_numbers in cards]
    return sum(2 ** (num_winning - 1) for num_winning in num_winning_by_card if num_winning > 0)


def part2(cards):
    num_winning_by_card = [len(winning_numbers & card_numbers) for _, winning_numbers, card_numbers in cards]
    n = len(cards)
    num_cards = [1 for _ in range(n)]

    for i, num_winning in enumerate(num_winning_by_card):
        for j in range(i + 1, i + num_winning + 1):
            if j < n:
                num_cards[j] += num_cards[i]

    return sum(num_cards)


def test():
    sample = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''
    cards = parse(sample)
    assert part1(cards) == 13
    assert part2(cards) == 30


test()
data = read_data(2023, 4)
print('Part1:', part1(parse(data)))
print('Part2:', part2(parse(data)))
