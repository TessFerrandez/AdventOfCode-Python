def read_input() -> list:
    lines = [line.strip() for line in open("input/day22.txt").readlines()][2:]
    nodes = []
    for line in lines:
        parts = line.split()
        _, x, y = parts[0].split("-")
        x, y = int(x[1:]), int(y[1:])
        size, used, avail, use_pct = [int(p[:-1]) for p in parts[1:]]
        nodes.append([(x, y), size, used, avail, use_pct])
    return nodes


def get_available_pairs(nodes: list) -> list:
    available = []
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if i != j and nodes[i][2] != 0 and nodes[i][2] < nodes[j][3]:
                available.append([nodes[i][0], nodes[j][0]])
    return available


def print_grid(nodes: list):
    grid = [[0 for i in range(30)] for j in range(35)]
    for node in nodes:
        x, y = node[0]
        if x == 0 and y == 0:
            marker = "!"
        elif x == 29 and y == 0:
            marker = "G"
        elif node[2] == 0:
            marker = "-"
        elif node[1] > 100:
            marker = "#"
        else:
            marker = "."
        grid[y][x] = marker

    for row in grid:
        print("".join(row))


def puzzles():
    nodes = read_input()
    available_pairs = get_available_pairs(nodes)
    print("available:", len(available_pairs))
    print_grid(nodes)
    empty_node = next(node for node in nodes if node[2] == 0)
    # print(empty_node)
    x, y = empty_node[0]
    # 1. move empty to top row (x + y steps)
    # 2. move empty to G - 29 steps
    # .G_
    # ...
    # 3. shift G one over 28 times (takes 5 steps per time)
    # G_.
    # ...
    print("steps needed:", x + y + 29 + (29 - 1) * 5)


if __name__ == "__main__":
    puzzles()
