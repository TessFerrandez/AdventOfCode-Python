from input_processing import read_data


def parse(data):
    warehouse, moves = data.split('\n\n')
    moves = ''.join(moves.splitlines())
    warehouse, robot = [list(line) for line in warehouse.split()], warehouse.index('@')
    x, y = robot % (len(warehouse[0]) + 1), robot // (len(warehouse[0]) + 1)
    warehouse[y][x] = '.'

    return warehouse, (x, y), moves


def parse2(data):
    warehouse, moves = data.split('\n\n')
    moves = ''.join(moves.splitlines())
    warehouse = [[('[' if i % 2 == 0 else ']') if line[i // 2] == 'O' else line[i // 2] for i in range(len(line) * 2)] for line in warehouse.split()]
    for y, row in enumerate(warehouse):
        if '@' in row:
            x = row.index('@')
            break
    robot = (x, y)
    warehouse[y][x] = '.'
    warehouse[y][x + 1] = '.'

    return warehouse, robot, moves


def part1(warehouse, robot, moves):
    directions = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
    x, y = robot
    for move in moves:
        x1, y1 = x + directions[move][0], y + directions[move][1]
        while warehouse[y1][x1] == 'O':
            x1, y1 = x1 + directions[move][0], y1 + directions[move][1]
        if warehouse[y1][x1] == '.':  # Empty space
            if abs(y1 - y + x1 - x) > 1:
                warehouse[y1][x1] = 'O'
                warehouse[y + directions[move][1]][x + directions[move][0]] = '.'
            x, y = x + directions[move][0], y + directions[move][1]

    for row in warehouse:
        print(''.join(row))

    return sum([100 * y + x for y, row in enumerate(warehouse) for x, cell in enumerate(row) if cell == 'O'])


def part2(warehouse, robot, moves):
    x, y = robot
    directions = {'>': 1, '<': -1, '^': -1, 'v': 1}
    for move in ''.join(moves.split()):
        if move in ['>', '<']:
            x1 = x + (directions[move])
            while warehouse[y][x1] in ['[', ']']: x1 += directions[move]
            if warehouse[y][x1] == '.':
                for x2 in range(x1, x, -directions[move]): warehouse[y][x2] = warehouse[y][x2 - directions[move]]
                x += directions[move]
        else:
            boxes = [{(x, y)}]
            while boxes[-1]:
                boxes.append(set())
                for box in boxes[-2]:
                    if warehouse[box[1] + directions[move]][box[0]] == '#': break
                    if warehouse[box[1] + directions[move]][box[0]] == '[': boxes[-1] |= {(box[0], box[1] + directions[move]), (box[0] + 1, box[1] + directions[move])}
                    elif warehouse[box[1] + directions[move]][box[0]] == ']': boxes[-1] |= {(box[0], box[1] + directions[move]), (box[0] - 1, box[1] + directions[move])}
                else: continue
                break
            else:
                for row in list(reversed(boxes)):
                    for box in row: warehouse[box[1] + directions[move]][box[0]], warehouse[box[1]][box[0]] = warehouse[box[1]][box[0]], '.'
                y += directions[move]

    return sum([100 * i + j for i, line in enumerate(warehouse) for j, c in enumerate(line) if c == '['])


def test():
    data = '''########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<'''
    warehouse, robot, moves = parse(data)
    assert part1(warehouse, robot, moves) == 2028
    data = '''##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^'''
    warehouse, robot, moves = parse(data)
    assert part1(warehouse, robot, moves) == 10092

    warehouse, robot, moves = parse2(data)
    assert part2(warehouse, robot, moves) == 9021


test()
data = read_data(2024, 15)
warehouse, robot, moves = parse(data)
print('Part1:', part1(warehouse, robot, moves))
warehouse, robot, moves = parse2(data)
print('Part2:', part2(warehouse, robot, moves))
