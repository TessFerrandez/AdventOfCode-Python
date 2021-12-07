from typing import List


def calculate_cost(steps: int) -> int:
    return (steps * (steps + 1)) // 2


def fuel_required(positions: List[int]) -> List[int]:
    fuel: List[int] = []
    min_pos = min(positions)
    max_pos = max(positions)

    for current_pos in range(min_pos, max_pos + 1):
        fuel.append(sum(abs(position - current_pos) for position in positions))

    return fuel


def fuel_required2(positions: List[int]) -> List[int]:
    fuel: List[int] = []
    min_pos = min(positions)
    max_pos = max(positions)

    for current_pos in range(min_pos, max_pos + 1):
        fuel.append(sum(calculate_cost(abs(position - current_pos)) for position in positions))

    return fuel


positions = [int(pos) for pos in open('2021//input//day7.txt').readline().split(',')]
print("Part 1:", min(fuel_required(positions)))
print("Part 2:", min(fuel_required2(positions)))
