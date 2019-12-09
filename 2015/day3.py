def deliver_gifts(path):
    visited = [(0, 0)]
    x = 0
    y = 0
    for direction in path:
        if direction == ">":
            x += 1
        elif direction == "<":
            x -= 1
        elif direction == "^":
            y += 1
        else:
            y -= 1
        visited.append((x, y))
    unique_visited = list(set(visited))
    return unique_visited


def puzzle1():
    print("Day 3 - Puzzle 1")
    houses_visited = deliver_gifts(open("input/day3.txt").read())
    print("houses visited: ", len(houses_visited))


def puzzle2():
    print("Day 3 - Puzzle 2")
    path = open("input/day3.txt").read()
    houses_visited = deliver_gifts(path[::2])
    robo_houses_visited = deliver_gifts(path[1::2])
    print("houses visited: ", len(set(houses_visited + robo_houses_visited)))


if __name__ == "__main__":
    puzzle1()
    puzzle2()
