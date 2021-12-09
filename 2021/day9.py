lines = [line.strip() for line in open('2021//input//day9.txt').readlines()]

heights = {(x, y): int(c)
           for y, line in enumerate(lines)
           for x, c in enumerate(line)}


def is_lowest(heights, x, y):
    for diff in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        neighbor = (x + diff[0], y + diff[1])
        if neighbor in heights and heights[neighbor] <= heights[(x, y)]:
            return False
    return True


def get_lowest_points(heights):
    return [heights[(x, y)] for (x, y) in heights if is_lowest(heights, x, y)]


lowest_points = get_lowest_points(heights)
print("Part 1:", sum(lowest_points) + len(lowest_points))
