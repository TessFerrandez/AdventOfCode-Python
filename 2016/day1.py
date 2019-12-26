def parse_input():
    return open("input/day1.txt").readline().split(", ")


def calculate_distance(moves):
    x, y = 0, 0
    visited = []

    dx, dy = 0, 1
    for move in moves:
        direction = move[0]
        if direction == "R":
            if dx == 0 and dy == 1:
                dx, dy = 1, 0
            elif dx == 1 and dy == 0:
                dx, dy = 0, -1
            elif dx == 0 and dy == -1:
                dx, dy = -1, 0
            else:
                dx, dy = 0, 1
        else:
            if dx == 0 and dy == 1:
                dx, dy = -1, 0
            elif dx == 1 and dy == 0:
                dx, dy = 0, 1
            elif dx == 0 and dy == -1:
                dx, dy = 1, 0
            else:
                dx, dy = 0, -1

        steps = int(move[1:])
        for i in range(0, steps):
            x += dx
            y += dy
            visited.append((x, y))

    return abs(x) + abs(y), visited


def puzzles():
    moves = parse_input()
    distance, visited = calculate_distance(moves)
    print("Easter Bunny HQ is", distance, "blocks away")

    for location in visited:
        if visited.count(location) > 1:
            print(
                "first location visited twice is",
                abs(location[0]) + abs(location[1]),
                "steps away",
            )
            return


if __name__ == "__main__":
    puzzles()
