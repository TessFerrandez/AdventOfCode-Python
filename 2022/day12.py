from input_processing import read_data
from collections import deque


def parse(data):
    rows = data.splitlines()
    grid = {}
    for r, row in enumerate(rows):
        for c, ch in enumerate(row):
            if ch == 'S':
                start = (r, c)
                grid[r, c] = ord('a')
            elif ch == 'E':
                end = (r, c)
                grid[r, c] = ord('z')
            else:
                grid[r, c] = ord(ch)
    return grid, start, end


def part1(grid, start, end):
    visited = set([start])
    queue = deque([(start, 0)])

    while queue:
        pos, steps = queue.popleft()
        if pos == end:
            return steps
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = pos[0] + dr, pos[1] + dc
            if new_pos in visited:
                continue
            if new_pos not in grid:
                continue
            if grid[new_pos] > grid[pos] + 1:
                continue
            visited.add(new_pos)
            queue.append((new_pos, steps + 1))


def part2(grid, start, end):
    """
    start at end, find the shortest path to any a
    only allow paths where the neighbor is >= current - 1
    """
    visited = set([end])
    queue = deque([(end, 0)])

    while queue:
        pos, steps = queue.popleft()
        if grid[pos] == ord('a'):
            return steps
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = pos[0] + dr, pos[1] + dc
            if new_pos in visited:
                continue
            if new_pos not in grid:
                continue
            if grid[new_pos] < grid[pos] - 1:
                continue
            visited.add(new_pos)
            queue.append((new_pos, steps + 1))


def test():
    sample = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
    grid, start, end = parse(sample)
    assert part1(grid, start, end) == 31
    assert part2(grid, start, end) == 29


test()
grid, start, end = parse(read_data(2022, 12))
print('Part1:', part1(grid, start, end))
print('Part2:', part2(grid, start, end))
