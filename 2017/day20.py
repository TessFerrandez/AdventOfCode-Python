from typing import List
from operator import add


def parse_input(filename: str) -> List[List[List[int]]]:
    lines = [line.strip() for line in open(filename).readlines()]
    particles = []
    for line in lines:
        p, v, a = line.split(', ')
        p = [int(d) for d in p[3:-1].split(',')]
        v = [int(d) for d in v[3:-1].split(',')]
        a = [int(d) for d in a[3:-1].split(',')]
        particles.append([p, v, a])
    return particles


def part1(particles: List[List[List[int]]]) -> int:
    for j in range(1000):
        for i in range(len(particles)):
            particles[i][1] = list(map(add, particles[i][1], particles[i][2]))
            particles[i][0] = list(map(add, particles[i][0], particles[i][1]))

    min_distance, closest_particle = float('inf'), -1
    for i in range(len(particles)):
        distance = sum(abs(d) for d in particles[i][0])
        if distance < min_distance:
            min_distance = distance
            closest_particle = i
    return closest_particle


def part2(particles: List[List[List[int]]]) -> int:
    for j in range(1000):
        seen = set()
        to_remove = set()
        for i in range(len(particles)):
            particles[i][1] = list(map(add, particles[i][1], particles[i][2]))
            particles[i][0] = list(map(add, particles[i][0], particles[i][1]))
            if tuple(particles[i][0]) in seen:
                to_remove.add(tuple(particles[i][0]))
            else:
                seen.add(tuple(particles[i][0]))

        particles_to_remove = []
        for p in to_remove:
            for particle in particles:
                if particle[0] == list(p):
                    particles_to_remove.append(particle)

        for particle in particles_to_remove:
            particles.remove(particle)

    return len(particles)


def main():
    particles = parse_input('input/day20.txt')
    print(f'Part 1: {part1(particles)}')
    particles = parse_input('input/day20.txt')
    print(f'Part 2: {part2(particles)}')


if __name__ == "__main__":
    main()
