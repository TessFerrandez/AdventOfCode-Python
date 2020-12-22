from typing import List, Tuple


def parse_input(filename: str) -> List[Tuple[int, int, int]]:
    discs = []
    lines = [line.strip().split() for line in open(filename).readlines()]
    for line in lines:
        disc = (int(line[1][1:]), int(line[3]), int(line[11][:-1]))
        discs.append(disc)
    return discs


def disc_in_position(disc: Tuple[int, int, int], time) -> bool:
    disc_num, positions, position = disc
    return (disc_num + position + time) % positions == 0


def falls_through(discs: List[Tuple[int, int, int]], time: int) -> bool:
    for disc in discs:
        if not disc_in_position(disc, time):
            return False
    return True


def part1(discs: List[Tuple[int, int, int]]) -> int:
    time = 0
    while True:
        time += 1
        if falls_through(discs, time):
            return time


def main():
    discs = parse_input('input/day15.txt')
    print(f'Part 1: {part1(discs)}')
    discs.append((7, 11, 0))
    print(f'Part 2: {part1(discs)}')


if __name__ == "__main__":
    main()
