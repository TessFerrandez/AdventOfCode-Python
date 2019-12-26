def parse_input() -> dict:
    lines = [
        line.strip().replace(":", "").replace(",", "")
        for line in open("input/day16.txt").readlines()
    ]
    sues = dict()
    for line in lines:
        parts = line.split()
        sues[parts[1]] = {
            parts[2]: int(parts[3]),
            parts[4]: int(parts[5]),
            parts[6]: int(parts[7]),
        }
    return sues


def compare_sue_to_evidence(properties: dict) -> bool:
    evidence = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    for ev in evidence:
        if ev in properties and evidence[ev] != properties[ev]:
            return False
    return True


def compare_sue_to_new_evidence(properties: dict) -> bool:
    base_evidence = {
        "children": 3,
        "samoyeds": 2,
        "akitas": 0,
        "vizslas": 0,
        "cars": 2,
        "perfumes": 1,
    }
    greater_evidence = {"cats": 7, "trees": 3}
    lower_evidence = {"pomeranians": 3, "goldfish": 5}

    for ev in base_evidence:
        if ev in properties and base_evidence[ev] != properties[ev]:
            return False
    for ev in greater_evidence:
        if ev in properties and properties[ev] <= greater_evidence[ev]:
            return False
    for ev in lower_evidence:
        if ev in properties and properties[ev] >= lower_evidence[ev]:
            return False
    return True


def puzzles():
    sues = parse_input()
    for sue in sues:
        if compare_sue_to_evidence(sues[sue]):
            print("this is the aunt:", sue)
            break
    for sue in sues:
        if compare_sue_to_new_evidence(sues[sue]):
            print("this is the aunt:", sue)
            break


if __name__ == "__main__":
    puzzles()
