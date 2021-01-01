from typing import List
from collections import Counter, defaultdict

LEFT = 0
STRAIGHT = 1
RIGHT = 2


class Cart:
    def __init__(self, position: complex, direction: complex):
        self.position = position
        self.direction = direction
        self.next_turn = LEFT
        self.dead = False

    def rotate(self, track):
        if not track:
            return
        if track == '\\':
            if self.direction.real == 0:
                self.direction *= -1j
            else:
                self.direction *= 1j
        if track == '/':
            if self.direction.real == 0:
                self.direction *= 1j
            else:
                self.direction *= -1j
        if track == '+':
            self.direction *= -1j * 1j ** self.next_turn
            self.next_turn = (self.next_turn + 1) % 3


def parse_input(filename: str) -> (dict, List[Cart]):
    lines = [line.replace('\n', '') for line in open(filename).readlines()]
    carts = []
    rails = defaultdict(lambda: '')
    for y, line in enumerate(lines):
        for x, track in enumerate(line):
            if track in '><^v':
                direction = {'>': 1, '<': -1, '^': -1j, 'v': 1j}[track]
                carts.append(Cart(x + y * 1j, direction))
            if track in r'\+//':
                rails[x + y * 1j] = track
    return rails, carts


def part1(rails: dict, carts: List[Cart]) -> str:
    while True:
        carts.sort(key=lambda c: (c.position.imag, c.position.real))
        for ci, cart in enumerate(carts):
            cart.position += cart.direction
            if any(c2.position == cart.position for c2i, c2 in enumerate(carts) if c2i != ci):
                return str(int(cart.position.real)) + ',' + str(int(cart.position.imag))
            track = rails[cart.position]
            cart.rotate(track)


def part2(rails: dict, carts: List[Cart]) -> str:
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
            track = rails[cart.position]
            cart.rotate(track)
        carts = [c for c in carts if not c.dead]
    cart = carts[0]
    return str(int(cart.position.real)) + ',' + str(int(cart.position.imag))


def main():
    rails, carts = parse_input('input/day13.txt')
    print(f'Part 1: {part1(rails, carts)}')
    rails, carts = parse_input('input/day13.txt')
    print(f'Part 2: {part2(rails, carts)}')


if __name__ == "__main__":
    main()
