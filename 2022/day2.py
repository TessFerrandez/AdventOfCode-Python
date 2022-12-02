from input_processing import read_data, read_sample_data


ROCK = 1
PAPER = 2
SCISSORS = 3
LOSE = 0
DRAW = 3
WIN = 6


def parse(data):
    return [line.split(' ') for line in data.splitlines()]


def part1(instructions):
    shapes = {'A': ROCK, 'B': PAPER, 'C': SCISSORS, 'X': ROCK, 'Y': PAPER, 'Z': SCISSORS}

    score = 0

    for opponent, you in instructions:
        op_shape, your_shape = shapes[opponent], shapes[you]
        score += your_shape
        if op_shape == your_shape:
            score += DRAW
        elif (op_shape == ROCK and your_shape == PAPER) or (op_shape == PAPER and your_shape == SCISSORS) or (op_shape == SCISSORS and your_shape == ROCK):
            score += WIN

    return score


def part2(instructions):
    shapes = {'A': ROCK, 'B': PAPER, 'C': SCISSORS}
    outcomes = {'X': LOSE, 'Y': DRAW, 'Z': WIN}

    score = 0

    for opponent, outcome in instructions:
        op_shape, outcome = shapes[opponent], outcomes[outcome]
        score += outcome
        if outcome == DRAW:
            score += op_shape
        elif outcome == WIN:
            if op_shape == ROCK:
                score += PAPER
            elif op_shape == PAPER:
                score += SCISSORS
            else:
                score += ROCK
        else:
            if op_shape == ROCK:
                score += SCISSORS
            elif op_shape == PAPER:
                score += ROCK
            else:
                score += PAPER

    return score


def test():
    data = parse(read_sample_data(2022, 2))
    assert part1(data) == 15
    assert part2(data) == 12


test()
data = parse(read_data(2022, 2))
print('Part1:', part1(data))
print('Part2:', part2(data))
