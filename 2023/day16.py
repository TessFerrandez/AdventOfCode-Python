from collections import deque
from input_processing import read_data


def parse(data):
    grid = {}
    rows = data.splitlines()

    for r, row in enumerate(rows):
        for c, slot in enumerate(row):
            grid[r + c * 1j] = slot

    return grid, len(rows), len(rows[0])


RIGHT = 1j
LEFT = -1j
UP = -1
DOWN = 1


def energize(grid, start, direction):
    visited = set()
    rays = deque([(start, direction)])

    while rays:
        pos, direction = rays.popleft()

        if pos not in grid:
            continue

        if (pos, direction) in visited:
            continue

        visited.add((pos, direction))

        if grid[pos] == '.':
            rays.append((pos + direction, direction))
        elif grid[pos] == '|' and direction in (UP, DOWN):
            rays.append((pos + direction, direction))
        elif grid[pos] == '-' and direction in (LEFT, RIGHT):
            rays.append((pos + direction, direction))
        elif grid[pos] == '|':
            rays.append((pos + UP, UP))
            rays.append((pos + DOWN, DOWN))
        elif grid[pos] == '-':
            rays.append((pos + LEFT, LEFT))
            rays.append((pos + RIGHT, RIGHT))
        elif grid[pos] == '\\':
            if direction == LEFT:
                rays.append((pos + UP, UP))
            elif direction == RIGHT:
                rays.append((pos + DOWN, DOWN))
            elif direction == DOWN:
                rays.append((pos + RIGHT, RIGHT))
            else:
                rays.append((pos + LEFT, LEFT))
        elif grid[pos] == '/':
            if direction == LEFT:
                rays.append((pos + DOWN, DOWN))
            elif direction == RIGHT:
                rays.append((pos + UP, UP))
            elif direction == DOWN:
                rays.append((pos + LEFT, LEFT))
            else:
                rays.append((pos + RIGHT, RIGHT))

    positions = set([pos for pos, _ in visited])
    return len(positions)


def part1(grid):
    return energize(grid, 0, RIGHT)


def part2(grid, rows, cols):
    max_energy = 0

    for c in range(cols):
        energy = energize(grid, c * 1j, DOWN)
        max_energy = max(max_energy, energy)
        energy = energize(grid, rows - 1 + c * 1j, UP)
        max_energy = max(max_energy, energy)

    for r in range(rows):
        energy = energize(grid, r, RIGHT)
        max_energy = max(max_energy, energy)
        energy = energize(grid, r + (cols - 1) * 1j, LEFT)
        max_energy = max(max_energy, energy)

    return max_energy


def test():
    sample = '''.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....'''
    grid, rows, cols = parse(sample)
    assert part1(grid) == 46
    assert part2(grid, rows, cols) == 51


test()
data = read_data(2023, 16)
grid, rows, cols = parse(data)
print('Part1:', part1(grid))
print('Part2:', part2(grid, rows, cols))
