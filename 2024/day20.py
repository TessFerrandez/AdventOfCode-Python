from collections import defaultdict
from input_processing import read_data


def parse(data):
    grid = set()
    for y, row in enumerate(data.splitlines()):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                end = (x, y)
            if cell in 'SE.':
                grid.add((x, y))
    return grid, start, end


def get_grid_steps(grid, start, end):
    grid_steps = {start: 0}
    queue = [(start, 0)]

    while queue:
        (x, y), steps = queue.pop()
        if (x, y) == end:
            grid_steps[(x, y)] = steps
            break
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) in grid and (new_x, new_y) not in grid_steps:
                grid_steps[(new_x, new_y)] = steps + 1
                queue.append(((new_x, new_y), steps + 1))

    return grid_steps


def part1(grid, start, end):
    grid_steps = get_grid_steps(grid, start, end)
    saved = defaultdict(int)

    for (x, y) in grid_steps:
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            next_x, next_y = new_x + dx, new_y + dy
            if (new_x, new_y) not in grid_steps and (next_x, next_y) in grid_steps:
                steps_saved = grid_steps[(next_x, next_y)] - grid_steps[(x, y)] - 2
                if steps_saved > 0:
                    saved[steps_saved] += 1

    return sum(saved[steps_saved] for steps_saved in saved if steps_saved >= 100)


def part2(grid, start, end, min_saved):
    grid_steps = get_grid_steps(grid, start, end)
    steps = {grid_steps[pos]: pos for pos in grid_steps}
    max_steps = max(grid_steps.values())
    saved = defaultdict(int)
    for s1 in range(max_steps, min_saved + 2, -1):
        for s2 in range(0, s1 - min_saved - 1):
            x1, y1 = steps[s1]
            x2, y2 = steps[s2]
            cheat = abs(x1 - x2) + abs(y1 - y2)
            if cheat > 20:
                continue
            steps_saved = s1 - s2 - cheat
            if steps_saved >= min_saved:
                saved[steps_saved] += 1
    return sum(saved[steps_saved] for steps_saved in saved)


def test():
    data = '''###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############'''
    grid, start, end = parse(data)
    assert part1(grid, start, end) == 0
    assert part2(grid, start, end, 50) == 285


test()
data = read_data(2024, 20)
grid, start, end = parse(data)
print('Part1:', part1(grid, start, end))
print('Part2:', part2(grid, start, end, 100))
