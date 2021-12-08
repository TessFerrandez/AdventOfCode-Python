entries = [[[pattern for pattern in part.split(' ')] for part in line.strip().split(' | ')] for line in open('2021//input//day8.txt').readlines()]


def part1():
    return sum(sum(1 for pattern in entry[1] if len(pattern) <= 4 or len(pattern) == 7) for entry in entries)


print("part 1:", part1())
