from input_processing import read_data


def part1(strategy):
    score = {"A X": 4, "A Y": 8, "A Z": 3,
             "B X": 1, "B Y": 5, "B Z": 9,
             "C X": 7, "C Y": 2, "C Z": 6}
    return sum(score[row] for row in strategy)


def part2(strategy):
    score = {"A X": 3, "A Y": 4, "A Z": 8,
             "B X": 1, "B Y": 5, "B Z": 9,
             "C X": 2, "C Y": 6, "C Z": 7}
    return sum(score[row] for row in strategy)


def test():
    sample_strategy = """A Y
B X
C Z""".splitlines()
    data = sample_strategy
    assert part1(data) == 15
    assert part2(data) == 12


test()
data = read_data(2022, 2).splitlines()
print('Part1:', part1(data))
print('Part2:', part2(data))
