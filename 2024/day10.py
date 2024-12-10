from collections import defaultdict
from input_processing import read_data, get_numbers_from_lines


def parse(data):
    grid = defaultdict(int)
    data = data.splitlines()
    for r, row in enumerate(data):
        for c, num in enumerate(row):
            grid[(r, c)] = int(num)
    return grid, len(data[0]), len(data)


def part1(grid, width, height):
    def find_paths(pos):
        end_positions = set()
        level = 0
        queue = [(pos, level)]
        while queue:
            pos, level = queue.pop()
            if level == 9:
                end_positions.add(pos)
            else:
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    new_pos = (pos[0] + dx, pos[1] + dy)
                    if new_pos in grid and grid[new_pos] == level + 1 and (new_pos, level + 1) not in queue:
                        queue.append((new_pos, level + 1))
        return len(end_positions)

    starts = [pos for pos, elevation in grid.items() if elevation == 0]
    paths = 0
    for start in starts:
        paths += find_paths(start)
    return paths


def part2(grid, width, height):
    def find_paths(pos):
        num_paths = 0
        level = 0
        queue = [(pos, level)]
        while queue:
            pos, level = queue.pop()
            if level == 9:
                num_paths += 1
            else:
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    new_pos = (pos[0] + dx, pos[1] + dy)
                    if new_pos in grid and grid[new_pos] == level + 1 and (new_pos, level + 1) not in queue:
                        queue.append((new_pos, level + 1))
        return num_paths

    starts = [pos for pos, elevation in grid.items() if elevation == 0]
    paths = 0
    for start in starts:
        paths += find_paths(start)
    return paths


def test():
    data = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''
    grid, width, height = parse(data)
    assert part1(grid, width, height) == 36
    assert part2(grid, width, height) == 81


test()
data = read_data(2024, 10)
grid, width, height = parse(data)
print('Part1:', part1(grid, width, height))
print('Part2:', part2(grid, width, height))
