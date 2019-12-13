import re


def get_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def calculate_lcm(steps):
    primes_per_dimension = [get_prime_factors(step) for step in steps]
    all_primes = set([prime for primes in primes_per_dimension for prime in primes])

    lcm = 1
    for prime in all_primes:
        amount = max(primes_per_dimension[dim].count(prime) for dim in range(3))
        lcm *= prime ** amount
    return lcm


def calc_abs_sum(numbers):
    return sum(abs(number) for number in numbers)


def apply_gravity(planets, velocities):
    for p1 in range(3):
        for p2 in range(p1 + 1, 4):
            for axis in range(3):
                if planets[p1][axis] > planets[p2][axis]:
                    velocities[p1][axis] -= 1
                    velocities[p2][axis] += 1
                elif planets[p1][axis] < planets[p2][axis]:
                    velocities[p1][axis] += 1
                    velocities[p2][axis] -= 1


def apply_gravity_per_dim(planets, velocities):
    for p1 in range(3):
        for p2 in range(p1 + 1, 4):
            if planets[p1] > planets[p2]:
                velocities[p1] -= 1
                velocities[p2] += 1
            elif planets[p1] < planets[p2]:
                velocities[p1] += 1
                velocities[p2] -= 1


def apply_velocity(planets, velocities):
    for p in range(4):
        for axis in range(3):
            planets[p][axis] += velocities[p][axis]


def apply_velocity_per_dim(planets, velocities):
    for p in range(4):
        planets[p] += velocities[p]


def matches_start_state(planets, velocities, p_dim, v_dim, dim):
    for i in range(4):
        if planets[i][dim] != p_dim[i] or \
           velocities[i][dim] != v_dim[i]:
            return False
    return True


def calculate_energy(planets, velocities):
    pot = [calc_abs_sum(planet) for planet in planets]
    kin = [calc_abs_sum(velocity) for velocity in velocities]
    return sum([p * k for p, k in list(zip(pot, kin))])


def puzzle1():
    planets = [[int(digit) for digit in re.findall(r'[-\d]+', line)]
               for line in open("input/day12.txt").readlines()]
    velocities = [[0, 0, 0] for i in range(4)]

    for _ in range(1000):
        apply_gravity(planets, velocities)
        apply_velocity(planets, velocities)

    print("total energy:", calculate_energy(planets, velocities))


def puzzle2():
    planets = [[int(digit) for digit in re.findall(r'[-\d]+', line)]
               for line in open("input/day12.txt").readlines()]
    velocities = [[0, 0, 0] for i in range(4)]
    steps = [0, 0, 0]

    for dim in range(3):
        planet_dims = [planet[dim] for planet in planets]
        velocities_dims = [velocity[dim] for velocity in velocities]

        while True:
            apply_gravity_per_dim(planet_dims, velocities_dims)
            apply_velocity_per_dim(planet_dims, velocities_dims)

            steps[dim] += 1

            if matches_start_state(planets, velocities, planet_dims, velocities_dims, dim):
                break

    print("steps:", calculate_lcm(steps))


if __name__ == "__main__":
    puzzle1()
    puzzle2()
