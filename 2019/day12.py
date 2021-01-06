from common.helpers import extract_numbers
from typing import List

NUM_MOONS = 4
NUM_DIMS = 3


def parse_input(filename: str) -> List[List[int]]:
    return [extract_numbers(line.strip()) for line in open(filename).readlines()]


def apply_gravity(moons: List[List[int]], velocities: List[List[int]]):
    for m1 in range(NUM_MOONS):
        for m2 in range(m1 + 1, NUM_MOONS):
            for dim in range(NUM_DIMS):
                if moons[m1][dim] > moons[m2][dim]:
                    velocities[m1][dim] -= 1
                    velocities[m2][dim] += 1
                if moons[m1][dim] < moons[m2][dim]:
                    velocities[m1][dim] += 1
                    velocities[m2][dim] -= 1


def apply_velocity(moons: List[List[int]], velocities: List[List[int]]):
    for m in range(NUM_MOONS):
        for dim in range(NUM_DIMS):
            moons[m][dim] += velocities[m][dim]


def calculate_energy(moons: List[List[int]], velocities: List[List[int]]) -> int:
    energy = 0
    for i in range(NUM_MOONS):
        pot = sum(abs(d) for d in moons[i])
        kin = sum(abs(d) for d in velocities[i])
        total = pot * kin
        energy += total
    return energy


def part1(moons: List[List[int]]) -> int:
    velocities = [[0, 0, 0] for _ in range(NUM_MOONS)]

    for k in range(1000):
        apply_gravity(moons, velocities)
        apply_velocity(moons, velocities)

    return calculate_energy(moons, velocities)


def apply_gravity_by_dim(moons: List[int], velocities: List[int]):
    for m1 in range(NUM_MOONS):
        for m2 in range(m1 + 1, NUM_MOONS):
            if moons[m1] > moons[m2]:
                velocities[m1] -= 1
                velocities[m2] += 1
            elif moons[m1] < moons[m2]:
                velocities[m1] += 1
                velocities[m2] -= 1


def apply_velocity_by_dim(moons: List[int], velocities: List[int]):
    for moon in range(NUM_MOONS):
        moons[moon] += velocities[moon]


def matches_start_state(moons: List[List[int]], velocities: List[List[int]], moon_dims: List[int], velocities_dims: List[int], dim: int) -> bool:
    for m in range(NUM_MOONS):
        if moons[m][dim] != moon_dims[m] or velocities[m][dim] != velocities_dims[m]:
            return False
    return True


def get_prime_factors(step: int) -> List[int]:
    i = 2
    factors = []
    while i * i <= step:
        if step % i:
            i += 1
        else:
            step //= i
            factors.append(i)
    if step > 1:
        factors.append(step)
    return factors


def calculate_lcm(steps: List[int]) -> int:
    primes_per_dim = [get_prime_factors(step) for step in steps]
    all_primes = set([prime for primes in primes_per_dim for prime in primes])

    lcm = 1
    for prime in all_primes:
        amount = max(primes_per_dim[dim].count(prime) for dim in range(NUM_DIMS))
        lcm *= prime ** amount
    return lcm


def part2(moons: List[List[int]]) -> int:
    velocities = [[0, 0, 0] for _ in range(NUM_MOONS)]
    steps = [0, 0, 0]

    for dim in range(3):
        moon_dims = [moon[dim] for moon in moons]
        velocities_dims = [velocity[dim] for velocity in velocities]

        while True:
            apply_gravity_by_dim(moon_dims, velocities_dims)
            apply_velocity_by_dim(moon_dims, velocities_dims)

            steps[dim] += 1

            if matches_start_state(moons, velocities, moon_dims, velocities_dims, dim):
                break

    return calculate_lcm(steps)


def main():
    moons = parse_input('input/day12.txt')
    print(f'Part 1: {part1(moons)}')
    moons = parse_input('input/day12.txt')
    print(f'Part 2: {part2(moons)}')


if __name__ == "__main__":
    main()
