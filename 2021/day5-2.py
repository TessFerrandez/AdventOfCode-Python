from collections import defaultdict


lines = [line.strip().split(' -> ') for line in open('2021/input/day5.txt').readlines()]

cells = defaultdict(lambda: 0)

for line in lines:
    x1, y1 = [int(n) for n in line[0].split(',')]
    x2, y2 = [int(n) for n in line[1].split(',')]

    if x1 == x2 and y1 != y2:
        minY, maxY = min(y1, y2), max(y1, y2)
        for y in range(minY, maxY + 1):
            cells[(x1, y)] += 1
    elif x1 != x2 and y1 == y2:
        minX, maxX = min(x1, x2), max(x1, x2)
        for x in range(minX, maxX + 1):
            cells[(x, y1)] += 1
    else:
        dx = 0 if x1 == x2 else 1 if x1 < x2 else -1
        dy = 0 if y1 == y2 else 1 if y1 < y2 else -1
        x, y = x1, y1
        for i in range(abs(x1 - x2) + 1):
            cells[(x, y)] += 1
            x += dx
            y += dy

print(sum(1 for c in cells.values() if c > 1))
