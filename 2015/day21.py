import itertools
import math


def generate_combos() -> list:
    weapons = [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]
    armor = [[0, 0, 0], [13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5]]
    rings = [
        [0, 0, 0],
        [0, 0, 0],
        [20, 0, 1],
        [25, 1, 0],
        [40, 0, 2],
        [50, 2, 0],
        [80, 0, 3],
        [100, 3, 0],
    ]
    ring_combos = list(itertools.combinations(rings, 2))

    combos = []

    for weapon in weapons:
        for armor_item in armor:
            for ring_combo in ring_combos:
                price = weapon[0] + armor_item[0] + ring_combo[0][0] + ring_combo[1][0]
                arm = weapon[1] + armor_item[1] + ring_combo[0][1] + ring_combo[1][1]
                dmg = weapon[2] + armor_item[2] + ring_combo[0][2] + ring_combo[1][2]
                combos.append([price, arm, dmg])
    return sorted(combos)


def fight(combo: list) -> bool:
    you_hp = 100
    boss_hp = 103
    boss_dmg = 9
    boss_arm = 2

    you_dmg_per_hit = max(combo[1] - boss_arm, 1)
    boss_dmg_per_hit = max(boss_dmg - combo[2], 1)

    you_num_hits = math.ceil(boss_hp / you_dmg_per_hit)
    boss_num_hits = math.ceil(you_hp / boss_dmg_per_hit)

    if boss_num_hits >= you_num_hits:
        return True
    return False


def puzzles():
    combos = generate_combos()
    for combo in combos:
        if fight(combo):
            print(combo)
            print("money spent:", combo[0])
            break
    combos.reverse()
    for combo in combos:
        if not fight(combo):
            print(combo)
            print("money spent:", combo[0])
            break


if __name__ == "__main__":
    puzzles()
