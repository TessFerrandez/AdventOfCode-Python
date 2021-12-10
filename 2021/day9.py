from collections import Counter


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


heights = {(x, y): int(c)
           for y, line in enumerate(lines)
           for x, c in enumerate(line)}


def merge(regions: dict, region1: int, region2: int):
    for region in regions:
        if regions[region] == region1:
            regions[region] = region2


def calculate_largest_basins(heights) -> int:
    regions = {location: region_number for region_number, location in enumerate(heights) if heights[location] != 9}
    for x, y in regions:
        if (x - 1, y) in regions:
            merge(regions, regions[(x - 1, y)], regions[(x, y)])
        if (x, y - 1) in regions:
            merge(regions, regions[(x, y - 1)], regions[(x, y)])

    basin_sizes = [size[1] for size in Counter(regions.values()).most_common(3)]
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


lowest_points = get_lowest_points(heights)
print("Part 1:", sum(lowest_points) + len(lowest_points))
print("Part 2:", calculate_largest_basins(heights))
