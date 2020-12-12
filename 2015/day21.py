from typing import List, Tuple
from itertools import combinations


class Player:
    def __init__(self, armor: int, damage: int, hit_points: int, is_boss: bool):
        self.armor = armor
        self.damage = damage
        self.hit_points = hit_points
        self.is_boss = is_boss

    def is_alive(self):
        return self.hit_points > 0

    def take_punch(self, damage):
        self.hit_points -= max((damage - self.armor), 1)

    def __repr__(self):
        return f'armor: {self.armor}, damage: {self.damage}, hit points: {self.hit_points}, is_boss: {self.is_boss}'


def fight(player: Player, boss: Player) -> Player:
    current_attacker = player
    current_defender = boss

    while True:
        current_defender.take_punch(current_attacker.damage)
        if current_defender.is_alive():
            current_attacker, current_defender = current_defender, current_attacker
        else:
            break
    return current_attacker


def get_weapon_combos() -> List[Tuple[int, int, int]]:
    weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
    armors = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
    rings = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]

    # find ring combos
    ring_combos = [(0, 0, 0)]
    for ring in rings:
        ring_combos.append(ring)
    for ring_combo in list(combinations(rings, 2)):
        ring1, ring2 = ring_combo
        ring_combos.append((ring1[0] + ring2[0], ring1[1] + ring2[1], ring1[2] + ring2[2]))

    # calculate weapon, armor, ring combos
    weapon_combos = []
    for weapon in weapons:
        for armor in armors:
            for ring_combo in ring_combos:
                weapon_combos.append((weapon[0] + armor[0] + ring_combo[0], weapon[1] + armor[1] + ring_combo[1], weapon[2] + armor[2] + ring_combo[2]))

    return list(sorted(weapon_combos))


def part1(boss_stats: dict) -> int:
    for weapon_combo in get_weapon_combos():
        cost, damage, armor = weapon_combo
        player = Player(armor=armor, damage=damage, hit_points=100, is_boss=False)
        boss = Player(armor=boss_stats['armor'], damage=boss_stats['damage'], hit_points=boss_stats['hit_points'], is_boss=True)
        winner = fight(player, boss)
        if not winner.is_boss:
            return cost


def part2(boss_stats: dict) -> int:
    weapon_combos = list(reversed(get_weapon_combos()))
    for weapon_combo in weapon_combos:
        cost, damage, armor = weapon_combo
        player = Player(armor=armor, damage=damage, hit_points=100, is_boss=False)
        boss = Player(armor=boss_stats['armor'], damage=boss_stats['damage'], hit_points=boss_stats['hit_points'], is_boss=True)
        winner = fight(player, boss)
        if winner.is_boss:
            return cost


def main():
    boss_stats = {'armor': 2, 'damage': 9, 'hit_points': 103, 'is_boss': True}
    print(f'Part 1: {part1(boss_stats)}')
    print(f'Part 2: {part2(boss_stats)}')


if __name__ == "__main__":
    main()
