from collections import defaultdict
from input_processing import read_data


ALL = [-1, 1, 1j, -1j, -1 - 1j, -1 + 1j, 1 - 1j, 1 + 1j]
NORTH = [-1 - 1j, -1, -1 + 1j]
SOUTH = [1 - 1j, 1, 1 + 1j]
WEST = [-1 - 1j, -1j, 1 - 1j]
EAST = [-1 + 1j, 1j, 1 + 1j]


def parse(data):
    return set([r + c * 1j for r, row in enumerate(data.splitlines())
                for c, ch in enumerate(row) if ch == '#'])


def part1(elves):
    directions = [NORTH, SOUTH, WEST, EAST]

    for _ in range(10):
        proposed_moves = defaultdict(list)

        for elf in elves:
            if not any(elf + diff in elves for diff in ALL):
                continue
            for direction in directions:
                if not any(elf + diff in elves for diff in direction):
                    proposed_moves[elf + direction[1]].append(elf)
                    break

        for move in proposed_moves:
            if len(proposed_moves[move]) == 1:
                elves.remove(proposed_moves[move][0])
                elves.add(move)

        directions = directions[1:] + directions[:1]

    min_col = min(elf.imag for elf in elves)
    max_col = max(elf.imag for elf in elves)
    min_row = min(elf.real for elf in elves)
    max_row = max(elf.real for elf in elves)
    area = int((max_col - min_col + 1) * (max_row - min_row + 1))
    return area - len(elves)


def part2(elves):
    directions = [NORTH, SOUTH, WEST, EAST]

    round = 1
    while True:
        proposed_moves = defaultdict(list)

        for elf in elves:
            if not any(elf + diff in elves for diff in ALL):
                continue
            for direction in directions:
                if not any(elf + diff in elves for diff in direction):
                    proposed_moves[elf + direction[1]].append(elf)
                    break

        if not proposed_moves:
            return round

        for move in proposed_moves:
            if len(proposed_moves[move]) == 1:
                elves.remove(proposed_moves[move][0])
                elves.add(move)

        directions = directions[1:] + directions[:1]
        round += 1


def test():
    sample = """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#.."""
    assert part1(parse(sample)) == 110


test()
data = read_data(2022, 23)
print('Part1:', part1(parse(data)))
print('Part2:', part2(parse(data)))
