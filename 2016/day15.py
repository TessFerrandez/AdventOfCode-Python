def disc_in_position(disc: int, positions: int, position: int, time: int) -> bool:
    if (disc + position + time) % positions == 0:
        return True
    return False


def read_input() -> list:
    discs = []
    lines = [line.strip().split() for line in open("input/day15.txt").readlines()]
    for line in lines:
        disc = [int(line[1][1:]), int(line[3]), int(line[11][:-1])]
        discs.append(disc)
    return discs


def puzzle1(discs: list) -> int:
    i = 0
    while True:
        i += 1
        ok = True
        for disc in discs:
            if not disc_in_position(disc[0], disc[1], disc[2], i):
                ok = False
                break
        if ok:
            return i


def puzzles():
    discs = read_input()
    first = puzzle1(discs)
    print("first button press:", first)
    new_disc = [7, 11, 0]
    discs.append(new_disc)
    first = puzzle1(discs)
    print("first button press:", first)


if __name__ == "__main__":
    puzzles()
