from dataclasses import dataclass
from typing import Set, Tuple
from input_processing import read_data


@dataclass
class Grid:
    # data is offset (top left = -1, -1)
    # to allow for easy mod
    target: Tuple[int]
    start: Tuple[int]
    walls: Set[Tuple[int]]
    lefts: Set[Tuple[int]]
    rights: Set[Tuple[int]]
    ups: Set[Tuple[int]]
    downs: Set[Tuple[int]]
    width: int
    height: int

    def __init__(self, data) -> None:
        data = data.splitlines()
        self.height, self.width = len(data) - 2, len(data[0]) - 2

        self.start = (-1, 0)
        self.target = (self.height, self.width - 1)

        self.walls = set()
        self.downs = set()
        self.ups = set()
        self.lefts = set()
        self.rights = set()

        for r, row in enumerate(data):
            for c, ch in enumerate(row):
                pos = (r - 1, c - 1)
                if ch == '#':
                    self.walls.add(pos)
                elif ch == '>':
                    self.rights.add(pos)
                elif ch == '<':
                    self.lefts.add(pos)
                elif ch == '^':
                    self.ups.add(pos)
                elif ch == 'v':
                    self.downs.add(pos)

        # block tile above start
        self.walls.add((-2, 0))
        # block tile below end
        self.walls.add((self.height + 1, self.width - 1))

    def move_winds(self):
        self.lefts = set((row, (col - 1) % self.width) for row, col in self.lefts)
        self.rights = set((row, (col + 1) % self.width) for row, col in self.rights)
        self.ups = set(((row - 1) % self.height, col) for row, col in self.ups)
        self.downs = set(((row + 1) % self.height, col) for row, col in self.downs)

    def find_moves(self, pos):
        row, col = pos

        moves = set()

        for new_pos in (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1), (row, col):
            if new_pos not in self.walls and \
               new_pos not in self.lefts and \
               new_pos not in self.rights and \
               new_pos not in self.ups and \
               new_pos not in self.downs:
                moves.add(new_pos)

        return moves


def parse(data):
    return Grid(data)


def find_shortest_path(grid: Grid):
    moves = set([grid.start])
    minutes = 0

    while grid.target not in moves:
        new_moves = set()

        grid.move_winds()
        for pos in moves:
            new_moves |= grid.find_moves(pos)

        moves = new_moves
        minutes += 1

    return minutes


def part1(grid: Grid):
    return find_shortest_path(grid)


def part2(grid, first_route):
    grid.start, grid.target = grid.target, grid.start
    back_to_start = find_shortest_path(grid)
    grid.start, grid.target = grid.target, grid.start
    back_to_end_again = find_shortest_path(grid)

    return first_route + back_to_start + back_to_end_again


def test():
    sample = """#.#####
#.....#
#>....#
#.....#
#...v.#
#.....#
#####.#"""
    grid = parse(sample)
    first_route = part1(grid)
    assert first_route == 18
    assert part2(grid, first_route) == 54


test()
grid = parse(read_data(2022, 23))
first_route = part1(grid)
print('Part1:', first_route)
print('Part2:', part2(grid, first_route))
