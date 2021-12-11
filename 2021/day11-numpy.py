from typing import List, Tuple
import numpy as np


MAX = 10


def get_flashing(octopuses, prev_flashing: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Get the new flashing positions
    """
    new_flashing = np.where(octopuses >= 10)
    return [(x, y) for x, y in zip(new_flashing[0], new_flashing[1]) if (x, y) not in prev_flashing]


def increase_neighbors(octopuses, flashing: List[Tuple[int, int]]) -> None:
    """
    Increase the neighbors of the flashing octopuses
    """
    for y, x in flashing:
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                ny = y + dy
                nx = x + dx
                if 0 <= nx < MAX and 0 <= ny < MAX and (dx, dy) != (0, 0):
                    octopuses[ny, nx] += 1


def reset_energy(octopuses) -> int:
    """
    Reset the energy of the flashing octopuses
    """
    num_flashing = np.count_nonzero(octopuses >= 10)
    octopuses[octopuses >= 10] = 0
    return num_flashing


def get_octopuses() -> np.ndarray:
    """
    Get the octopuses
    """
    return np.array([[int(energy) for energy in line.strip()] for line in open('2021//input//day11.txt')])


def simulate_octopuses(max_steps: int) -> Tuple[int, int]:
    simultaneous_flashing = False
    step = 0
    octopuses = get_octopuses()
    total_flashing = 0

    while step < max_steps and not simultaneous_flashing:
        step += 1
        flashing = []

        # increase all energies by 1
        octopuses += 1

        # get the new flashing octopuses
        new_flashing = get_flashing(octopuses, [])
        flashing += new_flashing

        while new_flashing:
            # increase all neighbors of the new flashing octopuses
            increase_neighbors(octopuses, new_flashing)

            # get the new flashing octopuses
            new_flashing = get_flashing(octopuses, flashing)
            flashing += new_flashing

        # reset the energy of the flashing octopuses
        num_flashing = reset_energy(octopuses)

        if num_flashing == 100:
            simultaneous_flashing = True
            break
        total_flashing += num_flashing

    return total_flashing, step


flashing, step = simulate_octopuses(100)
print(f'Part 1: {flashing}')
flashing, step = simulate_octopuses(1000)
print(f'Part 2: {step}')
