# solution from p88h
from input_processing import read_data


def get_start(grid):
    for y in range(len(grid)):
        if "S" in grid[y]:
            x = grid[y].find("S")
            return (y, x)


def get_loop(grid):
    mapping = {
        "-": [(0, 1), (0, -1)],
        "|": [(1, 0), (-1, 0)],
        "L": [(0, 1), (-1, 0)],
        "F": [(0, 1), (1, 0)],
        "7": [(0, -1), (1, 0)],
        "J": [(0, -1), (-1, 0)],
    }

    loop = set()

    start = get_start(grid)
    y, x = start
    loop.add(start)

    if grid[y][x + 1] in ("J", "-", "7"):
        current = (y, x + 1)
    elif grid[y][x - 1] in ("L", "-", "F"):
        current = (y, x - 1)
    elif grid[y - 1][x] in ("|", "F", "7"):
        current = (y - 1, x)
    elif grid[y + 1][x] in ("|", "L", "J"):
        current = (y + 1, x)

    prev = start
    while current != start:
        loop.add(current)
        (y, x) = current
        char = grid[y][x]
        for dy, dx in mapping[char]:
            next = (y + dy, x + dx)
            if next != prev:
                prev = current
                current = next
                break

    return loop


def part1(loop):
    return len(loop) // 2


def part2(loop, grid):
    count = 0
    skip = " "
    for y, row in enumerate(grid):
        out = True
        for x, ch in enumerate(row):
            if (y, x) in loop:
                # start of the fence, maybe
                if ch == "F":
                    skip = "7"
                elif ch == "L":
                    skip = "J"
                elif ch == "-":
                    # walking along the fence, whatever.
                    continue
                else:
                    # equivalent to "|" now
                    if ch != skip:
                        out = not out
                    # stop walking along the fence
                    skip = " "
            elif not out:
                count += 1
    return count


def test():
    sample = '''7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ'''.splitlines()
    loop = get_loop(sample)
    assert part1(loop) == 8
    sample2 = '''...........
.S-------7.
.|F-----7|.
.||OOOOO||.
.||OOOOO||.
.|L-7OF-J|.
.|II|O|II|.
.L--JOL--J.
.....O.....'''.splitlines()
    loop = get_loop(sample2)
    assert part2(loop, sample2) == 4


test()
grid = read_data(2023, 10).splitlines()
loop = get_loop(grid)
print("Part1:", part1(loop))
print("Part2:", part2(loop, grid))
