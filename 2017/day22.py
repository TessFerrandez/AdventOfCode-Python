grid = {}
dirs = {
    ((0, 1), "R"): (-1, 0),
    ((0, 1), "L"): (1, 0),
    ((0, -1), "R"): (1, 0),
    ((0, -1), "L"): (-1, 0),
    ((1, 0), "R"): (0, 1),
    ((1, 0), "L"): (0, -1),
    ((-1, 0), "R"): (0, -1),
    ((-1, 0), "L"): (0, 1),
}


def read_input() -> (int, int):
    lines = [line.strip() for line in open("input/day22.txt").readlines()]
    w = len(lines[0])
    for y in range(w):
        for x in range(w):
            grid[(x, y)] = lines[y][x]
    return w // 2, w // 2


def puzzle1():
    x, y = read_input()
    current_pos = (x, y)
    current_dir = (0, -1)
    count_infections = 0
    for i in range(10000):
        if current_pos in grid and grid[current_pos] == "#":
            grid[current_pos] = "."
            current_dir = dirs[(current_dir, "R")]
        else:
            count_infections += 1
            grid[current_pos] = "#"
            current_dir = dirs[(current_dir, "L")]
        x2, y2 = current_pos[0] + current_dir[0], current_pos[1] + current_dir[1]
        current_pos = (x2, y2)
    print("infections:", count_infections)


def puzzle2():
    grid.clear()
    x, y = read_input()
    current_pos = (x, y)
    current_dir = (0, -1)
    count_infections = 0
    for i in range(10000000):
        if current_pos in grid:
            if grid[current_pos] == "#":
                grid[current_pos] = "F"
                current_dir = dirs[(current_dir, "R")]
            elif grid[current_pos] == "F":
                grid[current_pos] = "."
                current_dir = (-current_dir[0], -current_dir[1])
            elif grid[current_pos] == "W":
                count_infections += 1
                grid[current_pos] = "#"
            else:
                grid[current_pos] = "W"
                current_dir = dirs[(current_dir, "L")]
        else:
            grid[current_pos] = "W"
            current_dir = dirs[(current_dir, "L")]
        x2, y2 = current_pos[0] + current_dir[0], current_pos[1] + current_dir[1]
        current_pos = (x2, y2)
    print("infections:", count_infections)


if __name__ == "__main__":
    puzzle1()
    puzzle2()
