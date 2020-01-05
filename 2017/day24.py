def read_input() -> list:
    return [
        [int(num) for num in line.strip().split("/")]
        for line in open("input/day24.txt").readlines()
    ]


def find_chains(dominoes: list, last_num: int) -> list:
    chains = []
    possible = [domino for domino in dominoes if last_num in domino]
    for domino in possible:
        dominoes_left = [d for d in dominoes if d != domino]
        if domino[0] == last_num:
            chains.append([domino])
            for chain in find_chains(dominoes_left, domino[1]):
                chains.append([domino] + chain)
        else:
            chains.append([[domino[1], domino[0]]])
            for chain in find_chains(dominoes_left, domino[0]):
                chains.append([[domino[1], domino[0]]] + chain)
    return chains


def find_totals(dominoes: list, last_num: int) -> list:
    totals = []
    possible = [domino for domino in dominoes if last_num in domino]
    for domino in possible:
        dominoes_left = [d for d in dominoes if d != domino]
        if domino[0] == last_num:
            totals.append(sum(domino))
            for total in find_totals(dominoes_left, domino[1]):
                totals.append(sum(domino) + total)
        else:
            totals.append(sum(domino))
            for total in find_totals(dominoes_left, domino[0]):
                totals.append(sum(domino) + total)
    return totals


def puzzle1(dominoes: list):
    totals = find_totals(dominoes, 0)
    print("max sum:", max(totals))


def puzzle2(dominoes: list):
    chains = find_chains(dominoes, 0)
    max_len = 0
    max_chains = []
    for chain in chains:
        if len(chain) > max_len:
            max_chains = [chain]
            max_len = len(chain)
        if len(chain) == max_len:
            max_chains.append(chain)

    max_strength = 0
    for chain in max_chains:
        chain_strength = 0
        for domino in chain:
            chain_strength += sum(domino)
        max_strength = max(max_strength, chain_strength)
    print("max strength:", max_strength)


def puzzles():
    dominoes = read_input()
    puzzle1(dominoes)
    puzzle2(dominoes)


if __name__ == "__main__":
    puzzles()
