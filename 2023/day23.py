from collections import defaultdict, deque
from input_processing import read_data


def neighbors(grid, r, c):
    node = grid[r][c]

    if node == '.':
        for r, c in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if grid[r][c] != '#':
                yield (r, c)

    elif node == 'v':
        yield (r + 1, c)
    elif node == '^':
        yield (r - 1, c)
    elif node == '>':
        yield (r, c + 1)
    elif node == '<':
        yield (r, c - 1)


def num_neighbors(grid, r, c):
    if grid[r][c] == '.':
        return sum(grid[r][c] != '#' for r, c in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)))
    return 1


def is_node(grid, node, source, destination):
    return node == source or node == destination or num_neighbors(grid, *node) > 2


def get_neighbors(grid, node, source, destination):
    queue = deque([(node, 0)])
    visited = set()

    while queue:
        node, distance = queue.popleft()
        visited.add(node)

        for neighbor in neighbors(grid, *node):
            if neighbor in visited:
                continue

            if is_node(grid, neighbor, source, destination):
                yield (neighbor, distance + 1)
                continue

            queue.append((neighbor, distance + 1))


def graph_from_grid(grid, source, destination):
    graph = defaultdict(list)
    queue = deque([source])
    visited = set()

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in get_neighbors(grid, node, source, destination):
            graph[node].append((neighbor, weight))
            queue.append(neighbor)

    return graph


def parse(data):
    grid = list(map(list, data.splitlines()))
    height, width = len(grid), len(grid[0])
    grid[0][1] = '#'
    grid[height - 1][width - 2] = '#'
    source, destination = (1, 1), (height - 2, width - 2)

    graph = graph_from_grid(grid, source, destination)
    return graph, source, destination


def parse_no_slopes(data):
    grid = [list(line.replace('^', '.').replace('v', '.').replace('<', '.').replace('>', '.')) for line in data.splitlines()]
    height, width = len(grid), len(grid[0])
    grid[0][1] = '#'
    grid[height - 1][width - 2] = '#'
    source, destination = (1, 1), (height - 2, width - 2)

    graph = graph_from_grid(grid, source, destination)
    return graph, source, destination


def longest_path(graph, source, destination, distance=0, visited=set()):
    if source == destination:
        return distance

    best = 0
    visited.add(source)

    for neighbor, weight in graph[source]:
        if neighbor in visited:
            continue
        best = max(best, longest_path(graph, neighbor, destination, distance + weight))

    visited.remove(source)
    return best


def part1(graph, source, destination):
    return longest_path(graph, source, destination) + 2


def test():
    sample = '''#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#'''
    graph, source, destination = parse(sample)
    assert part1(graph, source, destination) == 94
    graph, source, destination = parse_no_slopes(sample)
    assert part1(graph, source, destination) == 154


test()
data = read_data(2023, 23)
graph, source, destination = parse(data)
print('Part1:', part1(graph, source, destination))
graph, source, destination = parse_no_slopes(data)
print('Part2:', part1(graph, source, destination))
