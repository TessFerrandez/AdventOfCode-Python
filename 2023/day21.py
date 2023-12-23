from input_processing import read_data


def parse(data):
    rocks = set()

    for r, row in enumerate(data.splitlines()):
        for c, col in enumerate(row):
            if col == '#':
                rocks.add(r + c * 1j)
            elif col == 'S':
                start = (r + c * 1j)

    return rocks, start


def part1(rocks, start, steps=64):
    positions = set()
    positions.add(start)

    for _ in range(steps):
        next_positions = set()
        for position in positions:
            for direction in [1, -1, 1j, -1j]:
                new_position = position + direction
                if new_position not in rocks:
                    next_positions.add(new_position)
        positions = next_positions

    return len(positions)


# based on solution from 4HbQ - fit a quadratic function to the data
def part2(data):
    rows = data.splitlines()
    size = len(rows)

    gardens = {r + c * 1j: ch
               for r, row in enumerate(rows)
               for c, ch in enumerate(row)
               if ch in '.S'}

    done = []
    positions = {position for position in gardens if gardens[position] == 'S'}

    for step in range(int(2.5 * size) + 1):
        if step == 64:
            print("64 steps", len(positions))
        if step % size == size // 2:
            n_positions = len(positions)
            print(f"{step} steps: {n_positions}")
            done.append(n_positions)

        positions = {position + direction
                     for direction in {1, -1, 1j, -1j}
                     for position in positions
                     if (position + direction).real % size + (position + direction).imag % size * 1j in gardens}

    # create a quadratic function from the last 3 values
    def f(n, a, b, c):
        return a + n * (b - a) + n * (n - 1) // 2 * ((c - b) - (b - a))

    return f(26501365 // size, *done)


def test():
    sample = '''...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........'''
    rocks, start = parse(sample)
    assert part1(rocks, start, 6) == 16
    # part2(rocks, start, rows, cols)


test()
data = read_data(2023, 21)
rocks, start = parse(data)
print('Part1:', part1(rocks, start))
print('Part2:', part2(data))
