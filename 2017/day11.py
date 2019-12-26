moves = {
    "n": (0, 1),
    "ne": (0.5, 0.5),
    "nw": (-0.5, 0.5),
    "s": (0, -1),
    "se": (0.5, -0.5),
    "sw": (-0.5, -0.5),
}


def do_moves(input_steps: list) -> (int, int):
    max_dist = 0
    x, y = 0.0, 0.0
    for step in input_steps:
        x += moves[step][0]
        y += moves[step][1]
        dist = abs(x) + abs(y)
        max_dist = max(max_dist, dist)

    end_dist = abs(x) + abs(y)
    return int(end_dist), int(max_dist)


def puzzles():
    input_steps = open("input/day11.txt").read().strip().split(",")
    end_dist, max_dist = do_moves(input_steps)
    print("end distance:", end_dist)
    print("max distance:", max_dist)


if __name__ == "__main__":
    puzzles()
