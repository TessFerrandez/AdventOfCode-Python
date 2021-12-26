from collections import defaultdict


initial_state = '''v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>'''


def read_input():
    area = {}

    x, y = 0, 0
    lines = [line.strip() for line in open('2021/input/day25.txt').readlines()]
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            area[(x, y)] = char

    return area, x + 1, y + 1


def process_step(area, width, height):
    have_moved = False

    # move east-cucumbers
    moves = []
    for pos, char in area.items():
        new_pos = ((pos[0] + 1) % width, pos[1])
        if char == '>' and area[new_pos] == '.':
            moves.append((pos, new_pos))

    for pos, new_pos in moves:
        have_moved = True
        area[new_pos] = '>'
        area[pos] = '.'

    # move down-cucumbers
    moves = []
    for pos, char in area.items():
        new_pos = (pos[0], (pos[1] + 1) % height)
        if char == 'v' and area[new_pos] == '.':
            moves.append((pos, new_pos))

    for pos, new_pos in moves:
        have_moved = True
        area[new_pos] = 'v'
        area[pos] = '.'

    return have_moved


def print_area(area, width, height):
    for y in range(height):
        for x in range(width):
            print(area[(x, y)], end='')
        print()


area, width, height = read_input()
# print_area(area, width, height)
num_steps = 1
while process_step(area, width, height):
    num_steps += 1

print("Part 1:", num_steps)
