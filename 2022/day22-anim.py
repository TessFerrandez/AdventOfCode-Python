'''
GRAPH
There is something weird about p2
Look at day 22 no anim for a correct solution
'''
from input_processing import read_data_no_strip
from dataclasses import dataclass
from typing import List, Tuple
import numpy as np
import pygame


EMPTY = 0
WALL = 1
GROUND = 2
PATH = 3

# facing
RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 1000
STEPS = {UP: (-1, 0), DOWN: (1, 0), LEFT: (0, -1), RIGHT: (0, 1)}


def parse(data):
    def parse_grid(grid_data):
        grid_data = grid_data.splitlines()

        height = len(grid_data) + 2
        width = max(len(line) for line in grid_data) + 2

        grid = np.zeros((height, width))
        for r, row in enumerate(grid_data):
            first = last = -1
            for c, square in enumerate(row):
                if square == ' ':
                    continue
                if square == '.':
                    grid[r + 1, c + 1] = GROUND
                elif square == '#':
                    grid[r + 1, c + 1] = WALL

        row_ends = {}
        col_ends = {}

        for row in range(height):
            first = last = -1
            for col in range(width):
                if grid[row, col] != EMPTY:
                    first = col if first == -1 else first
                    last = col
            row_ends[row] = (first, last)

        for col in range(width):
            first = last = -1
            for row in range(height):
                if grid[row, col] != EMPTY:
                    first = row if first == -1 else first
                    last = row
            col_ends[col] = (first, last)

        first_square = 1, row_ends[1][0]

        return grid, row_ends, col_ends, first_square

    def parse_path(path_data):
        path = []

        current_number = ''
        for ch in path_data:
            if ch in 'RLUD':
                path.append((int(current_number), ch))
                current_number = ''
            else:
                current_number += ch

        return path

    grid_data, path_data = data.split('\n\n')
    grid, row_ends, col_ends, first_square = parse_grid(grid_data)
    path = parse_path(path_data)

    return grid, row_ends, col_ends, first_square, path


@dataclass
class GameState:
    path: List[Tuple[int, str]]
    current_segment: int
    current_pos: Tuple[int, int]
    current_facing: int
    current_step_diff: Tuple[int, int]
    steps_left_in_segment: int
    done: bool = True


def simulate_monkey_trail_part1(grid, connected, first_square, path, animate=False):
    def create_materials():
        materials = {tile_type: pygame.Surface((tile_size, tile_size))
                     for tile_type in [EMPTY, WALL, GROUND, PATH]}
        materials[EMPTY].fill('bisque2')
        materials[WALL].fill('brown')
        materials[GROUND].fill('bisque3')
        materials[PATH].fill('aqua')
        return materials

    def init_game():
        real_screen_width = width * tile_size
        real_screen_height = height * tile_size

        pygame.init()
        screen = pygame.display.set_mode((real_screen_width, real_screen_height))
        background_color = pygame.Color('white')
        materials = create_materials()

        return screen, background_color, materials

    def draw_grid():
        for row in range(height):
            for col in range(width):
                position = (col * tile_size, row * tile_size)
                screen.blit(materials[grid[row, col]], position)

    def update_grid(game_state: GameState):
        def turn(current_facing, turn):
            return {
                RIGHT: {'R': (DOWN, (1, 0)), 'L': (UP, (-1, 0))},
                DOWN: {'R': (LEFT, (0, -1)), 'L': (RIGHT, (0, 1))},
                UP: {'R': (RIGHT, (0, 1)), 'L': (LEFT, (0, -1))},
                LEFT: {'R': (UP, (-1, 0)), 'L': (DOWN, (1, 0))}
            }[current_facing][turn]

        if game_state.done:
            return game_state

        if game_state.steps_left_in_segment != 0:
            current_row, current_col = game_state.current_pos
            dr, dc = game_state.current_step_diff

            next_row, next_col = current_row + dr, current_col + dc
            next_facing = None
            wrap = False
            if (next_row, next_col) in connected:
                wrap = True
                next_facing = connected[(next_row, next_col)][1]
                next_row, next_col = connected[(next_row, next_col)][0]

            if grid[next_row, next_col] in (GROUND, PATH):
                game_state.current_pos = (next_row, next_col)
                game_state.steps_left_in_segment -= 1
                grid[next_row, next_col] = PATH
                if wrap:
                    game_state.current_facing = next_facing
                    game_state.current_step_diff = STEPS[next_facing]
            else:
                game_state.steps_left_in_segment = 0
        else:
            # turn
            facing, step_diff = turn(game_state.current_facing, game_state.path[game_state.current_segment][1])
            game_state.current_facing = facing
            game_state.current_step_diff = step_diff

            # switch segment
            game_state.current_segment += 1

            # if segment is > len(segments) - end turn
            if game_state.current_segment == len(game_state.path):
                game_state.done = True
            else:
                # mark steps left
                game_state.steps_left_in_segment = game_state.path[game_state.current_segment][0]

        return game_state

    height, width = grid.shape
    tile_size = min(SCREEN_WIDTH // width, SCREEN_HEIGHT // height)

    if animate:
        screen, bg_color, materials = init_game()
        clock = pygame.time.Clock()
        running = True

        start_row, start_col = first_square
        game_state = GameState(path, 0, (start_row, start_col), RIGHT, (0, 1), path[0][0], False)
        grid[start_row, start_col] = PATH

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            game_state = update_grid(game_state)

            screen.fill(bg_color)
            draw_grid()
            pygame.display.flip()

            clock.tick(40)

        pygame.quit()
    else:
        start_row, start_col = first_square
        game_state = GameState(path, 0, (start_row, start_col), RIGHT, (0, 1), path[0][0], False)
        grid[start_row, start_col] = PATH

        while not game_state.done:
            game_state = update_grid(game_state)

    return game_state.current_pos[0], game_state.current_pos[1], game_state.current_facing


def part1(grid, row_ends, col_ends, first_square, path, animate=False):
    connected = {}
    for row in row_ends:
        connected[(row, row_ends[row][0] - 1)] = ((row, row_ends[row][1]), LEFT)
        connected[(row, row_ends[row][1] + 1)] = ((row, row_ends[row][0]), RIGHT)
    for col in col_ends:
        connected[(col_ends[col][0] - 1, col)] = ((col_ends[col][1], col), DOWN)
        connected[(col_ends[col][1] + 1, col)] = ((col_ends[col][0], col), UP)

    row, col, facing = simulate_monkey_trail_part1(grid, connected, first_square, path, animate)
    return row * 1000 + col * 4 + facing


def part2(grid, path, first_square, testing=False, animate=False):
    connected = {}

    def connect(square1, side1, square2, side2, reverse, dir1, dir2):
        r1, c1 = top_lefts[square1]
        r2, c2 = top_lefts[square2]

        if side1 == UP:
            connect1 = [(r1 - 1, c) for c in range(c1, c1 + dice_side)]
        elif side1 == DOWN:
            connect1 = [(r1 + dice_side, c) for c in range(c1, c1 + dice_side)]
        elif side1 == LEFT:
            connect1 = [(r, c1 - 1) for r in range(r1, r1 + dice_side)]
        else:
            connect1 = [(r, c1 + dice_side) for r in range(r1, r1 + dice_side)]

        if side2 == UP:
            connect2 = [(r2, c) for c in range(c2, c2 + dice_side)]
        elif side2 == DOWN:
            connect2 = [(r2 + dice_side - 1, c) for c in range(c2, c2 + dice_side)]
        elif side2 == LEFT:
            connect2 = [(r, c2) for r in range(r2, r2 + dice_side)]
        else:
            connect2 = [(r, c2 + dice_side - 1) for r in range(r2, r2 + dice_side)]

        if reverse:
            connect2 = connect2[::-1]

        for i in range(len(connect1)):
            connected[connect1[i]] = (connect2[i], dir1)

        if side1 == UP:
            connect1 = [(r1, c) for c in range(c1, c1 + dice_side)]
        elif side1 == DOWN:
            connect1 = [(r1 + dice_side - 1, c) for c in range(c1, c1 + dice_side)]
        elif side1 == LEFT:
            connect1 = [(r, c1) for r in range(r1, r1 + dice_side)]
        else:
            connect1 = [(r, c1 + dice_side - 1) for r in range(r1, r1 + dice_side)]

        if side2 == UP:
            connect2 = [(r2 - 1, c) for c in range(c2, c2 + dice_side)]
        elif side2 == DOWN:
            connect2 = [(r2 + dice_side, c) for c in range(c2, c2 + dice_side)]
        elif side2 == LEFT:
            connect2 = [(r, c2 - 1) for r in range(r2, r2 + dice_side)]
        else:
            connect2 = [(r, c2 + dice_side) for r in range(r2, r2 + dice_side)]

        if reverse:
            connect1 = connect1[::-1]

        for i in range(len(connect2)):
            connected[connect2[i]] = (connect1[i], dir2)

    if testing:
        top_lefts = {'A': (1, 9), 'B': (5, 1), 'C': (5, 5), 'D': (5, 9), 'E': (9, 9), 'F': (9, 13)}
        dice_side = 4

        connect('A', UP, 'B', UP, True, RIGHT, DOWN)
        connect('C', UP, 'A', LEFT, False, RIGHT, DOWN),
        connect('A', RIGHT, 'F', RIGHT, True, LEFT, LEFT)
        connect('D', RIGHT, 'F', UP, True, DOWN, LEFT)
        connect('B', LEFT, 'F', DOWN, True, UP, RIGHT)
        connect('B', DOWN, 'E', DOWN, True, UP, UP)
        connect('C', DOWN, 'E', LEFT, True, RIGHT, UP)
    else:
        top_lefts = {'A': (1, 51), 'B': (1, 101), 'C': (51, 51), 'D': (101, 1), 'E': (101, 51), 'F': (151, 1)}
        dice_side = 50

        connect('A', UP, 'F', LEFT, False, RIGHT, DOWN)
        connect('A', LEFT, 'D', LEFT, True, RIGHT, RIGHT),
        connect('B', UP, 'F', DOWN, False, UP, DOWN)
        connect('B', RIGHT, 'E', RIGHT, True, LEFT, LEFT)
        connect('B', DOWN, 'C', RIGHT, False, LEFT, UP)
        connect('C', LEFT, 'D', UP, False, DOWN, RIGHT)
        connect('E', DOWN, 'F', RIGHT, False, LEFT, UP)

    row, col, facing = simulate_monkey_trail_part1(grid, connected, first_square, path, animate)
    return row * 1000 + col * 4 + facing


def test():
    grid, row_ends, col_ends, first_square, path = parse(read_data_no_strip(2022, 22))
    # part1(grid.copy(), row_ends, col_ends, first_square, path, animate=False) == 6032
    # part2(grid.copy(), path, first_square, animate=False) == 5031


test()
grid, row_ends, col_ends, first_square, path = parse(read_data_no_strip(2022, 22))
# print('Part1:', part1(grid.copy(), row_ends, col_ends, first_square, path, animate=False))
print('Part2:', part2(grid.copy(), path, first_square, animate=True))
