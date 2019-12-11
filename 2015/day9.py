import re
from itertools import permutations


travel_routes = dict()
cities = []


def parse_input(lines):
    global travel_routes
    global cities

    routes = [re.split(' to | = ', line.strip()) for line in lines]
    for route in routes:
        city_from, city_to, distance = route
        cities.append(city_from)
        cities.append(city_to)
        travel_routes[(city_from, city_to)] = int(distance)
        travel_routes[(city_to, city_from)] = int(distance)
    cities = list(set(cities))


def get_distance(travel_route):
    num_locations = len(travel_route)
    distance = 0
    for i in range(num_locations - 1):
        distance += travel_routes[(travel_route[i], travel_route[i + 1])]
    return distance


def puzzles():
    parse_input(open('input/day9.txt').readlines())
    distances = [get_distance(permutation)
                 for permutation in permutations(cities)]

    print("min distance", min(distances))
    print("max distance", max(distances))


if __name__ == "__main__":
    puzzles()
