from input_processing import read_data


def get_regions(crops):
    visited = set()
    regions = []

    for position, crop in crops.items():
        if position in visited:
             continue
        crop = crops[position]
        region = set()
        queue = [position]
        while queue:
            position = queue.pop()
            if position in visited:
                continue
            visited.add(position)
            region.add(position)
            x, y = position
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                neighbor = (x + dx, y + dy)
                if neighbor in crops and crops[neighbor] == crop:
                    queue.append(neighbor)
        regions.append(region)
    return regions


def parse(data):
    crops = {}
    for y, row in enumerate(data.splitlines()):
        for x, crop in enumerate(row):
                crops[(x, y)] = crop
    return get_regions(crops)


def part1(regions):
    total = 0
    for region in regions:
        size = len(region)
        perimeter = 0
        for x, y in region:
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (x + dx, y + dy) not in region:
                    perimeter += 1
        total += size * perimeter
    return total


def count_sides(perimeters):
    sides = 0
    neighbors = {"top": [(-1, 0), (1, 0)], "bottom": [(-1, 0), (1, 0)], "left": [(0, -1), (0, 1)], "right": [(0, -1), (0, 1)]}
    for perimeter_location, positions in perimeters.items():
        visited = set()
        sections = 0
        for position in positions:
            if position in visited:
                continue
            queue = [position]
            while queue:
                position = queue.pop()
                if position in visited:
                    continue
                visited.add(position)
                x, y = position
                for dx, dy in neighbors[perimeter_location]:
                    neighbor = (x + dx, y + dy)
                    if neighbor in positions and neighbor not in visited:
                        queue.append(neighbor)
            sections += 1
        sides += sections
    return sides


def part2(regions):
    total = 0
    for region in regions:
        size = len(region)
        perimeters = {"top": set(), "bottom": set(), "left": set(), "right": set()}
        for x, y in region:
            if (x, y - 1) not in region:
                perimeters["top"].add((x, y - 1))
            if (x, y + 1) not in region:
                perimeters["bottom"].add((x, y + 1))
            if (x - 1, y) not in region:
                perimeters["left"].add((x - 1, y))
            if (x + 1, y) not in region:
                perimeters["right"].add((x + 1, y))
        sides = count_sides(perimeters)
        total += size * sides
    return total


def test():
    data1 = '''AAAA
BBCD
BBCC
EEEC'''
    data2 = '''OOOOO
OXOXO
OOOOO
OXOXO
OOOOO'''
    data3 = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''
    regions1 = parse(data1)
    regions2 = parse(data2)
    assert part1(regions1) == 140
    assert part1(regions2) == 772
    assert part1(parse(data3)) == 1930
    assert part2(regions1) == 80
    assert part2(regions2) == 436


test()
data = read_data(2024, 12)
regions = parse(data)
print('Part1:', part1(regions))
print('Part2:', part2(regions))
