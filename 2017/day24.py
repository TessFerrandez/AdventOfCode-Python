from typing import List


def parse_input(filename: str):
    return [[int(d) for d in line.strip().split('/')] for line in open(filename).readlines()]


def get_totals(components: List[List[int]], start: int) -> List[int]:
    totals = []
    possible = [c for c in components if start in c]
    for component in possible:
        components_left = [c for c in components if c != component]
        next_val = component[1] if component[0] == start else component[0]
        totals.append(sum(component))
        for total in get_totals(components_left, next_val):
            totals.append(sum(component) + total)
    return totals


def part1(components: List[List[int]]) -> int:
    return max(get_totals(components, 0))


def get_bridges(components: List[List[int]], start: int):
    bridges = []
    possible = [c for c in components if start in c]
    for component in possible:
        components_left = [c for c in components if c != component]
        next_val = component[1] if component[0] == start else component[0]
        bridges.append([component])
        for bridge in get_bridges(components_left, next_val):
            bridges.append([component] + bridge)
    return bridges


def part2(components: List[List[int]]) -> int:
    bridges = get_bridges(components, 0)
    max_len = max(len(bridge) for bridge in bridges)
    longest_bridges = [bridge for bridge in bridges if len(bridge) == max_len]
    return max([sum([sum(c) for c in bridge]) for bridge in longest_bridges])


def main():
    components = parse_input('input/day24.txt')
    print(f'Part 1: {part1(components)}')
    print(f'Part 2: {part2(components)}')


if __name__ == "__main__":
    main()
