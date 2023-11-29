from input_processing import read_data_no_strip
import re


RIGHT = 1j
LEFT = -1j
UP = -1
DOWN = 1


def get_faces(map, rows, cols, side_len):
    faces = {}
    face = 0

    for row in range(0, rows, side_len):
        for col in range(0, cols, side_len):
            if col >= len(map[row]):
                break
            if map[row][col] != ' ':
                faces[face] = row + col * 1j
                face += 1

    return faces


def get_map(map_data):
    open = set()
    walls = set()

    for r, row in enumerate(map_data):
        for c, ch in enumerate(row):
            if ch == '.':
                open.add(r + c * 1j)
            elif ch == '#':
                walls.add(r + c * 1j)

    return open, walls


def parse(data, side_len):
    map_data, path_data = data.split('\n\n')
    map_data = map_data.splitlines()

    rows, cols = len(map_data), max(len(row) for row in map_data)
    faces = get_faces(map_data, rows, cols, side_len)
    first_square = map_data[0].index('.') * 1j
    open, walls = get_map(map_data)

    path = re.split(r'([LR])', path_data)
    return path, faces, first_square, open, walls


def part1(path, faces, first_square, open, walls, side_len, test=False):
    def get_folds():
        if test:
            return {
                (0, LEFT): 0,
                (0, UP): 4,
                (0, RIGHT): 0,
                (1, LEFT): 3,
                (1, UP): 1,
                (1, DOWN): 1,
                (2, UP): 2,
                (2, DOWN): 2,
                (3, RIGHT): 1,
                (4, LEFT): 5,
                (4, DOWN): 0,
                (5, UP): 5,
                (5, RIGHT): 4,
                (5, DOWN): 5
            }
        else:
            return {
                (0, LEFT): 1,
                (0, UP): 4,
                (1, UP): 1,
                (1, RIGHT): 0,
                (1, DOWN): 1,
                (2, LEFT): 2,
                (2, RIGHT): 2,
                (3, LEFT): 4,
                (3, UP): 5,
                (4, RIGHT): 3,
                (4, DOWN): 0,
                (5, LEFT): 5,
                (5, DOWN): 3,
                (5, RIGHT): 5
            }

    def get_next_pos(pos, facing):
        row, col = int(pos.real), int(pos.imag)
        face_row = (row // side_len) * side_len
        face_col = (col // side_len) * side_len
        face = pos_to_face[face_row + face_col * 1j]

        next_face = folds[face, facing]
        n_row, n_col = faces[next_face].real, faces[next_face].imag

        if facing == RIGHT:
            new_pos = row + n_col * 1j
        elif facing == LEFT:
            new_pos = row + (n_col + side_len - 1) * 1j
        elif facing == UP:
            new_pos = (n_row + side_len - 1) + col * 1j
        else:
            new_pos = n_row + col * 1j

        return new_pos

    pos_to_face = {v: k for k, v in faces.items()}
    pos = first_square
    facing = RIGHT
    folds = get_folds()

    for cmd in path:
        if cmd == 'L':
            facing *= RIGHT
        elif cmd == 'R':
            facing *= LEFT
        else:
            steps = int(cmd)
            for _ in range(steps):
                next_pos = pos + facing
                if next_pos in open:
                    pos = next_pos
                else:
                    # switch face if we need to
                    next_pos = get_next_pos(pos, facing) if next_pos not in walls else next_pos
                    if next_pos not in walls:
                        pos = next_pos
                    else:
                        break

    row, col = int(pos.real) + 1, int(pos.imag) + 1
    facing_score = {RIGHT: 0, DOWN: 1, LEFT: 2, UP: 3}[facing]
    return row * 1000 + col * 4 + facing_score


def part2(path, faces, first_square, open, walls, side_len, test=False):
    def get_folds():
        if test:
            return {
                (0, LEFT): (2, DOWN),
                (0, UP): (1, DOWN),
                (0, RIGHT): (5, LEFT),
                (1, LEFT): (5, UP),
                (1, UP): (0, DOWN),
                (1, DOWN): (4, UP),
                (2, UP): (0, RIGHT),
                (2, DOWN): (4, RIGHT),
                (3, RIGHT): (5, DOWN),
                (4, LEFT): (2, UP),
                (4, DOWN): (1, UP),
                (5, UP): (3, LEFT),
                (5, RIGHT): (0, LEFT),
                (5, DOWN): (1, RIGHT)
            }
        else:
            return {
                (0, LEFT): (3, RIGHT),
                (0, UP): (5, RIGHT),
                (1, UP): (5, UP),
                (1, RIGHT): (4, LEFT),
                (1, DOWN): (2, LEFT),
                (2, LEFT): (3, DOWN),
                (2, RIGHT): (1, UP),
                (3, LEFT): (0, RIGHT),
                (3, UP): (2, RIGHT),
                (4, RIGHT): (1, LEFT),
                (4, DOWN): (5, LEFT),
                (5, LEFT): (0, DOWN),
                (5, DOWN): (1, DOWN),
                (5, RIGHT): (4, UP)
            }

    def get_next_pos(pos, facing):
        row, col = int(pos.real), int(pos.imag)
        face_row = (row // side_len) * side_len
        face_col = (col // side_len) * side_len
        face = pos_to_face[face_row + face_col * 1j]

        next_face, next_facing = folds[face, facing]
        top_row, left_col = faces[next_face].real, faces[next_face].imag

        row_offset = row % side_len
        col_offset = col % side_len

        if facing == LEFT and next_facing == UP:
            next_row = top_row + side_len - 1
            next_col = left_col + side_len - row_offset - 1
        elif facing == LEFT and next_facing == RIGHT:
            next_row = top_row + side_len - row_offset - 1
            next_col = left_col
        elif facing == LEFT and next_facing == DOWN:
            next_row = top_row
            next_col = left_col + row_offset
        elif facing == RIGHT and next_facing == UP:
            next_row = top_row + side_len - 1
            next_col = left_col + row_offset
        elif facing == RIGHT and next_facing == LEFT:
            next_row = top_row + side_len - row_offset - 1
            next_col = left_col + side_len - 1
        elif facing == RIGHT and next_facing == DOWN:
            next_row = top_row
            next_col = left_col + side_len - row_offset - 1
        elif facing == UP and next_facing == UP:
            next_row = top_row + side_len - 1
            next_col = left_col + col_offset
        elif facing == UP and next_facing == DOWN:
            next_row = top_row
            next_col = left_col + side_len - col_offset - 1
        elif facing == UP and next_facing == LEFT:
            next_row = top_row + side_len - col_offset - 1
            next_col = left_col + side_len - 1
        elif facing == UP and next_facing == RIGHT:
            next_row = top_row + col_offset
            next_col = left_col
        elif facing == DOWN and next_facing == DOWN:
            next_row = top_row
            next_col = left_col + col_offset
        elif facing == DOWN and next_facing == UP:
            next_row = top_row + side_len - 1
            next_col = left_col + side_len - col_offset - 1
        elif facing == DOWN and next_facing == RIGHT:
            next_row = top_row + side_len - col_offset - 1
            next_col = left_col
        elif facing == DOWN and next_facing == LEFT:
            next_row = top_row + col_offset
            next_col = left_col + side_len - 1
        else:
            assert False

        new_pos = next_row + next_col * 1j

        return new_pos, next_facing

    pos_to_face = {v: k for k, v in faces.items()}
    pos = first_square
    facing = RIGHT
    folds = get_folds()

    for cmd in path:
        if cmd == 'L':
            facing *= RIGHT
        elif cmd == 'R':
            facing *= LEFT
        else:
            steps = int(cmd)
            for _ in range(steps):
                next_pos = pos + facing
                if next_pos in open:
                    pos = next_pos
                else:
                    # switch face if we need to
                    if next_pos in walls:
                        next_pos, next_facing = next_pos, facing
                    else:
                        next_pos, next_facing = get_next_pos(pos, facing)

                    if next_pos not in walls:
                        pos = next_pos
                        facing = next_facing
                    else:
                        break

    row, col = int(pos.real) + 1, int(pos.imag) + 1
    facing_score = {RIGHT: 0, DOWN: 1, LEFT: 2, UP: 3}[facing]
    return row * 1000 + col * 4 + facing_score


def test():
    sample = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""
    path, faces, first_square, open, walls = parse(sample, 4)
    assert part1(path, faces, first_square, open, walls, side_len=4, test=True) == 6032
    assert part2(path, faces, first_square, open, walls, side_len=4, test=True) == 5031


test()
path, faces, first_square, open, walls = parse(read_data_no_strip(2022, 22), 50)
print('Part1:', part1(path, faces, first_square, open, walls, side_len=50))
print('Part2:', part2(path, faces, first_square, open, walls, side_len=50))
