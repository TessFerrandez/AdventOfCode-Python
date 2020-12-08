import pytest
import json
from common.helpers import extract_numbers


@pytest.mark.parametrize('data, expected',
                         [
                             ('[1,2,3]', 6),
                             ('{"a":2,"b":4}', 6),
                             ('[[[3]]]', 3),
                             ('{"a":{"b":4},"c":-1}', 3),
                             ('{"a":[-1,1]}', 0),
                             ('[-1,{"a":1}]', 0),
                             ('[]', 0),
                             ('{}', 0),
                         ])
def test_part1(data: str, expected: int):
    assert part1(data) == expected


@pytest.mark.parametrize('data, expected',
                         [
                             ('[1,2,3]', 6),
                             ('[1,{"c":"red","b":2},3]', 4),
                             ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
                             ('[1,"red",5]', 6),
                         ])
def test_part2(data: str, expected: int):
    assert part2(data) == expected


def parse_input(filename: str):
    return open(filename).read()


def part1(data: str) -> int:
    return sum(extract_numbers(data))


def evaluate(data: any) -> int:
    if type(data) == int:
        return data
    if type(data) == list:
        return sum([evaluate(d) for d in data])
    if type(data) == dict and 'red' not in data.values():
        return evaluate(list(data.values()))
    return 0


def part2(data: str) -> int:
    return evaluate(json.loads(data))


def main():
    data = parse_input('input/day12.txt')
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == "__main__":
    main()
