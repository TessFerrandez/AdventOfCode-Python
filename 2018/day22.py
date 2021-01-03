""" algorithm from korylprince """
import networkx as nx
from typing import Tuple


def generate_grid(depth: int, target: Tuple[int, int]) -> dict:
    # (x, y) -> geo, erosion, risk
    grid = {}

    tx, ty = target
    for y in range(ty + 1):
        for x in range(tx + 1):
            if (x, y) in [(0, 0), target]:
                geo = 0
            elif x == 0:
                geo = y * 48271
            elif y == 0:
                geo = x * 16807
            else:
                geo = grid[(x - 1, y)][1] * grid[(x, y - 1)][1]
            erosion = (geo + depth) % 20183
            risk = erosion % 3
            grid[(x, y)] = (geo, erosion, risk)
    return grid


def part1(depth: int, target: Tuple[int, int]) -> int:
    grid = generate_grid(depth, target)
    return sum(risk for _, _, risk in grid.values())


def dijkstra(grid: dict, corner: Tuple[int, int], target: Tuple[int, int]):
    rocky, wet, narrow = 0, 1, 2
    torch, gear, neither = 0, 1, 2
    valid_items = {rocky: (torch, gear), wet: (gear, neither), narrow: (torch, neither)}

    graph = nx.Graph()

    max_x, max_y = corner
    target_x, target_y = target

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            items = valid_items[grid[(x, y)]]
            graph.add_edge((x, y, items[0]), (x, y, items[1]), weight=7)
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x <= max_x and 0 <= new_y <= max_y:
                    new_items = valid_items[grid[(new_x, new_y)]]
                    for item in set(items).intersection(set(new_items)):
                        graph.add_edge((x, y, item), (new_x, new_y, item), weight=1)

    return nx.dijkstra_path_length(graph, (0, 0, torch), (target_x, target_y, torch))


def part2(depth: int, target: Tuple[int, int], extra: int) -> int:
    corner = (target[0] + extra, target[1] + extra)

    # generate a grid a bit larger than the target square
    grid = generate_grid(depth, corner)

    # extract only the region types
    grid = {c: v[2] for c, v in grid.items()}

    #
    return dijkstra(grid, corner, target)


def main():
    # depth, target = 510, (10, 10)
    depth, target = 10647, (7, 770)
    print(f'Part 1: {part1(depth, target)}')
    print(f'Part 2: {part2(depth, target, extra=100)}')


if __name__ == "__main__":
    main()
