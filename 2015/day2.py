import re


def calculate_paper(sides):
    return 3 * sides[0] * sides[1] + \
           2 * sides[0] * sides[2] + \
           2 * sides[1] * sides[2]


def calculate_ribbon(sides):
    return 2 * sides[0] + \
           2 * sides[1] + \
           sides[0] * sides[1] * sides[2]


def puzzle():
    total_paper = 0
    total_ribbon = 0
    with open("input/day2.txt") as f:
        for gift in f:
            sides = [int(side) for side in re.split(r'x', gift)]
            sides.sort()
            total_paper += calculate_paper(sides)
            total_ribbon += calculate_ribbon(sides)

    print("Paper: ", total_paper)
    print("Ribbon: ", total_ribbon)


if __name__ == "__main__":
    puzzle()
