import collections


def puzzle1():
    cols = [[], [], [], [], [], [], [], []]
    with open("input/day6.txt") as f:
        for line in f:
            for col in range(8):
                cols[col].append(line[col])

    word = ""
    for col in range(0, 8):
        word += collections.Counter(cols[col]).most_common(1)[0][0]
    print("code word:", word)


def puzzle2():
    cols = [[], [], [], [], [], [], [], []]
    with open("input/day6.txt") as f:
        for line in f:
            for col in range(8):
                cols[col].append(line[col])

    word = ""
    for col in range(8):
        word += collections.Counter(cols[col]).most_common()[-1][0]
    print("code word:", word)


if __name__ == "__main__":
    puzzle1()
    puzzle2()
