from hashlib import md5


def path_to_str(path: list) -> str:
    pre_square = path[0]
    path_str = ""
    for square in path[1:]:
        if square[1] - pre_square[1] == 1:
            path_str += "D"
        elif square[1] - pre_square[1] == -1:
            path_str += "U"
        elif square[0] - pre_square[0] == 1:
            path_str += "R"
        else:
            path_str += "L"
        pre_square = square
    return path_str


def get_neighbor_rooms(position: list, path: str, key="lpvhkcbi") -> list:
    hash_code = md5((key + path).encode("utf-8")).hexdigest()
    open_door = "bcdef"
    directions = []
    if hash_code[0] in open_door and position[1] - 1 >= 0:
        directions.append([position[0], position[1] - 1])
    if hash_code[1] in open_door and position[1] + 1 < 4:
        directions.append([position[0], position[1] + 1])
    if hash_code[2] in open_door and position[0] - 1 >= 0:
        directions.append([position[0] - 1, position[1]])
    if hash_code[3] in open_door and position[0] + 1 < 4:
        directions.append([position[0] + 1, position[1]])
    return directions


def bfs_shortest_path(start=[0, 0], goal=[3, 3]) -> list:
    to_visit = [[start]]

    if start == goal:
        return []

    while to_visit:
        path = to_visit.pop(0)
        square = path[-1]
        path_str = path_to_str(path)
        neighbors = get_neighbor_rooms(square, path_str)
        for neighbor in neighbors:
            new_path = list(path)
            new_path.append(neighbor)
            to_visit.append(new_path)
            if neighbor == goal:
                return new_path
    return []


def paths_to_vault(start=[0, 0], goal=[3, 3]) -> list:
    to_visit = [[start]]
    all_paths = []

    if start == goal:
        return []

    i = 0
    while to_visit:
        path = to_visit.pop(0)
        square = path[-1]
        path_str = path_to_str(path)
        neighbors = get_neighbor_rooms(square, path_str)
        for neighbor in neighbors:
            new_path = list(path)
            new_path.append(neighbor)
            if neighbor == goal:
                i += 1
                all_paths.append(new_path)
            else:
                to_visit.append(new_path)

    return all_paths


def puzzles():
    print("shortest path:", path_to_str(bfs_shortest_path()))
    all_paths = paths_to_vault()
    max_len = 0
    for path in all_paths:
        max_len = max(max_len, len(path))
    print("longest path:", max_len - 1)


if __name__ == "__main__":
    puzzles()
