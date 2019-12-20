import itertools


def find_combos(containers: list, target: int) -> list:
    return [seq for i in range(len(containers), 0, -1)
            for seq in itertools.combinations(containers, i)
            if sum(seq) == target]


def find_lowest_number_of_containers(combos) -> (int, int):
    combo_count = dict()
    for combo in combos:
        combo_len = len(combo)
        if combo_len in combo_count:
            combo_count[combo_len] += 1
        else:
            combo_count[combo_len] = 1

    n_lowest_cont = sorted(combo_count)[0]
    n_combos = combo_count[n_lowest_cont]
    return n_lowest_cont, n_combos


def puzzles():
    containers = [int(num) for num in open("input/day17.txt").readlines()]
    combos = find_combos(containers, 150)
    print("number of combos", len(combos))
    n_containers, n_combos = find_lowest_number_of_containers(combos)
    print(n_combos, "combos with", n_containers, "containers")


if __name__ == "__main__":
    puzzles()
