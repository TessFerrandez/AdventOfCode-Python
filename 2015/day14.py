from typing import List, Tuple
from collections import defaultdict


def parse_input(filename: str) -> List[Tuple[str, int, int, int]]:
    deer = []
    lines = [line.strip() for line in open(filename).readlines()]

    for line in lines:
        parts = line.split(' ')
        deer.append((parts[0], int(parts[3]), int(parts[6]), int(parts[13])))
    return deer


def travel(seconds: int, deer: Tuple[str, int, int, int]) -> List[int]:
    traveled = []
    current_location = 0
    second = 0
    _, speed, fly_time, rest_time = deer
    while second <= seconds:
        for fs in range(fly_time):
            current_location += speed
            traveled.append(current_location)
        for rs in range(rest_time):
            traveled.append(current_location)
        second += 1
    return traveled[: seconds + 1]


def part1(deer: List[Tuple[str, int, int, int]]) -> int:
    max_traveled = 0
    for d in deer:
        max_traveled = max(max_traveled, travel(2503, d)[2503])
    return max_traveled


def part2(deer: List[Tuple[str, int, int, int]]) -> int:
    distances = []
    num_deer = len(deer)
    points = [0] * num_deer
    for d in deer:
        distances.append(travel(2503, d))
    for i in range(2503):
        second_distances = [distances[j][i] for j in range(num_deer)]
        best_distance = max(second_distances)
        leaders = [i for i, distance in enumerate(second_distances) if distance == best_distance]
        for d in leaders:
            points[d] += 1

    return max(points)


def main():
    deer = parse_input('input/day14.txt')
    print(f'Part 1: {part1(deer)}')
    print(f'Part 2: {part2(deer)}')


if __name__ == "__main__":
    main()
