from input_processing import read_data


def parse(data):
    data = data.splitlines()
    obstacles = set()
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '#':
                obstacles.add((x, y))
            elif char == '^':
                start = (x, y)
    width = len(data[0])
    height = len(data)
    return obstacles, start, width, height


def get_guard_positions(obstacles, start, width, height):
    visited = set()
    x, y = start
    direction = -1j

    while 0 <= x < width and 0 <= y < height:
        visited.add((x, y))
        next_pos = (x + direction.real, y + direction.imag)
        while next_pos in obstacles:
            # turn right
            direction = direction * 1j
            next_pos = (x + direction.real, y + direction.imag)
        x, y = next_pos

    return visited


def is_loop(obstacles, start, width, height):
    visited = set()
    x, y = start
    direction = -1j

    while 0 <= x < width and 0 <= y < height:
        if ((x, y), direction) in visited:
            return True
        visited.add(((x, y), direction))
        next_pos = (x + direction.real, y + direction.imag)
        while next_pos in obstacles:
            # turn right
            direction = direction * 1j
            next_pos = (x + direction.real, y + direction.imag)
        x, y = next_pos

    return False


def part1(obstacles, start, width, height):
    return len(get_guard_positions(obstacles, start, width, height))


def part2(obstacles, start, width, height):
    guard_positions = get_guard_positions(obstacles, start, width, height)
    guard_positions.remove(start)

    good_positions = set()
    i = 0
    for position in guard_positions:
        i += 1
        if i % 100 == 0:
            print(".", end="")
        obstacles.add(position)
        if is_loop(obstacles, start, width, height):
            good_positions.add(position)
        obstacles.remove(position)
    print()

    return len(good_positions)


def test():
    data = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''
    obstacles, start, width, height = parse(data)
    assert part1(obstacles, start, width, height) == 41
    assert part2(obstacles, start, width, height) == 6

test()
data = read_data(2024, 6)
obstacles, start, width, height = parse(data)
print('Part1:', part1(obstacles, start, width, height))
print('Part2:', part2(obstacles, start, width, height))
