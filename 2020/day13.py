import pytest
import progressbar
import numpy as np
from typing import List, Tuple


@pytest.mark.parametrize('bus_info, earliest_departure, expected',
                         [
                             ('7,13,x,x,59,x,31,19', 939, 295),
                         ])
def test_part1(bus_info: str, earliest_departure: int, expected: int):
    buses = parse_buses(bus_info)
    assert part1(buses, earliest_departure) == expected


@pytest.mark.parametrize('bus_info, expected',
                         [
                             ('17,x,13,19', 3417),
                             ('67,7,59,61', 754018),
                             ('67,x,7,59,61', 779210),
                             ('67,7,x,59,61', 1261476),
                             ('7,13,x,x,59,x,31,19', 1068781),
                             # ('1789,37,47,1889', 1202161486),
                         ])
def test_part2(bus_info: str, expected: int):
    buses = parse_buses(bus_info)
    assert part2(buses) == expected


def parse_buses(bus_str: str) -> List[Tuple[int, int]]:
    buses = [(-delay, int(bus)) for delay, bus in enumerate(bus_str.split(',')) if bus != 'x']
    return buses


def parse_input(filename: str) -> (int, List[Tuple[int, int]]):
    lines = [line.strip() for line in open(filename).readlines()]
    earliest_departure = int(lines[0])
    return earliest_departure, parse_buses(lines[1])


def part1(buses: List[Tuple[int, int]], earliest_departure: int) -> int:
    timestamp = earliest_departure
    while True:
        for _, bus in buses:
            if timestamp % bus == 0:
                return (timestamp - earliest_departure) * bus
        timestamp += 1


def extended_gcd(a: int, b: int) -> (int, int, int):
    """
    # extended GCD for finding modular inverse
    # https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
    """
    if a == 0:
        return b, 0, 1
    else:
        b_div_a, b_mod_a = divmod(b, a)
        g, x, y = extended_gcd(b_mod_a, a)
        return g, y - b_div_a * x, x


def mod_inverse(a: int, b: int) -> int:
    """
    return x such that (x * a) % b == 1
    """
    g, x, _ = extended_gcd(a, b)
    if g != 1:
        print(f'gcd(a, b) = {g} för ({a}, {b}) != 1')
        raise Exception('gcd(a, b) != 1')
    return x % b


def chinese_remainder(pairs: List[Tuple[int, int]]) -> int:
    """
    chinese remainder - to solve equations like
    x ≡ 3 (mod 5)
    x ≡ 1 (mod 7)
    x ≡ 6 (mod 8)
    ----------------
    so we can solve timestamp ≡ 0 (mod 17) ≡ 13-2 (mod 13) ≡ 19-3 (mod 19)
    for 17,x,13,19
    """
    rems, ns = zip(*pairs)
    total = 0

    N = 1
    for n in ns:
        N *= n

    for pair in pairs:
        bi, ni = pair
        Ni = N // ni
        xi = mod_inverse(Ni % ni, ni)
        total += bi * Ni * xi

    return total % N


def part2(buses: List[Tuple[int, int]]) -> int:
    return chinese_remainder(buses)


def main():
    earliest_departure, buses = parse_input('input/day13.txt')
    print(f'Part 1: {part1(buses, earliest_departure)}')
    print(f'Part 2: {part2(buses)}')


if __name__ == "__main__":
    main()
