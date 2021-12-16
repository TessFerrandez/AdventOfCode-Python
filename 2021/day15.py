import sys
from typing import Dict, Tuple, List
from collections import defaultdict


def read_input() -> Tuple[Dict[Tuple[int, int], int], int, int]:
    risks = {(x, y): int(risk)
             for x, line in enumerate(open('2021/input/day15.txt'))
             for y, risk in enumerate(line.strip())}
    width = max(point[0] for point in risks) + 1
    height = max(point[1] for point in risks) + 1
    return risks, width, height


def get_least_risk(risks, width, height):
    """
    Dynamic programming solution to find the least risk path.
    Assumes you will always only go east or south.
    Starting bottom, right, just add min(east, south) to the current risk.
    min_risk[(0, 0)] will contain the least risk path from start to end (including self)
    """
    min_risk = {}

    for x in range(width - 1, -1, -1):
        for y in range(height - 1, -1, -1):
            neighbors = [min_risk[neighbor] for neighbor in [(x + 1, y), (x, y + 1)]
                         if neighbor in min_risk]
            min_neighbors = min(neighbors, default=0)
            min_risk[x, y] = min_neighbors + risks[(x, y)]

    return min_risk[(0, 0)] - risks[(0, 0)]


def expand_risks(risks, width, height) -> Tuple[Dict, int, int]:
    new_risks = {}

    for x, y in risks:
        for row in range(5):
            for col in range(5):
                new_risk = risks[(x, y)] + col + row
                new_risks[x + col * width, y + row * height] = new_risk if new_risk <= 9 else new_risk - 9

    return new_risks, width * 5, height * 5


def pop_item_with_lowest_risk(todo: List[Tuple[Tuple[int, int], int]]) -> Tuple[Tuple[int, int], int]:
    node = min(todo, key=lambda node: node[1])
    todo.remove(node)
    return node


def get_least_risk_djikstra(risks, width, height) -> int:
    """
    Djiksra's algorithm to find the least risk path.
    This allows you to travel in any direction
    """
    path_risk = defaultdict(lambda: sys.maxsize)
    path_risk[(0, 0)] = 0
    todo = [((0, 0), 0)]

    while(todo):
        (x, y), risk = pop_item_with_lowest_risk(todo)

        for neighbor in [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]:
            if neighbor in risks:
                neighbor_risk = path_risk[neighbor]
                if neighbor_risk > risk + risks[neighbor]:
                    if (neighbor, neighbor_risk) in todo:
                        todo.remove((neighbor, neighbor_risk))
                    path_risk[neighbor] = risk + risks[neighbor]
                    todo.append((neighbor, path_risk[neighbor]))

    return path_risk[(width - 1, height - 1)]


risks, width, height = read_input()
print("Part 1:", get_least_risk(risks, width, height))

risks, width, height = expand_risks(risks, width, height)
print("Part 2:", get_least_risk(risks, width, height))
print("Part 2: (djikstra)", get_least_risk_djikstra(risks, width, height))
