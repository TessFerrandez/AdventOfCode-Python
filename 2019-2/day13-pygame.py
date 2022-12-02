from ComputerV4 import Computer, InputInterrupt, OutputInterrupt
import numpy as np
import pygame


EMPTY = 0
WALL = 1
BLOCK = 2
PADDLE = 3
BALL = 4

WHITE = (255, 255, 255)

colors = {
    EMPTY: (255, 255, 255),
    WALL: (0, 0, 0),
    BLOCK: (255, 0, 0),
    PADDLE: (0, 255, 0),
    BALL: (0, 0, 255)
}

TILE_WIDTH = 10
SCREEN_WIDTH = 37 * TILE_WIDTH
SCREEN_HEIGHT = 26 * TILE_WIDTH


def play_game(code):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    board = np.zeros((26, 37))
    step = 0
    ball_x = 0
    paddel_x = 0
    score = 0

    computer = Computer(code)
    computer.memory[0] = 2

    while not computer.done:
        screen.fill(WHITE)

        try:
            computer.run()
        except InputInterrupt:
            if ball_x == paddel_x:
                computer.inputs.append(0)
            elif ball_x < paddel_x:
                computer.inputs.append(-1)
            else:
                computer.inputs.append(1)
        except OutputInterrupt:
            step += 1
            if step == 3:
                tile = computer.outputs.pop()
                y = computer.outputs.pop()
                x = computer.outputs.pop()

                if x == -1 and y == 0:
                    score = tile
                else:
                    board[y][x] = tile

                if tile == BALL:
                    ball_x = x
                elif tile == PADDLE:
                    paddel_x = x

                step = 0

        for y in range(26):
            for x in range(37):
                tile_surf = pygame.Surface((TILE_WIDTH, TILE_WIDTH))
                tile_surf.fill(colors[board[y][x]])
                screen.blit(tile_surf, (x * TILE_WIDTH, y * TILE_WIDTH))

        pygame.display.flip()

    pygame.quit()

    return score


code = open('2019/input/day13.txt').read().strip()
score = play_game(code)
print("Part 2:", score)
