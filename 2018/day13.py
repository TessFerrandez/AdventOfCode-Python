"""
Solution from Shemetz https://www.reddit.com/r/adventofcode/comments/a5qd71/2018_day_13_solutions/

NOTE: instead of storing x and y, you can store the position as x + y * i (complex 1j in python)
Then you can set the direction as +1, +1j, -1 and -1j, and changing direction is simply multiplying direction with turn_direction
"""
from typing import List, Tuple, Dict
from collections import defaultdict


class Cart:
    def __init__(self, position: complex, direction: complex):
        self.position = position
        self.direction = direction
        self.cross_mod = 0
        self.dead = False

    def __repr__(self):
        return f"[{self.position}, {self.direction}, {self.cross_mod}, {self.dead}]"


def parse_input() -> Tuple[Dict[complex, str], List[Cart]]:
    with open("input/day13.txt") as f:
        input_file_lines = [line for line in f.readlines()]

    tracks = defaultdict(lambda: "")  # only store the important tracks: \ / +
    carts = []
    for y, line in enumerate(input_file_lines):
        for x, char in enumerate(line):
            if char == "\n":
                continue
            if char in "<v>^":
                direction = {"<": -1, "v": +1j, ">": +1, "^": -1j}[char]
                carts.append(Cart(x + y * 1j, direction))  # location, direction
                part = {"<": "-", "v": "|", ">": "-", "^": "|"}[char]
            else:
                part = char
            if part in "\\/+":
                tracks[(x + y * 1j)] = part
    return tracks, carts


def turn_cart(cart: Cart, part: str):
    """
    using downwards-facing Y axis, so all calculations must flip the imaginary bit
    eg. rotation to left = * -1j instead of * +1j
    """

    if not part:  # empty track (impossible) and | or - don't matter
        return
    if part == "\\":
        if cart.direction.real == 0:
            cart.direction *= -1j  # ⮡ ⮢
        else:
            cart.direction *= +1j  # ⮧ ⮤
    if part == "/":
        if cart.direction.real == 0:
            cart.direction *= +1j  # ⮣ ⮠
        else:
            cart.direction *= -1j  # ⮥ ⮦
    if part == "+":
        cart.direction *= -1j * 1j ** cart.cross_mod  # rotate left, forward, or right
        cart.cross_mod = (cart.cross_mod + 1) % 3


def puzzle1(tracks: Dict[complex, str], carts: List[Cart]) -> str:
    while True:
        carts.sort(key=lambda c: (c.position.imag, c.position.real))
        for ci, cart in enumerate(carts):
            cart.position += cart.direction
            if any(
                c2.position == cart.position
                for c2i, c2 in enumerate(carts)
                if c2i != ci
            ):
                return str(int(cart.position.real)) + "," + str(int(cart.position.imag))
            part = tracks[cart.position]
            turn_cart(cart, part)


def puzzle2(tracks: Dict[complex, str], carts: List[Cart]) -> str:
    while len(carts) > 1:
        carts.sort(key=lambda c: (c.position.imag, c.position.real))
        for ci, cart in enumerate(carts):
            if cart.dead:
                continue
            cart.position += cart.direction
            for ci2, cart2 in enumerate(carts):
                if ci != ci2 and cart.position == cart2.position and not cart2.dead:
                    cart.dead = True
                    cart2.dead = True
                    break
            if cart.dead:
                continue
            part = tracks[cart.position]
            turn_cart(cart, part)
        carts = [c for c in carts if not c.dead]
    if not carts:
        return "ERROR: there's an even number of carts, there's isn't 1 cart left at the end!"
    cart = carts[0]
    return str(int(cart.position.real)) + "," + str(int(cart.position.imag))


def main():
    tracks, carts = parse_input()
    puzzle1_answer = puzzle1(tracks, carts)
    print(f"Puzzle 1: {puzzle1_answer}")
    tracks, carts = parse_input()
    puzzle2_answer = puzzle2(tracks, carts)
    print(f"Puzzle 2: {puzzle2_answer}")


if __name__ == "__main__":
    main()
