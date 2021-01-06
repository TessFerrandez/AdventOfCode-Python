from typing import List


def parse_input(filename: str) -> List[int]:
    return [int(d.strip()) for d in open(filename).readlines()]


def part1(modules: List[int]) -> int:
    return sum(module // 3 - 2 for module in modules)


def get_fuel_needed(module: int) -> int:
    total_fuel = 0

    remaining_fuel = module // 3 - 2
    while remaining_fuel > 0:
        total_fuel += remaining_fuel
        remaining_fuel = remaining_fuel // 3 - 2

    return total_fuel


def part2(modules: List[int]) -> int:
    return sum(get_fuel_needed(module) for module in modules)


def main():
    modules = parse_input('input/day1.txt')
    print(f'Part 1: {part1(modules)}')
    print(f'Part 2: {part2(modules)}')


if __name__ == "__main__":
    main()
