def read_input() -> list:
    particles = []
    lines = [line.strip() for line in open("input/day20.txt").readlines()]
    for line in lines:
        particle = []
        parts = line.split(", ")
        for part in parts:
            particle.append([int(num) for num in part[3:-1].split(",")])
        particles.append(particle)
    return particles


def update_particle(particle: list):
    for dim in range(len(particle[0])):
        particle[1][dim] += particle[2][dim]
        particle[0][dim] += particle[1][dim]


def puzzle1(particles: list):
    distances = []
    for _ in range(1000):
        distances = []
        for i, particle in enumerate(particles):
            update_particle(particle)
            distances.append(sum([abs(n) for n in particle[0]]))

    min_particle = distances.index(min(distances))
    print("best particle:", min_particle)


def puzzle2(particles: list):
    for _ in range(1000):
        particles_to_remove = []
        for i, particle in enumerate(particles):
            update_particle(particle)
        particle_positions = [particle[0] for particle in particles]
        for i in range(len(particle_positions)):
            if particle_positions.count(particle_positions[i]) > 1:
                particles_to_remove.append(i)
        particles_to_remove.reverse()
        for i in particles_to_remove:
            particles.pop(i)
    print("particles left", len(particles))


def puzzles():
    puzzle1(read_input())
    puzzle2(read_input())


if __name__ == "__main__":
    puzzles()
