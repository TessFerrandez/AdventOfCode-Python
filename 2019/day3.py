"""
Crossed wires
"""
from utils import intersection


D = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def get_locations_visited(wire):
    wire_sections = wire.split(",")
    visited = []
    for section in wire_sections:
        direction = section[0]
        for _ in range(int(section[1:])):
            last_visited = visited[-1] if len(visited) > 0 else (0, 0)
            visited.append(
                (last_visited[0] + D[direction][0], last_visited[1] + D[direction][1])
            )
    return visited


def shortest_distance(locations):
    distances = [abs(x) + abs(y) for x, y in locations]
    return min(distances)


def least_steps(common, locations1, locations2):
    steps = [
        locations1.index(location) + locations2.index(location) for location in common
    ]
    return min(steps) + 2  # add the first step for each (0, 0)


def puzzle1and2():
    wires = open("input/day3.txt").readlines()
    locations_wire1 = get_locations_visited(wires[0])
    locations_wire2 = get_locations_visited(wires[1])
    common = intersection(locations_wire1, locations_wire2)

    print("shortest distance:", shortest_distance(common))
    print("least steps:", least_steps(common, locations_wire1, locations_wire2))


if __name__ == "__main__":
    puzzle1and2()
