import pytest


@pytest.mark.parametrize('data, expected',
                         [
                             ('>', 2),
                             ('^>v<', 4),
                             ('^v^v^v^v^v', 2),
                         ])
def test_part1(data: str, expected: int):
    assert part1(data) == expected


@pytest.mark.parametrize('data, expected',
                         [
                             ('^v', 3),
                             ('^>v<', 3),
                             ('^v^v^v^v^v', 11),
                         ])
def test_part2(data: str, expected: int):
    assert part2(data) == expected


def parse_input(filename: str):
    return open(filename).read().strip()


def deliver_packages(moves: str) -> set:
    directions = {'>': 1, '<': -1, '^': -1j, 'v': 1j}

    houses = set()
    houses.add(0)

    current = 0
    for move in moves:
        current = current + directions[move]
        houses.add(current)

    return houses


def part1(data: str) -> int:
    return len(deliver_packages(data))


def part2(data: str) -> int:
    robot1_houses = deliver_packages(data[::2])
    robot2_houses = deliver_packages(data[1::2])
    all_houses = robot1_houses.union(robot2_houses)
    return len(all_houses)


def main():
    data = parse_input('input/day3.txt')
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == "__main__":
    main()
