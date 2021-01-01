from typing import List, Tuple
from collections import defaultdict


def parse_input(filename: str) -> List[Tuple]:
    return [tuple([int(d) for d in line.strip().split(', ')]) for line in open(filename).readlines()]


def part1(points: List[Tuple[int, int]]) -> int:
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)

    closest = defaultdict(lambda: [])

    # calculate the closest points
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            distances = [abs(y - oy) + abs(x - ox) for ox, oy in points]
            min_distance = min(distances)
            if distances.count(min_distance) == 1:
                closest[points[distances.index(min_distance)]].append((x, y))

    # remove all infinite
    to_remove = []
    for c in closest:
        for x, y in closest[c]:
            if x == min_x or x == max_x or y == min_y or y == max_y:
                to_remove.append(c)
                break

    for r in to_remove:
        del closest[r]

    # calculate largest area
    return max(len(closest[c]) for c in closest)


def part2(points: List[Tuple[int, int]], max_distance) -> int:
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)

    num_points = 0

    # calculate the distances to all points
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            distances = [abs(y - oy) + abs(x - ox) for ox, oy in points]
            total_distance = sum(distances)
            if total_distance < max_distance:
                num_points += 1

    return num_points


def main():
    points = parse_input('input/day6.txt')
    print(f'Part 1: {part1(points)}')
    print(f'Part 2: {part2(points, 10000)}')


if __name__ == "__main__":
    main()
