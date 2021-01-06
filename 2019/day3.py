from typing import List


def parse_input(filename: str) -> (List[str], List[str]):
    return [line.strip().split(',') for line in open(filename).readlines()]


def get_wire_locations(wires: List[List[str]]) -> List[List[complex]]:
    locations = [[], []]

    d = {'R': -1, 'U': -1j, 'L': 1, 'D': 1j}

    for wire in range(2):
        pos = 0
        for section in wires[wire]:
            direction = section[0]
            steps = int(section[1:])
            for s in range(steps):
                pos += d[direction]
                locations[wire].append(pos)

    return locations


def part1(wires: List[List[str]]) -> int:
    locations = get_wire_locations(wires)
    crosses = set(locations[1]).intersection(set(locations[0]))
    return min(abs(int(c.real)) + abs(int(c.imag)) for c in crosses)


def part2(wires: List[List[str]]) -> int:
    locations = get_wire_locations(wires)
    crosses = list(set(locations[1]).intersection(set(locations[0])))
    return min(locations[0].index(cross) + locations[1].index(cross) + 2 for cross in crosses)


def main():
    wires = parse_input('input/day3.txt')
    print(f'Part 1: {part1(wires)}')
    print(f'Part 2: {part2(wires)}')


if __name__ == "__main__":
    main()
