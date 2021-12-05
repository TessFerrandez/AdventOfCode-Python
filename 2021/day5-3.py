from collections import defaultdict


lines = [line.strip().split(' -> ') for line in open('2021/input/day5.txt').readlines()]

cells = defaultdict(lambda: 0)

for line in lines:
    x1, y1 = [int(n) for n in line[0].split(',')]
    x2, y2 = [int(n) for n in line[1].split(',')]
    steps = max(abs(x1 - x2), abs(y1 - y2))

    dx = 0 if x1 == x2 else 1 if x1 < x2 else -1
    dy = 0 if y1 == y2 else 1 if y1 < y2 else -1

    x, y = x1, y1

    for i in range(steps + 1):
        cells[(x, y)] += 1
        x += dx
        y += dy

print(sum(1 for c in cells.values() if c > 1))
