from typing import List, Set
from collections import defaultdict
from math import sqrt
from copy import deepcopy
import numpy as np


def parse_input(filename: str) -> dict:
    tile_info = [tile for tile in open(filename).read().split('\n\n')]
    tiles = {}

    for info in tile_info:
        info_rows = [row.strip() for row in info.split('\n')]
        tile_number = int((info_rows[0].split(' ')[1][:-1]))
        contents = info_rows[1:]
        grid = np.zeros((len(contents), len(contents)))
        for y, row in enumerate(contents):
            for x, ch in enumerate(row):
                if ch == '#':
                    grid[y][x] = 1
        tiles[tile_number] = grid
    return tiles


def extract_edges(tiles: dict) -> dict:
    tile_edges = defaultdict(lambda: [])

    for tile in tiles:
        grid = tiles[tile]
        top = grid[0, :]
        bottom = grid[9, :]
        left = grid[:, 0]
        right = grid[:, 9]
        tile_edges[tile].append(int(''.join([str(int(i)) for i in top]), 2))
        tile_edges[tile].append(int(''.join([str(int(i)) for i in top[::-1]]), 2))
        tile_edges[tile].append(int(''.join([str(int(i)) for i in right]), 2))
        tile_edges[tile].append(int(''.join([str(int(i)) for i in right[::-1]]), 2))
        tile_edges[tile].append(int(''.join([str(int(i)) for i in bottom]), 2))
        tile_edges[tile].append(int(''.join([str(int(i)) for i in bottom[::-1]]), 2))
        tile_edges[tile].append(int(''.join([str(int(i)) for i in left]), 2))
        tile_edges[tile].append(int(''.join([str(int(i)) for i in left[::-1]]), 2))
    return dict(tile_edges)


def find_matches(edges: dict) -> dict:
    matches = {}

    for current_tile in edges:
        tile_matches = set()
        for i, edge in enumerate(edges[current_tile]):
            for tile in edges:
                if tile != current_tile and edge in edges[tile]:
                    tile_matches.add(tile)
        matches[current_tile] = tile_matches
    return matches


def all_neighbors_in_match(neighbors: List[int], matches: Set[int]) -> bool:
    for neighbor in neighbors:
        if neighbor not in matches:
            return False
    return True


def get_match(neighbors: List[int], sorted_tiles: List[int], matches: dict, visited: List[int]) -> int:
    if not neighbors:
        return sorted_tiles[0]
    else:
        for tile in sorted_tiles:
            if all_neighbors_in_match(neighbors, matches[tile]):
                return tile
    return None


def get_neighbors(grid: List[List[int]], y: int, x: int) -> List[int]:
    neighbors = []
    if x - 1 >= 0 and grid[y][x - 1] != 0:
        neighbors.append(grid[y][x - 1])
    if x + 1 < len(grid) and grid[y][x + 1] != 0:
        neighbors.append(grid[y][x + 1])
    if y - 1 >= 0 and grid[y - 1][x] != 0:
        neighbors.append(grid[y - 1][x])
    if y + 1 < len(grid) and grid[y + 1][x] != 0:
        neighbors.append(grid[y + 1][x])
    return neighbors


def build_tile_grid(original_matches: dict) -> List[List[int]]:
    matches = deepcopy(original_matches)
    sorted_tiles = [tile for tile in sorted(matches, key=lambda key: len(matches[key]))]

    num_tiles = len(sorted_tiles)
    size = int(sqrt(num_tiles))
    grid = [[0 for _ in range(size)] for _ in range(size)]
    visited = []

    for y in range(size):
        for x in range(size):
            neighbors = get_neighbors(grid, y, x)
            this_tile = get_match(neighbors, sorted_tiles, matches, visited)
            for neighbor in neighbors:
                matches[this_tile].remove(neighbor)
                matches[neighbor].remove(this_tile)
            visited.append(this_tile)
            grid[y][x] = this_tile

    return grid


def fix_orientation(orientation: List[int]):
    # cheap fix - may not be general but good enough for this
    replace = {0: 2, 1: 3, 2: 0, 3: 1}

    if orientation[0] == -1:
        orientation[0] = replace[orientation[2]]
    if orientation[1] == -1:
        orientation[1] = replace[orientation[3]]


def get_flip(tile_id: int, tile_grid: List[List[int]], edges: dict, row: int, col: int, size: int) -> str:
    tile_edges = edges[tile_id]

    orientation = [-1, -1, -1, -1]
    if row - 1 >= 0:
        top = tile_grid[row - 1][col]
        top_edges = edges[top]
        for i, edge in enumerate(tile_edges):
            if edge in top_edges:
                orientation[0] = i // 2
                break
    if col + 1 < size:
        right = tile_grid[row][col + 1]
        right_edges = edges[right]
        for i, edge in enumerate(tile_edges):
            if edge in right_edges:
                orientation[1] = i // 2
                break
    if row + 1 < size:
        bottom = tile_grid[row + 1][col]
        bottom_edges = edges[bottom]
        for i, edge in enumerate(tile_edges):
            if edge in bottom_edges:
                orientation[2] = i // 2
                break
    if col - 1 >= 0:
        left = tile_grid[row][col - 1]
        left_edges = edges[left]
        for i, edge in enumerate(tile_edges):
            if edge in left_edges:
                orientation[3] = i // 2
                break

    # print('orientation:', row, col, orientation)
    fix_orientation(orientation)
    # print('fixed orientation:', orientation)

    return ''.join(str(i) for i in orientation[0:2])


def build_image(tile_grid: List[List[int]], edges: dict, tiles: dict) -> List[str]:
    size = len(tile_grid)
    image = []

    for row in range(size):
        row_grid = []
        for col in range(size):
            tile_id = tile_grid[row][col]
            flip = get_flip(tile_id, tile_grid, edges, row, col, size)
            grid = tiles[tile_id][1:9, 1:9]

            if flip == '12':
                grid = np.rot90(grid)
            elif flip == '23':
                grid = np.rot90(np.rot90(grid))
            elif flip == '30':
                grid = np.rot90(np.rot90(np.rot90(grid)))
            elif flip == '03':
                grid = np.fliplr(grid)
            elif flip == '10':
                grid = np.rot90(np.flipud(grid))
            elif flip == '21':
                grid = np.rot90(np.rot90(np.fliplr(grid)))
            elif flip == '32':
                grid = np.rot90(np.fliplr(grid))

            if col == 0:
                row_grid = grid
            else:
                row_grid = np.concatenate((row_grid, grid), axis=1)
        if row == 0:
            image = row_grid
        else:
            image = np.concatenate((image, row_grid), axis=0)
    return image


def find_sea_monsters(image: np.array) -> (int, bool):
    size = len(image)

    found = False
    hash_amount = 0

    for y in range(size - 2):
        for x in range(size - 19):
            if image[y][x + 18] == 1 and \
               image[y + 1][x] == 1 and \
               image[y + 1][x + 5] == 1 and \
               image[y + 1][x + 6] == 1 and \
               image[y + 1][x + 11] == 1 and \
               image[y + 1][x + 12] == 1 and \
               image[y + 1][x + 17] == 1 and \
               image[y + 1][x + 18] == 1 and \
               image[y + 1][x + 19] == 1 and \
               image[y + 2][x + 1] == 1 and \
               image[y + 2][x + 4] == 1 and \
               image[y + 2][x + 7] == 1 and \
               image[y + 2][x + 10] == 1 and \
               image[y + 2][x + 13] == 1 and \
               image[y + 2][x + 16] == 1:
                found = True
                image[y][x + 18] = 2
                image[y + 1][x] = 2
                image[y + 1][x + 5] = 2
                image[y + 1][x + 6] = 2
                image[y + 1][x + 11] = 2
                image[y + 1][x + 12] = 2
                image[y + 1][x + 17] = 2
                image[y + 1][x + 18] = 2
                image[y + 1][x + 19] = 2
                image[y + 2][x + 1] = 2
                image[y + 2][x + 4] = 2
                image[y + 2][x + 7] = 2
                image[y + 2][x + 10] = 2
                image[y + 2][x + 13] = 2
                image[y + 2][x + 16] = 2

    if found:
        hash_amount = np.sum(image == 1)

    return hash_amount, found


def part2(matches: dict, edges: dict, tiles: dict) -> int:
    tile_grid = build_tile_grid(matches)

    image = build_image(tile_grid, edges, tiles)
    hashes_left, found = find_sea_monsters(image)
    if found:
        return hashes_left

    image = np.rot90(image)
    hashes_left, found = find_sea_monsters(image)
    if found:
        return hashes_left

    image = np.rot90(image)
    hashes_left, found = find_sea_monsters(image)
    if found:
        return hashes_left

    image = np.rot90(image)
    hashes_left, found = find_sea_monsters(image)
    if found:
        return hashes_left

    image = np.fliplr(np.rot90(image))
    hashes_left, found = find_sea_monsters(image)
    if found:
        return hashes_left

    image = np.rot90(image)
    hashes_left, found = find_sea_monsters(image)
    if found:
        return hashes_left

    image = np.rot90(image)
    hashes_left, found = find_sea_monsters(image)
    if found:
        return hashes_left

    image = np.rot90(image)
    hashes_left, found = find_sea_monsters(image)
    if found:
        return hashes_left

    return hashes_left


def part1(matches: dict) -> (int, dict):
    product = 1
    for tile in matches:
        if len(matches[tile]) == 2:
            product *= tile
    return product


def main():
    tiles = parse_input('input/day20.txt')
    edges = extract_edges(tiles)
    matches = find_matches(edges)
    print(f'Part 1: {part1(matches)}')
    print(f'Part 2: {part2(matches, edges, tiles)}')


if __name__ == "__main__":
    main()
