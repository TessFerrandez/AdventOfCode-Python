### THIS IS INCORRECT

from typing import List, Dict, Tuple


def parse_group(line: str, type: str) -> Dict:
    parts = line.split(" ")
    group = {
        "units": int(parts[0]),
        "hp": int(parts[4]),
        "attack": int(parts[-6]),
        "attack_type": parts[-5],
        "initiative": int(parts[-1]),
        "weaknesses": [],
        "immunities": [],
        "type": type
    }
    group["effective_power"] = group["units"] * group["attack"]
    if "(" in line:
        _, p2 = line.split("(")
        weak_info, _ = p2.split(")")
        weak_infos = weak_info.split("; ")
        for info in weak_infos:
            if info.startswith("weak to"):
                group["weaknesses"] = info[8:].split(", ")
            elif info.startswith("immune to"):
                group["immunities"] = info[10:].split(", ")

    return group


def get_input() -> Tuple[List[Dict], List[Dict]]:
    lines = [line.strip() for line in open('2018//input//day24.txt').readlines()]
    immune_system, infection = [], []
    immune = True

    for line in lines:
        if line == "Immune System:":
            immune = True
        elif line == "Infection:":
            immune = False
        elif line == "":
            continue
        else:
            group = parse_group(line, "immune" if immune else "infection")
            if immune:
                immune_system.append(group)
            else:
                infection.append(group)

    return immune_system, infection


def calculate_damage(attacker: Dict, defender: Dict) -> int:
    damage = 0
    if attacker["attack_type"] in defender["immunities"]:
        damage = 0
    elif attacker["attack_type"] in defender["weaknesses"]:
        damage = attacker["units"] * attacker["attack"] * 2
    else:
        damage = attacker["units"] * attacker["attack"]

    return damage


def print_status(immune_system, infection):
    print("Immune System:")
    for i, group in enumerate(immune_system):
        print(f"Group {i} contains {group['units']} units")

    print("Infection:")
    for i, group in enumerate(infection):
        print(f"Group {i} contains {group['units']} units")


def select_target(attacker: Dict, targets: List[Dict]) -> Dict:
    targets.sort(key=lambda group: (calculate_damage(attacker, group), group["effective_power"], group["initiative"]), reverse=True)
    for target in targets:
        if calculate_damage(attacker, target) > 0:
            return target
    return None


def select_order(immune_system: List[Dict], infection: List[Dict]):
    order = []
    immune_system.sort(key=lambda group: (group["effective_power"], group["initiative"]), reverse=True)
    infection.sort(key=lambda group: (group["effective_power"], group["initiative"]), reverse=True)

    available_immune_system = [group for group in immune_system]
    available_infection = [group for group in infection]

    for attacker in immune_system:
        target = select_target(attacker, available_infection)
        if target is None:
            continue
        order.append((attacker, target))
        available_infection.remove(target)

    for attacker in infection:
        target = select_target(attacker, available_immune_system)
        if target is None:
            continue
        order.append((attacker, target))
        available_immune_system.remove(target)

    order.sort(key=lambda pair: pair[0]["initiative"], reverse=True)
    return order


def remove_dead_units(immune_system: List[Dict], infection: List[Dict]):
    immune_system = [group for group in immune_system if group["units"] > 0]
    infection = [group for group in infection if group["units"] > 0]


def part1() -> int:
    immune_system, infection = get_input()

    while immune_system and infection:
        # print status
        # print_status(immune_system, infection)

        # select targets
        order = select_order(immune_system, infection)

        # attack
        for attacker, target in order:
            if attacker["units"] <= 0:
                continue
            damage = calculate_damage(attacker, target)
            target["units"] -= damage // target["hp"]

        # remove dead units
        immune_system = [group for group in immune_system if group["units"] > 0]
        infection = [group for group in infection if group["units"] > 0]

    if infection:
        print("Infection won")
        return sum([group["units"] for group in infection])
    else:
        print("Immune System won")
        return sum([group["units"] for group in immune_system])


print("Part 1:", part1())
