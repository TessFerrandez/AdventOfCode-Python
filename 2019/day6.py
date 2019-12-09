"""
Universal Orbit Map
"""

orbits = dict()
cache = dict()


def parse_input():
    for line in open('input/day6.txt').readlines():
        orbit = line.strip().split(')')
        orbits[orbit[1]] = orbit[0]


def calculate_steps(planet):
    destination = orbits[planet]
    result = 0
    if destination not in orbits:
        result = 1
    elif destination in cache:
        result = 1 + cache[destination]
    else:
        result = 1 + calculate_steps(destination)
    cache[planet] = result
    return result


def calculate_orbits():
    return sum(calculate_steps(planet) for planet in orbits.keys())


def build_path(planet):
    if planet not in orbits:
        return [planet]
    return [planet] + build_path(orbits[planet])


def puzzle1and2():
    parse_input()
    print("number of orbits", calculate_orbits())

    cache.clear()
    path1 = build_path("YOU")
    path2 = build_path("SAN")
    unique_path1 = set(path1) - set(path2)
    unique_path2 = set(path2) - set(path1)
    print("orbital transfers: ", len(unique_path1) + len(unique_path2) - 2)


if __name__ == "__main__":
    puzzle1and2()
