from input_processing import read_data
from functools import cmp_to_key
from collections import Counter


def hand_value(hand):
    card_counts = Counter(hand).most_common(2)
    if card_counts[0][1] == 5:
        return 6
    if card_counts[0][1] == 4:
        return 5
    if card_counts[0][1] == 3:
        if card_counts[1][1] == 2:
            return 4
        return 3
    if card_counts[0][1] == 2:
        if card_counts[1][1] == 2:
            return 2
        return 1
    return 0


def card_values(hand):
    cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return [cards[card] for card in hand]


def hand_value_with_jokers(hand):
    jokers = Counter(hand)['J']
    hand_no_jokers = hand.replace('J', '')
    card_counts = Counter(hand_no_jokers).most_common()
    if len(card_counts) == 0:
        return 6    # all jokers
    if card_counts[0][1] + jokers == 5:
        return 6
    if card_counts[0][1] + jokers == 4:
        return 5
    if card_counts[0][1] + jokers == 3:
        if card_counts[1][1] == 2:
            return 4
        return 3
    if card_counts[0][1] + jokers == 2:
        if card_counts[1][1] == 2:
            return 2
        return 1
    return 0


def card_values_with_jokers(hand):
    cards_w_joker = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'Q': 12, 'K': 13, 'A': 14}
    return [cards_w_joker[card] for card in hand]


def parse(data):
    hands = [line.split(' ') for line in data.splitlines()]
    return [[hand, int(bid)] for hand, bid in hands]


def part1(hands):
    sorted_hands = sorted(hands, key=lambda hand: (hand_value(hand[0]), card_values(hand[0])))
    return sum(i * hand[1] for i, hand in enumerate(sorted_hands, start=1))


def part2(hands):
    sorted_hands = sorted(hands, key=lambda hand: (hand_value_with_jokers(hand[0]), card_values_with_jokers(hand[0])))
    return sum(i * hand[1] for i, hand in enumerate(sorted_hands, start=1))


def test():
    sample = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''
    part1(parse(sample)) == 6440
    part2(parse(sample)) == 5905


test()
data = read_data(2023, 7)
print('Part1:', part1(parse(data)))
print('Part2:', part2(parse(data)))
