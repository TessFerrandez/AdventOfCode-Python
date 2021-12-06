from collections import defaultdict


fish = [3, 4, 3, 1, 2]
fish = [int(f) for f in open('2021//input//day6.txt').readline().split(',')]


def simulate_fish_population(fish, days):
    """
    Simulate the fish population for a given number of days.
    """
    for _ in range(days):
        new_fish = []
        for fish in fish:
            if fish == 0:
                new_fish.append(6)
                new_fish.append(8)
            else:
                new_fish.append(fish - 1)
        fish = new_fish
    return fish


def calculate_fish_population(fish, days):
    """
    Calculate the fish population after a given number of days.
    Each day, the fish born are parented by some old fish that also gave birth 7 days ago, or some new fish that were born 9 days ago.

    We can use dynamic programming to build a table - so the new fish a given day are born[day - 7] + born[day - 9].
    Since we initiate the fish population (based on the input) we also have to add any initial fish (born[day]).
    This is way way faster than simulating, simulating takes forever for 256 days.

    The total fish population is the sum of all the fish born + all the initial fish
    """
    born_at = defaultdict(lambda: 0)

    for fish_individual in fish:
        born_at[fish_individual] += 1
    for day in range(days):
        born_at[day] = born_at[day] + born_at[day - 7] + born_at[day - 9]
    return sum(born_at.values()) + len(fish)


print("Part 1:", len(simulate_fish_population(fish, 80)))
print("Part 2:", calculate_fish_population(fish, 256))
