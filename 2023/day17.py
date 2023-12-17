# dijkstra, heap, pathfinding, shortest path, state space search
# based on snhansen's solution
from input_processing import read_data
from heapq import heappush, heappop


def parse(data):
    rows = data.splitlines()
    n_cols, n_rows = len(rows[0]), len(rows)
    grid = {(c + r * 1j): int(ch) for r, row in enumerate(rows) for c, ch in enumerate(row)}
    end = (n_cols - 1) + (n_rows - 1) * 1j
    return grid, end


def part1(grid, end):
    # state = (heat, id (for sorting), position, direction, stretch)
    queue = [(grid[pos], id(pos), pos, pos, 1) for pos in [1, 1j]]
    seen = set()

    while queue:
        heat, _, pos, direction, stretch = heappop(queue)

        if (pos, direction, stretch) in seen:
            continue

        seen.add((pos, direction, stretch))

        if pos == end:
            return heat

        dirs = [direction * 1j, -direction * 1j]

        # turn
        for new_dir in dirs:
            new_pos = pos + new_dir
            if new_pos in grid:
                heappush(queue, (heat + grid[new_pos], id(new_pos), new_pos, new_dir, 1))

        # if moved less than 3 blocks, we can continue in the same direction
        if stretch < 3:
            new_pos = pos + direction
            if new_pos in grid:
                heappush(queue, (heat + grid[new_pos], id(new_pos), new_pos, direction, stretch + 1))


def part2(grid, end):
    # state = (heat, id (for sorting), position, direction, stretch)
    queue = [(grid[pos], id(pos), pos, pos, 1) for pos in [1, 1j]]
    seen = set()

    while queue:
        heat, _, pos, direction, stretch = heappop(queue)

        if (pos, direction, stretch) in seen:
            continue

        seen.add((pos, direction, stretch))

        if pos == end and stretch >= 4:
            return heat

        # if moved less than 10 blocks we can continue
        if stretch < 10:
            new_pos = pos + direction
            if new_pos in grid:
                heappush(queue, (heat + grid[new_pos], id(new_pos), new_pos, direction, stretch + 1))

        # if moved at least 4 blocks, we can turn
        if stretch >= 4:
            dirs = [direction * 1j, -direction * 1j]

            # turn
            for new_dir in dirs:
                new_pos = pos + new_dir
                if new_pos in grid:
                    heappush(queue, (heat + grid[new_pos], id(new_pos), new_pos, new_dir, 1))


def test():
    sample = '''2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533'''
    grid, end = parse(sample)
    assert part1(grid, end) == 102
    assert part2(grid, end) == 94


test()
data = read_data(2023, 17)
grid, end = parse(data)
print('Part1:', part1(grid, end))
print('Part2:', part2(grid, end))
