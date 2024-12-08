from collections import defaultdict
from input_processing import read_data


def parse(data):
    antennas = defaultdict(list)
    data = data.splitlines()
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c != '.':
                antennas[c].append((x, y))
    return antennas, len(data[0]), len(data)


def get_anti_nodes(antennas, antenna, width, height):
    anti_nodes = set()
    antenna_locations = antennas[antenna]
    for i in range(len(antenna_locations) - 1):
        for j in range(i + 1, len(antenna_locations)):
            x1, y1 = antenna_locations[i]
            x2, y2 = antenna_locations[j]
            dx, dy = x2 - x1, y2 - y1
            a1 = (x2 + dx, y2 + dy)
            a2 = (x1 - dx, y1 - dy)
            if 0 <= a1[0] < width and 0 <= a1[1] < height:
                anti_nodes.add(a1)
            if 0 <= a2[0] < width and 0 <= a2[1] < height:
                anti_nodes.add(a2)
    return anti_nodes


def get_anti_nodes_p2(antennas, antenna, width, height):
    anti_nodes = set()
    antenna_locations = antennas[antenna]

    for i in range(len(antenna_locations) - 1):
        for j in range(i + 1, len(antenna_locations)):
            x1, y1 = antenna_locations[i]
            x2, y2 = antenna_locations[j]
            dx, dy = x2 - x1, y2 - y1
            ax, ay = x1, y1
            while 0 <= ax < width and 0 <= ay < height:
                anti_nodes.add((ax, ay))
                ax += dx
                ay += dy
            ax, ay = x1 - dx, y1 - dy
            while 0 <= ax < width and 0 <= ay < height:
                anti_nodes.add((ax, ay))
                ax -= dx
                ay -= dy
    return anti_nodes


def part1(antennas, width, height):
    anti_nodes = set()
    for antenna in antennas:
        anti_nodes.update(get_anti_nodes(antennas, antenna, width, height))
    return len(anti_nodes)


def part2(antennas, width, height):
    anti_nodes = set()
    for antenna in antennas:
        anti_nodes.update(get_anti_nodes_p2(antennas, antenna, width, height))
    return len(anti_nodes)


def test():
    data = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............'''
    antennas, width, height = parse(data)
    assert part1(antennas, width, height) == 14
    assert part2(antennas, width, height) == 34

test()
data = read_data(2024, 8)
antennas, width, height = parse(data)
print('Part1:', part1(antennas, width, height))
print('Part2:', part2(antennas, width, height))
