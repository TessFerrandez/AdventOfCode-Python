from typing import List


class CrabCups:
    def __init__(self, cups):
        self.current = cups[0]
        self.next_cup = {}
        for i in range(len(cups)):
            try:
                self.next_cup[cups[i]] = cups[i + 1]
            except IndexError:
                self.next_cup[cups[i]] = cups[0]
        self.max = len(cups)

    def __str__(self):
        cup_str = f'({self.current}) '
        next_cup = self.next_cup[self.current]
        while next_cup != self.current:
            cup_str += str(next_cup) + ' '
            next_cup = self.next_cup[next_cup]
        return cup_str

    def play(self):
        # print(f'cups: {self}')

        # pick up 3 cups
        pickup = []
        current = self.current
        for i in range(3):
            current = self.next_cup[current]
            pickup.append(current)
        # print('pickup:', ', '.join([str(d) for d in pickup]))

        # remove the picked up cups
        next_cup = self.next_cup[current]
        self.next_cup[self.current] = next_cup

        # find the destination
        destination = self.current - 1
        while destination == 0 or destination in pickup:
            if destination == 0:
                destination = self.max
            else:
                destination -= 1
        # print(f'destination: {destination}')

        # place the pickup cups
        next_after_destination = self.next_cup[destination]
        self.next_cup[destination] = pickup[0]
        self.next_cup[pickup[2]] = next_after_destination

        # move forward
        self.current = self.next_cup[self.current]


def part1(cups: List[int]) -> str:
    crab_cups = CrabCups(cups)
    for move in range(100):
        # print(f'-- move {move + 1} --')
        crab_cups.play()

    cup_str = ''
    next_cup = crab_cups.next_cup[1]
    while next_cup != 1:
        cup_str += str(next_cup)
        next_cup = crab_cups.next_cup[next_cup]
    return cup_str


def part2(cups: List[int]) -> int:
    cups.extend(range(10, 1000001))
    crab_cups = CrabCups(cups)
    for move in range(10000000):
        # if move % 1000000 == 0:
        #    print(move)
        # print(f'-- move {move + 1} --')
        crab_cups.play()

    p1 = crab_cups.next_cup[1]
    p2 = crab_cups.next_cup[p1]
    return p1 * p2


def main():
    puzzle_input = '598162734'
    cups = [int(d) for d in puzzle_input]
    print(f'Part 1: {part1(cups)}')
    print(f'Part 2: {part2(cups)}')


if __name__ == "__main__":
    main()
