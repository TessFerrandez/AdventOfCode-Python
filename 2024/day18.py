from input_processing import read_data


def parse(data):
    return [tuple(map(int, line.split(','))) for line in data.splitlines()]


def get_grid(coordinates, height, width, n_coordinates):
    corrupt = set()
    for x in range(-1, width + 1):
        corrupt.add((x, -1))
        corrupt.add((x, height))
    for y in range(-1, height + 1):
        corrupt.add((-1, y))
        corrupt.add((width, y))
    for x, y in coordinates[: n_coordinates]:
        corrupt.add((x, y))
    return corrupt


def shortest_path(width, height, corrupt):
    start = (0, 0)
    end = (width - 1, height - 1)

    queue = [(start, 0)]
    visited = set()

    while queue:
        (x, y), distance = queue.pop(0)
        if (x, y) == end:
            return distance
        if (x, y) in visited or (x, y) in corrupt:
            continue
        visited.add((x, y))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            queue.append(((x + dx, y + dy), distance + 1))
    return -1


def part1(coordinates, height, width, n_coordinates):
    corrupt = get_grid(coordinates, height, width, n_coordinates)
    return shortest_path(width, height, corrupt)


def part2(coordinates, height, width, n_coordinates):
    corrupt = get_grid(coordinates, height, width, n_coordinates)

    for coordinate in coordinates[n_coordinates:]:
        corrupt.add(coordinate)
        if shortest_path(width, height, corrupt) == -1:
            return str(coordinate[0]) + "," + str(coordinate[1])


def test():
    data = '''5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0'''
    assert part1(parse(data), 7, 7, 12) == 22
    print(part2(parse(data), 7, 7, 12))


test()
data = read_data(2024, 18)
print('Part1:', part1(parse(data), 71, 71, 1024))
print('Part2:', part2(parse(data), 71, 71, 1024))
