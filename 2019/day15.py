from typing import List
from Computer import Computer, InputInterrupt, OutputInterrupt
import pygame


NORTH, SOUTH, WEST, EAST = 1, 2, 3, 4
WALL, WALKABLE, DROID, ORIGIN, PATH, OXYGEN, BACKGROUND = 0, 1, 2, 3, 4, 5, 6
WALL_STATUS, EMPTY_STATUS, OXYGEN_STATUS = 0, 1, 2
DIRECTIONS = [NORTH, EAST, SOUTH, WEST]
DX = (0, 1, 0, -1)
DY = (-1, 0, 1, 0)
OFFSETS = tuple(zip(DX, DY))
TILE_SIZE = 15


def parse_input(filename: str) -> List[int]:
    return [int(d) for d in open(filename).read().strip().split(',')]


def get_status(droid: Computer, param: int) -> int:
    try:
        droid.run()
    except InputInterrupt:
        droid.inputs.append(param)
    try:
        droid.run()
    except OutputInterrupt:
        return droid.outputs[-1]


def read_events() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return False
    return True


class Game:
    def __init__(self, code: List[int]):
        # set origin to value found from previous runs
        # - to avoid grid shaking
        self.origin = (21, 21)
        self.position = self.origin
        self.found_oxygen = False
        self.world = {self.position: WALKABLE}
        self.path = [self.position]
        self.walkable = set()
        self.droid = Computer(code)
        self.dir_i = 0
        self.x_min = 0
        self.y_min = 0
        self.fully_explored = False
        self.contains_oxygen = set()
        self.check_neighbors = set()
        self.oxygen_minutes = 0

        # set up the game board
        pygame.init()
        self.display = pygame.display.set_mode((615, 615))
        self.colors = {
            WALL: pygame.Color('grey10'),
            WALKABLE: pygame.Color('white'),
            DROID: pygame.Color('firebrick'),
            ORIGIN: pygame.Color('orange'),
            PATH: pygame.Color('lightgreen'),
            OXYGEN: pygame.Color('deepskyblue'),
            BACKGROUND: pygame.Color('grey50')
        }
        self.display.fill(self.colors[BACKGROUND])

    def run_game_loop(self):
        running = True
        while running:
            running = read_events()

            if not self.fully_explored:
                self.explore_new_paths()
            else:
                running = self.fill_oxygen()
            self.draw_screen()
        pygame.quit()

    def draw_screen(self):
        for pos, tile in self.world.items():
            pygame.draw.rect(self.display, self.colors[tile], (pos[0] * TILE_SIZE, pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        for pos in self.path:
            pygame.draw.rect(self.display, self.colors[PATH], (pos[0] * TILE_SIZE, pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        pygame.draw.rect(self.display, self.colors[DROID], (self.position[0] * TILE_SIZE, self.position[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        for pos in self.contains_oxygen:
            pygame.draw.rect(self.display, self.colors[OXYGEN], (pos[0] * TILE_SIZE, pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        pygame.draw.rect(self.display, self.colors[ORIGIN], (self.origin[0] * TILE_SIZE, self.origin[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        pygame.display.flip()

    def explore_new_paths(self):
        new_position = (self.position[0] + DX[self.dir_i], self.position[1] + DY[self.dir_i])
        if new_position == self.origin:
            self.fully_explored = True
            self.walkable = {k for k, v in self.world.items() if v == WALKABLE}

        status = get_status(self.droid, DIRECTIONS[self.dir_i])

        if status == WALL_STATUS:
            self.dir_i = (self.dir_i + 1) % 4
            self.world[new_position] = WALL
        elif status == EMPTY_STATUS or status == OXYGEN_STATUS:
            if new_position in self.world:
                if not self.found_oxygen:
                    self.path.pop()
            else:
                self.world[new_position] = WALKABLE
                if status == OXYGEN_STATUS:
                    self.found_oxygen = True
                    self.contains_oxygen.add(new_position)
                    self.check_neighbors.add(new_position)
                if not self.found_oxygen:
                    self.path.append(new_position)
            self.dir_i = (self.dir_i - 1) % 4
            self.position = new_position
        self.x_min = min(self.x_min, self.position[0])
        self.y_min = min(self.y_min, self.position[1])

    def fill_oxygen(self) -> bool:
        self.oxygen_minutes += 1
        new_check_neighbors = set()
        while self.check_neighbors:
            pos = self.check_neighbors.pop()
            for o in OFFSETS:
                neighbor = (pos[0] + o[0], pos[1] + o[1])
                if self.world.get(neighbor) == WALKABLE and neighbor not in self.contains_oxygen and neighbor not in new_check_neighbors:
                    self.contains_oxygen.add(neighbor)
                    new_check_neighbors.add(neighbor)
        self.check_neighbors = new_check_neighbors
        if self.contains_oxygen == self.walkable:
            return False
        return True


def part1(code: List[int]) -> (int, int):
    game = Game(code)
    game.run_game_loop()
    return len(game.path), game.oxygen_minutes


def main():
    code = parse_input('input/day15.txt')
    path_len, minutes = part1(code)
    print(f'Part 1: {path_len}')
    print(f'Part 2: {minutes}')


if __name__ == "__main__":
    main()
