from typing import List
from copy import deepcopy


SPELLS = [
    {'index': 0, 'cost': 53, 'damage': 4, 'hp': 0, 'armor': 0, 'mana': 0, 'turns': 0},
    {'index': 1, 'cost': 73, 'damage': 2, 'hp': 2, 'armor': 0, 'mana': 0, 'turns': 0},
    {'index': 2, 'cost': 113, 'damage': 0, 'hp': 0, 'armor': 7, 'mana': 0, 'turns': 6},
    {'index': 3, 'cost': 173, 'damage': 3, 'hp': 0, 'armor': 0, 'mana': 0, 'turns': 6},
    {'index': 4, 'cost': 229, 'damage': 0, 'hp': 0, 'armor': 0, 'mana': 101, 'turns': 5},
]
LEAST_MANA_USED = float('inf')
BOSS_DAMAGE = 9
PART2 = False


def simulate(boss_hp: int, player_hp: int, player_mana: int, active_spells: List = [], player_turn: bool = True, mana_used: int = 0):
    global LEAST_MANA_USED

    my_armor = 0

    if PART2 and player_turn:
        player_hp -= 1
        if player_hp <= 0:
            return False

    new_active_spells = []
    for active_spell in active_spells:
        if active_spell['turns'] >= 0:
            boss_hp -= active_spell['damage']
            player_hp += active_spell['hp']
            my_armor += active_spell['armor']
            player_mana += active_spell['mana']

        new_active_spell = deepcopy(active_spell)
        new_active_spell['turns'] = new_active_spell['turns'] - 1
        if new_active_spell['turns'] > 0:
            new_active_spells.append(new_active_spell)

    if boss_hp <= 0:
        LEAST_MANA_USED = min(LEAST_MANA_USED, mana_used)
        return True

    if mana_used >= LEAST_MANA_USED:
        return False

    if player_turn:
        for spell in SPELLS:
            spell_already_active = False
            for new_active_spell in new_active_spells:
                if new_active_spell['index'] == spell['index']:
                    spell_already_active = True
                    break

            spell_mana_cost = spell['cost']
            if spell_mana_cost <= player_mana and not spell_already_active:
                a = deepcopy(new_active_spells)
                a.append(spell)
                simulate(boss_hp, player_hp, player_mana - spell_mana_cost, a, False, mana_used + spell_mana_cost)
    else:
        player_hp += my_armor - BOSS_DAMAGE if my_armor - BOSS_DAMAGE < 0 else -1
        if player_hp > 0:
            simulate(boss_hp, player_hp, player_mana, new_active_spells, True, mana_used)


def part1(boss_hp: int, player_hp: int, player_mana: int) -> int:
    global LEAST_MANA_USED, PART2
    LEAST_MANA_USED = float('inf')
    PART2 = False
    simulate(boss_hp, player_hp, player_mana)
    return int(LEAST_MANA_USED)


def part2(boss_hp: int, player_hp: int, player_mana: int) -> int:
    global LEAST_MANA_USED, PART2
    LEAST_MANA_USED = float('inf')
    PART2 = True
    simulate(boss_hp, player_hp, player_mana)
    return int(LEAST_MANA_USED)


def main():
    print(f'Part 1: {part1(58, 50, 500)}')
    print(f'Part 2: {part2(58, 50, 500)}')


if __name__ == "__main__":
    main()
