import re
import pygame
import numpy as np
from typing import List, Tuple


EMPTY = 0
CLAY = 1
FLOWING = 2
SETTLED = 3

SCREEN_WIDTH, SCREEN_HEIGHT = 1600, 1000
TILE_SIZE = 5


def print_grid(grid: np.array, min_x: int, max_x: int):
    symbols = {EMPTY: ".", CLAY: "#", FLOWING: "|", SETTLED: "~"}
    for line in grid:
        for tile in line[min_x - 1 : max_x + 2]:
            print(symbols[tile], end="")
        print()
    print()


def parse_input(filename: str) -> (np.array, int, int, int, int):
    lines = [line.strip() for line in open(filename).readlines()]

    clays = []

    min_x, max_x = float("inf"), float("-inf")
    min_y, max_y = float("inf"), float("-inf")

    # extract clay positions and min, max values
    for line in lines:
        width_pos, length_from, length_to = map(int, re.findall(r"([\d]+)", line))
        width_dir = line[0]

        clays.append((width_dir, width_pos, length_from, length_to))
        if width_dir == "x":
            min_x, max_x = min(min_x, width_pos), max(max_x, width_pos)
            min_y, max_y = min(min_y, length_from), max(max_y, length_to)
        else:
            min_x, max_x = min(min_x, length_from), max(max_x, length_to)
            min_y, max_y = min(min_y, width_pos), max(max_y, width_pos)

    grid = np.zeros((max_y + 2, max_x + 2))
    for width_dir, width_pos, length_from, length_to in clays:
        if width_dir == "x":
            grid[length_from : length_to + 1, width_pos] = 1
        else:
            grid[width_pos, length_from : length_to + 1] = 1

    return grid, min_x, max_x, min_y, max_y


def flow(grid: np.array, max_y: int, todo: List[Tuple[int, int]]):
    x, y = todo.pop()

    if y > max_y:
        return

    if grid[y + 1][x] in [EMPTY, FLOWING]:
        # flow down
        grid[y][x] = FLOWING
        todo.append((x, y + 1))
        return
    else:
        # flow left and right
        fill_left = x
        while grid[y][fill_left] in [EMPTY, FLOWING] and grid[y + 1][fill_left] in [
            CLAY,
            SETTLED,
        ]:
            grid[y][fill_left] = FLOWING
            fill_left -= 1
        fill_right = x
        while grid[y][fill_right] in [EMPTY, FLOWING] and grid[y + 1][fill_right] in [
            CLAY,
            SETTLED,
        ]:
            grid[y][fill_right] = FLOWING
            fill_right += 1

        # if we have an area delimited by clay - settle the water and move up
        if grid[y][fill_left] == CLAY and grid[y][fill_right] == CLAY:
            grid[y][fill_left + 1 : fill_right] = SETTLED
            todo.append((x, y - 1))
            return

        # if it is not delimited, start a flow
        if grid[y + 1][fill_left] == EMPTY:
            todo.append((fill_left, y))

        if grid[y + 1][fill_right] == EMPTY:
            todo.append((fill_right, y))


def create_surfaces() -> dict:
    surfaces = {}
    for tile_type in [EMPTY, CLAY, FLOWING, SETTLED]:
        surfaces[tile_type] = pygame.Surface((TILE_SIZE, TILE_SIZE))
    surfaces[EMPTY].fill("gray50")
    surfaces[CLAY].fill("tan")
    surfaces[FLOWING].fill("blue")
    surfaces[SETTLED].fill("darkblue")
    return surfaces


def draw_elements(
    grid: np.array, screen: pygame.display, surfaces: dict, min_x: int, max_x: int
):
    for y, line in enumerate(grid):
        for x, tile in enumerate(line[min_x - 1 : max_x + 2]):
            if x * TILE_SIZE <= SCREEN_WIDTH and y * TILE_SIZE <= SCREEN_HEIGHT:
                screen.blit(surfaces[tile], (x * TILE_SIZE, y * TILE_SIZE))


def main():
    global TILE_SIZE

    grid, min_x, max_x, min_y, max_y = parse_input("input/day17.txt")

    show_flow = False
    if not show_flow:
        todo = [(500, 0)]
        while todo:
            flow(grid, max_y, todo)
        # print_grid(grid, min_x, max_x)
    else:
        TILE_SIZE = max(
            2,
            min(
                SCREEN_WIDTH // (max_x - min_x + 3),
                SCREEN_HEIGHT // (max_y - min_y + 3),
            ),
        )

        pygame.init()

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        background_color = pygame.Color("white")
        surfaces = create_surfaces()

        running = True
        todo = [(500, 0)]

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if todo:
                flow(grid, max_y, todo)

            # draw the background
            screen.fill(background_color)

            # draw the elements
            draw_elements(grid, screen, surfaces, min_x, max_x)

            # flip the display
            pygame.display.flip()

        pygame.quit()

    print(f"Puzzle 1: {np.sum(grid[min_y: max_y + 1, :] >= 2)}")
    print(f"Puzzle 2: {np.sum(grid[min_y: max_y + 1, :] >= 3)}")


if __name__ == "__main__":
    main()
