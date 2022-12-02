from copy import deepcopy
from math import lcm


original_moons = [[7, 10, 17], [-2, 7, 0], [12, 5, 12], [5, -8, 6]]
original_velocities = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
# original_moons = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
# original_velocities = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]


def update_velocities(moons, velocities):
    for m in range(len(moons)):
        for i in range(3):
            velocities[m][i] += sum(1 if moons[m][i] < moon[i] else -1 if moons[m][i] > moon[i] else 0 for moon in moons)


def update_positions(moons, velocities):
    for m in range(len(moons)):
        for i in range(3):
            moons[m][i] += velocities[m][i]


def calculate_energy(moons, velocities):
    potential = [sum(abs(i) for i in moon) for moon in moons]
    kinetic = [sum(abs(i) for i in moon) for moon in velocities]
    total = sum(potential[i] * kinetic[i] for i in range(len(moons)))
    return total


def get_cadence(axis, moons, velocities):
    state = tuple(moon[axis] for moon in moons)
    step = 1

    while True:
        # update velocity
        for m in range(len(moons)):
            velocities[m][axis] += sum(1 if moons[m][axis] < moon[axis] else -1 if moons[m][axis] > moon[axis] else 0 for moon in moons)

        # update positions
        for m in range(len(moons)):
            moons[m][axis] += velocities[m][axis]

        step += 1
        new_state = tuple(m[axis] for m in moons)
        if state == new_state:
            return step


moons = deepcopy(original_moons)
velocities = deepcopy(original_velocities)

for step in range(1000):
    update_velocities(moons, velocities)
    update_positions(moons, velocities)

print("Part 1:", calculate_energy(moons, velocities))


moons = deepcopy(original_moons)
velocities = deepcopy(original_velocities)

x_cadence = get_cadence(0, moons, velocities)
y_cadence = get_cadence(1, moons, velocities)
z_cadence = get_cadence(2, moons, velocities)

least_common_multiple = lcm(lcm(x_cadence, y_cadence), z_cadence)
print("Part 2:", least_common_multiple)
