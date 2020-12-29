from collections import defaultdict


def parse_input(filename: str) -> dict:
    programs = defaultdict(lambda: set())
    lines = [line.strip() for line in open(filename).readlines()]
    for line in lines:
        p1, p2 = line.split(' <-> ')
        p1 = int(p1)
        p2s = [int(d) for d in p2.split(', ')]
        programs[p1].add(p1)
        for p in p2s:
            programs[p1].add(p)
            programs[p].add(p1)
    return dict(programs)


def get_group(programs: dict, item: int) -> dict:
    group = set()
    group.add(item)
    todo = [item]

    while todo:
        current = todo.pop(0)
        group.add(current)
        for p in programs[current]:
            if p not in group:
                todo.append(p)
    return group


def part1(programs: dict) -> int:
    group = get_group(programs, 0)
    return len(group)


def part2(programs: dict) -> int:
    numbers = list(programs.keys())
    num_groups = 0
    while numbers:
        num_groups += 1
        base = numbers.pop(0)
        group = get_group(programs, base)
        for item in group:
            if item in numbers:
                numbers.remove(item)
    return num_groups


def main():
    programs = parse_input('input/day12.txt')
    print(f'Part 1: {part1(programs)}')
    print(f'Part 2: {part2(programs)}')


if __name__ == "__main__":
    main()
