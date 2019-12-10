import numpy as np


asteroids = []


def find_asteroids():
    lines = open('input/day10.txt').readlines()
    row = 0
    for line in lines:
        col = 0
        for char in line:
            if char == "#":
                asteroids.append((col, row))
            col += 1
        row += 1


def angle_between(u, v):
    dot = u[0] * v[0] + u[1] * v[1]
    det = u[0] * v[1] - u[1] * v[0]
    angle = np.arctan2(det, dot)
    return angle


def get_direction_and_distance(asteroid_from, asteroid_to):
    north = (0, 1)
    vector_to_asteroid = (asteroid_to[0] - asteroid_from[0], asteroid_to[1] - asteroid_from[1])

    distance = abs(vector_to_asteroid[0]) + abs(vector_to_asteroid[1])

    direction = np.degrees(angle_between(north, vector_to_asteroid))
    direction = direction - 180.0
    if direction < 0:
        direction += 360.0

    return direction, distance


def find_best_asteroid():
    max_asteroids_seen = 0
    best_asteroid = (0, 0)

    for asteroid_source in asteroids:
        directions = dict()
        for asteroid_target in asteroids:
            if asteroid_source == asteroid_target:
                continue
            direction, distance = get_direction_and_distance(asteroid_source, asteroid_target)
            if direction not in directions.keys():
                directions[direction] = True

        asteroids_seen = len(directions)
        if asteroids_seen > max_asteroids_seen:
            max_asteroids_seen = asteroids_seen
            best_asteroid = asteroid_source

    return best_asteroid, max_asteroids_seen


def get_sorted_directions(asteroid_source):
    directions = dict()
    for asteroid in asteroids:
        if asteroid == asteroid_source:
            continue
        angle, distance = get_direction_and_distance(asteroid_source, asteroid)
        if angle in directions:
            directions[angle].append((distance, asteroid))
        else:
            directions[angle] = [(distance, asteroid)]

    directions = [[k, v] for k, v in directions.items()]
    for direction in directions:
        direction[1].sort()
    directions.sort()
    return directions


def nth_vaporized(asteroid_source, nth=200):
    directions = get_sorted_directions(asteroid_source)

    n = 0
    vapor_index = 0
    vaporized = 0, (0, 0)
    while vapor_index < nth and len(directions) > 0:
        vapor_index += 1
        index = n % len(directions)
        direction = directions[index]
        targeted_asteroids = direction[1]
        vaporized = targeted_asteroids.pop(0)
        if len(targeted_asteroids) == 0:
            directions.remove(direction)
        else:
            n += 1

    return vaporized[1]


def puzzles():
    find_asteroids()
    asteroid, number_seen = find_best_asteroid()
    print("best asteroid is", asteroid, "where you can see", number_seen)
    asteroid = nth_vaporized(asteroid, 200)
    print("200th vaporized:", asteroid[0] * 100 + asteroid[1])


if __name__ == "__main__":
    puzzles()
