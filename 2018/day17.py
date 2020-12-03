from typing import List, Tuple


def parse_input() -> List[Tuple[int, int]]:
    with open("input/day17.txt") as f:
        lines = [line.strip().split(", ") for line in f.readlines()]

    clay = []
    for line in lines:
        if "x" in line[0]:
            x = int(line[0].split("=")[1])
            from_y, to_y = (int(digit) for digit in line[1].split("=")[1].split(".."))
            for y in range(from_y, to_y + 1):
                clay.append((x, y))
        else:
            y = int(line[0].split("=")[1])
            from_x, to_x = (int(digit) for digit in line[1].split("=")[1].split(".."))
            for x in range(from_x, to_x + 1):
                clay.append((x, y))
    return clay


def draw_ground(clay: List[Tuple[int, int]]):
    min_x, max_x = min(c[0] for c in clay) - 1, max(c[0] for c in clay) + 1
    min_y, max_y = 0, max(c[1] for c in clay)
    x_offset = min_x

    grid = [["." for x in range(min_x, max_x + 1)] for y in range(min_y, max_y + 1)]
    for position in clay:
        grid[position[1]][position[0] - x_offset] = "#"

    for row in grid:
        print("".join(col for col in row))


def main():
    clay = parse_input()
    draw_ground(clay)


if __name__ == "__main__":
    main()
