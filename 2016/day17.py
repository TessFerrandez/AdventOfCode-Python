from typing import List, Tuple
from hashlib import md5


def path_to_string(path: List[Tuple[int, int]]) -> str:
    last_x, last_y = path[0]
    path_str = ''

    for x, y in path[1:]:
        if y - last_y == 1:
            path_str += 'D'
        elif y - last_y == -1:
            path_str += 'U'
        elif x - last_x == 1:
            path_str += 'R'
        else:
            path_str += 'L'
        last_x, last_y = x, y
    return path_str


def get_neighbors(position: Tuple[int, int], path: str, key: str):
    hash_code = md5((key + path).encode('utf-8')).hexdigest()
    open_door = 'bcdef'
    directions = []
    x, y = position
    if hash_code[0] in open_door and y - 1 >= 0:
        directions.append((x, y - 1))
    if hash_code[1] in open_door and y + 1 < 4:
        directions.append((x, y + 1))
    if hash_code[2] in open_door and x - 1 >= 0:
        directions.append((x - 1, y))
    if hash_code[3] in open_door and x + 1 < 4:
        directions.append((x + 1, y))
    return directions


def bfs_shortest_path(key: str, start: Tuple[int, int] = (0, 0), goal: Tuple[int, int] = (3, 3)) -> List[Tuple[int, int]]:
    to_visit = [[start]]

    if start == goal:
        return []

    while to_visit:
        path = to_visit.pop(0)
        square = path[-1]
        path_str = path_to_string(path)
        neighbors = get_neighbors(square, path_str, key)
        for neighbor in neighbors:
            new_path = list(path)
            new_path.append(neighbor)
            to_visit.append(new_path)
            if neighbor == goal:
                return new_path
    return []


def part1(passcode: str) -> str:
    return path_to_string(bfs_shortest_path(passcode))


def paths_to_vault(passcode: str, start: Tuple[int, int] = (0, 0), goal: Tuple[int, int] = (3, 3)) -> List[Tuple[int, int]]:
    to_visit = [[start]]
    all_paths = []

    if start == goal:
        return []

    while to_visit:
        path = to_visit.pop(0)
        square = path[-1]
        path_str = path_to_string(path)
        neighbors = get_neighbors(square, path_str, passcode)
        for neighbor in neighbors:
            new_path = list(path)
            new_path.append(neighbor)
            if neighbor == goal:
                all_paths.append(new_path)
            else:
                to_visit.append(new_path)
    return all_paths


def part2(passcode: str) -> int:
    all_paths = paths_to_vault(passcode)
    return max(len(path) for path in all_paths) - 1


def main():
    passcode = 'lpvhkcbi'
    print(f'Part 1: {part1(passcode)}')
    print(f'Part 2: {part2(passcode)}')


if __name__ == "__main__":
    main()
