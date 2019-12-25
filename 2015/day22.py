from copy import deepcopy
from sys import maxsize


# mana, damage, hp, armour, mana, turns, index
spells = [[53, 4, 0, 0, 0, 0, 0],
          [73, 2, 2, 0, 0, 0, 1],
          [113, 0, 0, 7, 0, 6, 2],
          [173, 3, 0, 0, 0, 6, 3],
          [229, 0, 0, 0, 101, 5, 4]]

least_mana_used = maxsize
part_two = False


def sim(boss_hp: int, my_hp: int, my_mana: int, active_spells: list, player_turn:bool, mana_used:int):
    global least_mana_used

    boss_damage = 9
    my_armor = 0

    if part_two and player_turn:
        my_hp -= 1
        if my_hp <= 0:
            return False

    new_active_spells = []
    for active_spell in active_spells:
        if active_spell[5] >= 0:
            boss_hp -= active_spell[1]
            my_hp += active_spell[2]
            my_armor += active_spell[3]
            my_mana += active_spell[4]

        new_active_spell = deepcopy(active_spell)
        new_active_spell[5] = new_active_spell[5] - 1
        if new_active_spell[5] > 0:
            new_active_spells.append(new_active_spell)

    if boss_hp <= 0:
        least_mana_used = min(least_mana_used, mana_used)
        return True

    if mana_used >= least_mana_used:
        return False

    if player_turn:
        for spell in spells:
            spell_already_active = False
            for new_active_spell in new_active_spells:
                if new_active_spell[6] == spell[6]:
                    spell_already_active = True
                    break

            spell_mana_cost = spell[0]
            if spell_mana_cost <= my_mana and not spell_already_active:
                a = deepcopy(new_active_spells)
                a.append(spell)
                sim(boss_hp, my_hp, my_mana - spell_mana_cost, a, False, mana_used + spell_mana_cost)
    else:
        my_hp += my_armor - boss_damage if my_armor - boss_damage < 0 else -1
        if my_hp > 0:
            sim(boss_hp, my_hp, my_mana, new_active_spells, True, mana_used)


def puzzles():
    global part_two
    global least_mana_used
    sim(58, 50, 500, [], True, 0)
    print("least mana:", least_mana_used)
    part_two = True
    least_mana_used = maxsize
    sim(58, 50, 500, [], True, 0)
    print("least mana:", least_mana_used)


if __name__ == "__main__":
    puzzles()
