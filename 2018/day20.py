from collections import defaultdict


D = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}


def parse_input(filename: str) -> str:
    return open(filename).read().strip()[1: -1]


def part1(path: str) -> int:
    positions = []
    distances = defaultdict(int)
    x, y = 0, 0
    prev_x, prev_y = x, y

    for ch in path:
        if ch == '(':
            positions.append((x, y))
        elif ch == ')':
            x, y = positions.pop()
        elif ch == '|':
            x, y = positions[-1]
        else:
            dx, dy = D[ch]
            x += dx
            y += dy
            if distances[(x, y)] != 0:
                distances[(x, y)] = min(distances[(x, y)], distances[(prev_x, prev_y)] + 1)
            else:
                distances[(x, y)] = distances[(prev_x, prev_y)] + 1
        prev_x, prev_y = x, y

    return max(distances.values())


def part2(path: str) -> int:
    positions = []
    distances = defaultdict(int)
    x, y = 0, 0
    prev_x, prev_y = x, y

    for ch in path:
        if ch == '(':
            positions.append((x, y))
        elif ch == ')':
            x, y = positions.pop()
        elif ch == '|':
            x, y = positions[-1]
        else:
            dx, dy = D[ch]
            x += dx
            y += dy
            if distances[(x, y)] != 0:
                distances[(x, y)] = min(distances[(x, y)], distances[(prev_x, prev_y)] + 1)
            else:
                distances[(x, y)] = distances[(prev_x, prev_y)] + 1
        prev_x, prev_y = x, y

    return len([distance for distance in distances if distances[distance] >= 1000])


def main():
    path = parse_input('input/day20.txt')
    print(f'Part 1: {part1(path)}')
    print(f'Part 2: {part2(path)}')


if __name__ == "__main__":
    main()
