import pygame
from input_processing import read_data


def parse(data):
    instructions = []
    for row in data.splitlines():
        direction, distance, color = row.split()
        color = color[1:-1]
        instructions.append((direction, int(distance), color))
    return instructions


step = {'R': 1, 'L': -1, 'U': -1j, 'D': 1j}


def create_grid(instructions):
    current = 0
    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0

    grid = {current: '#FFFFFF'}

    for direction, distance, color in instructions:
        for _ in range(distance):
            current += step[direction]
            max_x = max(max_x, current.real)
            min_x = min(min_x, current.real)
            max_y = max(max_y, current.imag)
            min_y = min(min_y, current.imag)
            grid[current] = color

    offset_x = -min_x
    offset_y = -min_y

    offset_grid = {}

    for pos in grid:
        offset_grid[pos + offset_x + offset_y * 1j] = grid[pos]

    return offset_grid, int(max_x - min_x), int(max_y - min_y)


def pygame_print(grid, fill, max_x, max_y, scale=10, print_color=False):
    import os
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50, 50)
    pygame.init()

    screen = pygame.display.set_mode(((max_x + 1) * scale, (max_y + 1) * scale))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        for pos in grid:
            x, y = pos.real, pos.imag
            surface = pygame.Surface((scale, scale))
            if print_color:
                color = grid[pos]
                r = int(color[1:3], 16)
                g = int(color[3:5], 16)
                b = int(color[5:7], 16)
            else:
                r = g = b = 20
            surface.fill((r, g, b))
            screen.blit(surface, (int(x) * scale, int(y) * scale))

        for pos in fill:
            x, y = pos.real, pos.imag
            surface = pygame.Surface((scale, scale))
            r = g = b = 100
            surface.fill((r, g, b))
            screen.blit(surface, (int(x) * scale, int(y) * scale))

        # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

        pygame.display.flip()

    pygame.quit()


def find_first_in_loop(grid, max_x, max_y):
    for x in range(1, max_x):
        if x + 1j not in grid and x in grid:
            return x + 1j


def flood_fill(grid, start):
    queue = [start]
    seen = set()
    while queue:
        pos = queue.pop()
        if pos in seen:
            continue
        seen.add(pos)
        for direction in step.values():
            new_pos = pos + direction
            if new_pos not in grid:
                queue.append(new_pos)
    return seen


def part1(instructions, large=False, do_print=False):
    grid, max_x, max_y = create_grid(instructions)
    start = find_first_in_loop(grid, max_x, max_y)
    fill = flood_fill(grid, start)
    if do_print:
        if not large:
            pygame_print(grid, fill, max_x, max_y, 100, print_color=False)
        else:
            pygame_print(grid, fill, max_x, max_y, 4)
    return len(fill) + len(grid)


# trying to get smart about inside and outside
# by keeping track of the min and max of each row
# but this doesn't work for the real data
def part1_v2(instructions):
    min_x, min_y = (0, 0)
    max_x, max_y = (0, 0)

    current_col, current_row = (0, 0)
    rows = {}

    for direction, distance, _ in instructions:
        if direction == 'R':
            min_col, max_col = current_col, current_col + distance
            if current_row not in rows:
                rows[current_row] = (min_col, max_col)
            else:
                rows[current_row] = (min(min_col, rows[current_row][0]), max(max_col, rows[current_row][1]))
            current_col += distance
        elif direction == 'L':
            min_col, max_col = current_col - distance, current_col
            if current_row not in rows:
                rows[current_row] = (min_col, max_col)
            else:
                rows[current_row] = (min(min_col, rows[current_row][0]), max(max_col, rows[current_row][1]))
            current_col -= distance
        elif direction == 'U':
            for _ in range(distance):
                current_row -= 1
                if current_row not in rows:
                    rows[current_row] = (current_col, current_col)
                else:
                    rows[current_row] = (min(current_col, rows[current_row][0]), max(current_col, rows[current_row][1]))
        elif direction == 'D':
            for _ in range(distance):
                current_row += 1
                if current_row not in rows:
                    rows[current_row] = (current_col, current_col)
                else:
                    rows[current_row] = (min(current_col, rows[current_row][0]), max(current_col, rows[current_row][1]))
        min_x, max_x = min(min_x, current_col), max(max_x, current_col)
        min_y, max_y = min(min_y, current_row), max(max_y, current_row)

    total_outside = 0
    for row in rows:
        min_col, max_col = rows[row]
        outside = abs(min_col - min_x) + abs(max_x - max_col)
        total_outside += outside

    grid_area = (max_x - min_x + 1) * (max_y - min_y + 1)
    return grid_area - total_outside


def get_xs_ys(instructions):
    x, y = (0, 0)
    xs = [x]
    ys = [y]

    outline = 0

    for direction, distance, _ in instructions:
        if direction == 'R':
            x += distance
        elif direction == 'L':
            x -= distance
        elif direction == 'U':
            y -= distance
        elif direction == 'D':
            y += distance
        outline += distance
        xs.append(x)
        ys.append(y)

    return xs, ys, outline


def get_xs_ys_part2(instructions):
    x, y = (0, 0)
    xs = [x]
    ys = [y]

    outline = 0

    for _, _, color in instructions:
        distance, direction = int(color[1:6], 16), {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}[color[6]]
        if direction == 'R':
            x += distance
        elif direction == 'L':
            x -= distance
        elif direction == 'U':
            y -= distance
        elif direction == 'D':
            y += distance
        outline += distance
        xs.append(x)
        ys.append(y)

    return xs, ys, outline


# using shoe lace formula
def part1_v3(instructions):
    xs, ys, outline = get_xs_ys(instructions)
    area_inside = 0.5 * abs(sum(x * y for x, y in zip(xs, ys[1:] + ys[:1])) - sum(x * y for x, y in zip(xs[1:] + xs[:1], ys)))

    return (outline // 2 + 1) + int(area_inside)


def part2(instructions):
    xs, ys, outline = get_xs_ys_part2(instructions)
    area_inside = 0.5 * abs(sum(x * y for x, y in zip(xs, ys[1:] + ys[:1])) - sum(x * y for x, y in zip(xs[1:] + xs[:1], ys)))
    return (outline // 2 + 1) + int(area_inside)


def test():
    sample = '''R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)'''
    instructions = parse(sample)
    assert part1(instructions, large=False, do_print=False) == 62
    # assert part1_v2(instructions) == 62
    assert part1_v3(instructions) == 62
    assert part2(instructions) == 952408144115


test()
data = read_data(2023, 18)
# print('Part1:', part1(parse(data), large=True, do_print=False))
print('Part1:', part1_v3(parse(data)))
print('Part2:', part2(parse(data)))
