from itertools import accumulate, cycle


def get_changes():
    return [int(change) for change in open("input/day1.txt").readlines()]


def puzzle1():
    changes = get_changes()
    print("sum of changes", sum(changes))


def puzzle2():
    changes = get_changes()
    seen = set()
    print(
        "first frequency reached twice:",
        next(f for f in accumulate(cycle(changes)) if f in seen or seen.add(f)),
    )


if __name__ == "__main__":
    puzzle1()
    puzzle2()
