from heapq import heappush, heappop
from typing import List, Tuple
from collections import namedtuple, deque
from progressbar import ProgressBar


def parse_input(filename: str) -> List[str]:
    return [line.strip() for line in open(filename).readlines()]


def get_start_and_keys(maze: List[str]) -> ((int, int), set):
    width, height = len(maze[0]), len(maze)
    keys = set()
    start = (0, 0)
    for y in range(height):
        for x in range(width):
            if maze[y][x] == '@':
                start = (x, y)
            if 'a' <= maze[y][x] <= 'z':
                keys.add(maze[y][x])
    return start, keys


def print_maze(maze: List[str]):
    print('-' * len(maze[0]))
    for row in maze:
        print(row)
    print('-' * len(maze[0]))


def get_neighbors(x, y) -> List[Tuple[int, int]]:
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


def part1(maze: List[str]) -> int:
    # print_maze(maze)

    (x, y), all_keys = get_start_and_keys(maze)

    State = namedtuple('State', ['x', 'y', 'keys', 'distance'])
    queue = deque()
    seen = set()

    # print(f'Starting at ({x}, {y}), looking for keys: {list(all_keys)}')
    queue.append(State(x, y, set(), 0))

    with ProgressBar(max_value=7400000) as p:
        while queue:
            x, y, keys, distance = queue.popleft()

            key = (x, y, tuple(sorted(keys)))
            if key in seen:
                # been here, done that
                continue
            seen.add(key)

            if len(seen) % 100000 == 0:
                p.update(len(seen))

            ch_at_pos = maze[y][x]
            if ch_at_pos == '#':
                # wall
                continue
            if 'A' <= ch_at_pos <= 'Z' and ch_at_pos.lower() not in keys:
                # locked door
                continue

            new_keys = set(keys)
            if 'a' <= ch_at_pos <= 'z':
                # new key - who diz
                new_keys.add(ch_at_pos)
                if new_keys == all_keys:
                    return distance

            # check out the neighbors
            for nx, ny in get_neighbors(x, y):
                queue.append(State(nx, ny, new_keys, distance + 1))

    return 0


def get_key_locations(maze: List[List[str]]) -> (dict, int):
    key_locations = {}
    opening = ord('0')
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x].islower():
                key_locations[maze[y][x]] = (y, x)
            elif maze[y][x] == '@':
                key_locations[chr(opening)] = (y, x)
                opening += 1

    num_keys = len(key_locations.keys()) - (opening - ord('0'))
    return key_locations, num_keys


def bfs(position, maze):
    """
    returns all reachable keys (even if there are doors in between)
    returns a dictionary like this:
    {'a': (7, ('b', 'c')), 'b': (4, ('d'))}
    -> can reach key a in 7 steps but door B and C are blocking
    -> can reach key b in 4 steps but door D is blocking
    """
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

    queue = [(*position, 0, ())]
    seen, reachable_keys = set(), dict()
    while queue:
        y, x, distance, doors_between = queue.pop(0)
        if (y, x) in seen:
            continue
        seen.add((y, x))
        if maze[y][x].islower() and position != (y, x):
            reachable_keys[maze[y][x]] = (distance, frozenset(doors_between))
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if maze[ny][nx] != '#':
                queue.append((ny, nx, distance + 1, doors_between + (maze[ny][nx].lower(),) if maze[ny][nx].isupper() else doors_between))
    return reachable_keys


def part2(maze: List[str]) -> int:
    maze = [list(row) for row in maze]

    # get all key location
    key_locations, num_keys = get_key_locations(maze)

    # get a graph between all starting points and keys and all other points
    # - and doors in between
    graph = {key: dict() for key in key_locations.keys()}
    for key in key_locations.keys():
        for key_reached, info in bfs(key_locations[key], maze).items():
            graph[key][key_reached] = info

    # start with four openings (0, 1, 2, 3) and an empty bag of keys
    # and go to a full bag of keys
    queue = [(0, (('0', '1', '2', '3'), frozenset()))]
    seen = dict()
    with ProgressBar(max_value=1836) as p:
        while queue:
            distance, node = heappop(queue)
            p.update(distance)
            if node in seen:
                continue
            seen[node] = distance
            bots, keys_in_bag = node
            if len(keys_in_bag) == num_keys:
                return distance
            for i in range(len(bots)):
                for key, (distance_to_key, doors) in graph[bots[i]].items():
                    if len(doors - keys_in_bag) == 0 and key not in keys_in_bag:
                        heappush(queue, ((distance + distance_to_key), (bots[:i] + (key,) + bots[i + 1:], keys_in_bag | frozenset(key))))

    return 0


def main():
    maze = parse_input('input/day18.txt')
    print(f'Part 1: {part1(maze)}')
    maze = parse_input('input/day18_pt2.txt')
    print(f'Part 2: {part2(maze)}')


if __name__ == "__main__":
    main()
