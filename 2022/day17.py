from enum import IntEnum
from numbers import Complex
from typing import List, Set
from dataclasses import dataclass
import pygame
from input_processing import read_data


WALL = 5
STOPPED = 6
TILE_SIZE = 20
SCREEN_WIDTH, SCREEN_HEIGHT = 180, 1000
VISIBLE_WIDTH, VISIBLE_HEIGHT = 9, 50


class RockShape(IntEnum):
    BAR = 0
    PLUS = 1
    BACKWARDS_L = 2
    COLUMN = 3
    SQUARE = 4


@dataclass
class Rock:
    top_left: Complex
    relative_positions: Set[Complex]
    shape: RockShape

    def __init__(self, top_left: int, shape: RockShape) -> None:
        self.top_left = top_left
        self.shape = shape
        match shape:
            case RockShape.BAR:
                self.relative_positions = {0 + 0j, 0 + 1j, 0 + 2j, 0 + 3j}
            case RockShape.PLUS:
                self.relative_positions = {0 + 1j, 1 + 0j, 1 + 1j, 1 + 2j, 2 + 1j}
            case RockShape.BACKWARDS_L:
                self.relative_positions = {0 + 2j, 1 + 2j, 2 + 0j, 2 + 1j, 2 + 2j}
            case RockShape.COLUMN:
                self.relative_positions = {0 + 0j, 1 + 0j, 2 + 0j, 3 + 0j}
            case RockShape.SQUARE:
                self.relative_positions = {0 + 0j, 0 + 1j, 1 + 0j, 1 + 1j}

    def get_positions(self):
        return {self.top_left + position for position in self.relative_positions}

    def move(self, direction: Complex):
        self.top_left += direction


@dataclass
class GameState:
    rock: Rock
    stopped: Set[Complex]
    column_heights = List[int]
    highest_rock: int = 0
    num_stopped: int = 0
    current_rock_shape: int = 0
    current_wind_idx: int = 0
    move_wind: bool = True

    def __init__(self) -> None:
        self.stopped = set()
        self.rock = Rock(-4 + 3j, 0)
        self.column_heights = [0 for _ in range(7)]


def create_materials():
    materials = {tile_type: pygame.Surface((TILE_SIZE, TILE_SIZE))
                 for tile_type in [RockShape.BAR, RockShape.BACKWARDS_L, RockShape.COLUMN, RockShape.PLUS, RockShape.SQUARE, WALL, STOPPED]}
    materials[WALL].fill('gray')
    materials[RockShape.PLUS].fill('red')
    materials[RockShape.BAR].fill('green')
    materials[RockShape.BACKWARDS_L].fill('blue')
    materials[RockShape.COLUMN].fill('purple')
    materials[RockShape.SQUARE].fill('orange')
    materials[STOPPED].fill('bisque4')
    return materials


def draw_tetris(state: GameState, screen, materials):
    rock_positions = state.rock.get_positions() if state.rock else set()
    screen_top = state.highest_rock - 5

    for row in range(screen_top, min(0, screen_top + VISIBLE_HEIGHT) + 1):
        for col in range(9):
            draw_position = (col * TILE_SIZE, (row - screen_top) * TILE_SIZE)
            if col == 0 or col == 8 or row == 0:
                screen.blit(materials[WALL], draw_position)
            else:
                position = row + 1j * col
                if position in rock_positions:
                    screen.blit(materials[state.rock.shape], (col * TILE_SIZE, (row - screen_top) * TILE_SIZE))
                elif position in state.stopped:
                    screen.blit(materials[STOPPED], (col * TILE_SIZE, (row - screen_top) * TILE_SIZE))


def update_tetris(state: GameState, wind):
    def is_blocked(rock: Rock, delta):
        for pos in rock.get_positions():
            if int((pos + delta).imag) in [0, 8] or int((pos + delta).real) == 0 or (pos + delta) in state.stopped:
                return True
        return False

    def mark_as_stopped(rock):
        rock_positions = rock.get_positions()
        state.stopped |= rock_positions

        for pos in rock_positions:
            row, col = int(pos.real), int(pos.imag)
            state.column_heights[col - 1] = min(state.column_heights[col - 1], row)

        state.num_stopped += 1

    if state.rock:
        if state.move_wind:
            wind_index = wind[state.current_wind_idx]
            if wind_index == '>' and not is_blocked(state.rock, 0 + 1j):
                state.rock.move(0 + 1j)
            elif wind_index == '<' and not is_blocked(state.rock, 0 - 1j):
                state.rock.move(0 - 1j)
            state.current_wind_idx = (state.current_wind_idx + 1) % len(wind)
            state.move_wind = False
        else:
            # check if can move down
            if is_blocked(state.rock, 1 + 0j):
                # mark this piece as stopped
                mark_as_stopped(state.rock)
                state.highest_rock = min(state.highest_rock, int(state.rock.top_left.real))
                state.rock = None
            else:
                # move down
                state.rock.move(1 + 0j)
                state.move_wind = True
    else:
        # add a new piece
        state.current_rock_shape = (state.current_rock_shape + 1) % 5
        rock_row = state.highest_rock - [1, 3, 3, 4, 2][state.current_rock_shape] - 4
        state.rock = Rock(rock_row + 3j, state.current_rock_shape)
        state.move_wind = False


def get_cycle_state(state):
    # note in reality it's min height but since we have negative heights it'll be the max
    max_column_height = max(state.column_heights)
    column_heights = tuple(col - max_column_height for col in state.column_heights)
    return (state.current_rock_shape, state.current_wind_idx, column_heights)


def calculate_result(state, states, current_state, highest_by_stop, stop_at):
    prev_stopped, prev_highest = states[current_state]
    cycle_length = state.num_stopped - prev_stopped
    height_per_cycle = prev_highest - state.highest_rock

    steps_to_go = stop_at - prev_stopped
    cycles_to_go = steps_to_go // cycle_length
    cycle_offset = steps_to_go % cycle_length

    # the minus here is because we have negative heights
    return (cycles_to_go * height_per_cycle) - highest_by_stop[prev_stopped + cycle_offset]


def simulate_tetris(wind, max_rocks=2022, animate=True):
    '''
    Bottom row (wall) is rpw 0
    All rows above are negative (eg. state.highest_rock is really -state.highest_rock)
    '''
    state = GameState()
    prev_stopped = 0
    states = {}
    highest_by_stop = [0]

    if not animate:
        '''
        Find a cycle where wind/shape/skyline is same
        Calculate the diff between the cycles - and use that to calculate the end result
        '''
        while True:
            # we should update the cycles only when we "froze" a rock
            if prev_stopped != state.num_stopped:
                highest_by_stop.append(state.highest_rock)

                current_state = get_cycle_state(state)
                if current_state in states:
                    human_result = calculate_result(state, states, current_state, highest_by_stop, 2022)
                    elephant_result = calculate_result(state, states, current_state, highest_by_stop, 1000000000000)
                    return human_result, elephant_result

                states[current_state] = (state.num_stopped, state.highest_rock)
                prev_stopped = state.num_stopped

            update_tetris(state, wind)
    else:
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        background_color = pygame.Color('white')
        clock = pygame.time.Clock()
        materials = create_materials()

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # update
            if state.num_stopped == max_rocks:
                running = False

            update_tetris(state, wind)

            # draw
            screen.fill(background_color)
            draw_tetris(state, screen, materials)
            pygame.display.flip()

            clock.tick(15)

        pygame.quit()

    # returning for the case where we animate
    return state.num_stopped, 0


def test():
    wind = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"
    part1, part2 = simulate_tetris(wind, animate=False)
    assert part1 == 3068
    assert part2 == 1514285714288


test()
wind = read_data(2022, 17)
part1, part2 = simulate_tetris(wind, animate=False)
print('Part1:', part1)
print('Part2:', part2)
