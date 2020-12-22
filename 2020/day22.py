from typing import List, Tuple
from collections import deque


def parse_input(filename: str):
    players = open(filename).read().split('\n\n')
    decks = []
    for player in players:
        decks.append([int(d) for d in player.split('\n')[1:]])
    return decks


def part1(decks: List[List[int]]) -> int:
    deck1, deck2 = decks
    deck1, deck2 = deque(deck1), deque(deck2)

    while deck1 and deck2:
        card1, card2 = deck1.popleft(), deck2.popleft()
        if card1 > card2:
            deck1.extend([card1, card2])
        else:
            deck2.extend([card2, card1])

    winning_deck = [card for card in deck1 + deck2]
    return sum((i + 1) * card for i, card in enumerate(winning_deck[::-1]))


def play_recursive(deck1: Tuple[int], deck2: Tuple[int]) -> (List[int], List[int]):
    rounds = set()
    while deck1 and deck2:
        # we've already seen this position in prev rounds
        # short circuiting by letting 1 win
        if deck1 in rounds:
            return deck1 + deck2, []

        rounds.add(deck1)

        card1, deck1 = deck1[0], deck1[1:]
        card2, deck2 = deck2[0], deck2[1:]

        # check if we can do a recursive game
        if card1 <= len(deck1) and card2 <= len(deck2):
            result1, result2 = play_recursive(deck1[:card1], deck2[:card2])
            if result1:
                deck1 += (card1, card2)
            else:
                deck2 += (card2, card1)
        # else - highest card wins
        else:
            if card1 > card2:
                deck1 += (card1, card2)
            else:
                deck2 += (card2, card1)
    return deck1, deck2


def part2(decks: List[List[int]]):
    deck1, deck2 = decks
    result1, result2 = play_recursive(tuple(deck1), tuple(deck2))
    winning_deck = result1 if result1 else result2
    return sum((i + 1) * card for i, card in enumerate(winning_deck[::-1]))


def main():
    decks = parse_input('input/day22.txt')
    print(decks)
    print(f'Part 1: {part1(decks)}')
    print(f'Part 2: {part2(decks)}')


if __name__ == "__main__":
    main()
