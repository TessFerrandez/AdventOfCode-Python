from input_processing import read_data
from heapq import heappop, heappush
from sys import maxsize


def parse(data):
    grid = set()
    data = data.splitlines()
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                end = (x, y)
            if cell != '#':
                grid.add((x, y))
    return grid, start, end, len(data[0]), len(data)


def part1(grid, start, end):
    return dijkstra(grid, start, end)


def dijkstra(graph, start, end):
    def get_neighbors(vertex, direction):
        x, y = vertex
        neighbors = {(0, 1): [(1, 0, 1), (1001, 1, 0), (1001, -1, 0), (2001, 0, 1)],
                     (1, 0): [(1, 1, 0), (1001, 0, -1), (1001, 0, 1), (2001, -1, 0)],
                     (0, -1): [(1, 0, -1), (1001, -1, 0), (1001, 1, 0), (2001, 0, 1)],
                     (-1, 0): [(1, -1, 0), (1001, 0, -1), (1001, 0, 1), (2001, 1, 0)]}
        for cost, dx, dy in neighbors[direction]:
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) in graph:
                yield cost, (new_x, new_y), (dx, dy)

    queue, seen, mins = [(0, start, (-1, 0))], set(), {start: 0}
    while queue:
        (cost, vertex1, direction) = heappop(queue)
        if (vertex1, direction) not in seen:
            seen.add((vertex1, direction))
            if vertex1 == end:
                return cost

            for move_cost, vertex2, direction in get_neighbors(vertex1, direction):
                if (vertex2, direction) in seen:
                    continue
                prev = mins.get(vertex2, None)
                next = cost + move_cost
                if prev is None or next < prev:
                    mins[vertex2] = next
                    heappush(queue, (next, vertex2, direction))

    return float("inf")


def dijkstra_path(grid, start, end, width, height):
    mins = {(pos, dir): maxsize for pos in grid for dir in range(4)}
    diffs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = [(0, start, 1, [start])]    # start facing east
    paths = []
    best_score = maxsize

    while queue and queue[0][0] <= best_score:
        score, pos, dir, path = heappop(queue)
        if pos == end:
            best_score = score
            paths.append(path)
            continue
        if mins[(pos, dir)] < score:
            continue
        mins[(pos, dir)] = score

        for direction in range(4):
            dy, dx = diffs[direction]
            new_pos = pos[0] + dx, pos[1] + dy
            if new_pos in grid and new_pos not in path:
                cost = 1 if direction == dir else 1001
                heappush(queue, (score + cost, new_pos, direction, path + [new_pos]))

    seats = set()
    for path in paths:
        seats |= set(path)
    return len(seats)


def part2(grid, start, end, width, height):
    return dijkstra_path(grid, start, end, width, height)


def test():
    data = '''###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############'''
    grid, start, end, width, height = parse(data)
    assert part1(grid, start, end) == 7036
    assert part2(grid, start, end, width, height) == 45
    data = '''#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################'''
    grid, start, end, width, height = parse(data)
    assert part1(grid, start, end) == 11048
    assert part2(grid, start, end, width, height) == 64


test()
data = read_data(2024, 16)
grid, start, end, width, heigh = parse(data)
print('Part1:', part1(grid, start, end))
print('Part2:', part2(grid, start, end, width, heigh))
