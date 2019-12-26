def puzzle1():
    num_possible = 0
    with open("input/day3.txt") as f:
        for line in f:
            sides = [int(line[0:5]), int(line[5:10]), int(line[10:15])]
            sides.sort()
            if int(sides[0]) + int(sides[1]) > int(sides[2]):
                num_possible += 1
    print("possible triangles:", num_possible)


def puzzle2():
    all_sides = [
        [int(line[0:5]), int(line[5:10]), int(line[10:15])]
        for line in open("input/day3.txt").readlines()
    ]
    num_rows = len(all_sides)
    possible = 0
    for x in range(3):
        y = 0
        while y < num_rows:
            sides = [all_sides[y][x], all_sides[y + 1][x], all_sides[y + 2][x]]
            sides.sort()
            if sides[0] + sides[1] > sides[2]:
                possible += 1
            y += 3

    print("possible triangles:", possible)


if __name__ == "__main__":
    puzzle1()
    puzzle2()
