from input_processing import read_data, get_numbers_from_lines
import pygame


def parse(data):
    return get_numbers_from_lines(data)


def part1(robots, width, height):
    quadrants = [0, 0, 0, 0]
    mid_x = width // 2
    mid_y = height // 2

    for robot in robots:
        x, y, dx, dy = robot
        x = (x + dx * 100) % width
        y = (y + dy * 100) % height
        if x < mid_x and y < mid_y:
            quadrants[0] += 1
        elif x > mid_x and y < mid_y:
            quadrants[1] += 1
        elif x < mid_x and y > mid_y:
            quadrants[2] += 1
        elif x > mid_x and y > mid_y:
            quadrants[3] += 1

    safety_factor = 1
    for i in range(4):
        safety_factor *= quadrants[i]
    return safety_factor


def part2(robots, width, height):
    image = [['.' for _ in range(width)] for _ in range(height)]
    for robot in robots:
        x, y, dx, dy = robot
        x = (x + dx * 250) % width
        y = (y + dy * 250) % height
        image[y][x] = '#'
    print('\n'.join([''.join(row) for row in image]))
    pygame.init()

    color = (255, 255, 255)
    rect_color = (255, 0, 0)

    # CREATING CANVAS
    canvas = pygame.display.set_mode((505, 515))

    # TITLE OF CANVAS
    pygame.display.set_caption("My game")
    exit = False

    i = 0
    while not exit:
        canvas.fill(color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        if i < 8160:
            for robot in robots:
                x, y, dx, dy = robot
                x = (x + dx * i) % width
                y = (y + dy * i) % height
                pygame.draw.rect(canvas, rect_color, pygame.Rect(x * 5, y * 5, 5, 5))

            i += 1
            pygame.display.update()


def part2_calc(robots, width, height):
    done = False
    time = 0

    while not done:
        next_set = set()
        matching = set()

        for robot in robots:
            x, y, dx, dy = robot
            x = (x + dx * time) % width
            y = (y + dy * time) % height
            if (x, y) in next_set:
                matching.add((x, y))
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    next_set.add((x + dx, y + dy))

        if len(matching) > 256:
            for x in range(100):
                for y in range(101):
                    if (x, y) in next_set:
                        print('#', end='')
                    else:
                        print('.', end='')
                print("")
            print("time:", time)
            done = True
    return time


def test():
    data = '''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3'''
    robots = parse(data)
    assert part1(robots, 11, 7) == 12


test()
data = read_data(2024, 14)
print('Part1:', part1(parse(data), 101, 103))
part2(parse(data), 101, 103)
print('Part2:', part2_calc(parse(data), 101, 103))
