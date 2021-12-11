# positions are represented as complex numbers
# x, y = x+yj
import numpy as np


octopuses = {x + y * 1j: int(energy)
             for x, line in enumerate(open('2021//input//day11.txt'))
             for y, energy in enumerate(line.strip())}


def print_board(octopuses):
    line = ""
    for octopus in octopuses:
        if octopus.imag == 0j:
            print(line)
            line = str(octopuses[octopus]) + " "
        else:
            line += str(octopuses[octopus]) + " "
    print(line)


def step(octopuses):
    # increase all the energies
    for octopus in octopuses:
        octopuses[octopus] += 1

    step_flashes = 0

    # keep flashing and increasing neighbors until no one is flashing anymore
    while(flashes := sum(flash(octopuses, octopus) for octopus, energy in octopuses.items() if energy > 9)):
        step_flashes += flashes

    return step_flashes


def flash(octopuses, octopus):
    # reset the current octopus
    octopuses[octopus] = 0

    # increase the energy of all the neighbors
    for neighbor in np.array([-1, 1, -1j, 1j, -1 - 1j, -1 + 1j, 1 + 1j, 1 - 1j]) + octopus:
        if neighbor in octopuses and octopuses[neighbor] > 0:
            octopuses[neighbor] += 1

    return 1


print("Part 1:", sum(step(octopuses) for _ in range(100)))

current_step = 100
while(step(octopuses)) != 100:
    current_step += 1

print("Part 2:", current_step + 1)
