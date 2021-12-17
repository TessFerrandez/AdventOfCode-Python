def probe(dx, dy):
    x, y = 0, 0

    while x <= max_x and y >= min_y:
        x += dx
        y += dy

        if min_x <= x <= max_x and min_y <= y <= max_y:
            return True

        dx = max(0, dx - 1)
        dy -= 1

    return False


min_x, max_x = 14, 50
min_y, max_y = -267, -225
depth = abs(min_y) - 1

print("Part 1:", (depth + 1) * depth // 2)
print("Part 2:", sum(1 for x in range(max_x + 1) for y in range(min_y, abs(min_y) + 1) if probe(x, y)))
