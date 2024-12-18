from input_processing import read_data
import re


def parse(data):
    groups = data.split('\n\n')
    machines = []
    for group in groups:
        machines.append([int(d) for d in re.findall(r'-?\d+', group)])
    return machines


def min_cost(ax, ay, bx, by, px, py):
    b, b_reminder = divmod(ay * px - ax * py, ay * bx - ax * by)
    a, a_reminder = divmod(px - b * bx, ax)
    return 0 if a_reminder or b_reminder else a * 3 + b


def part1(machines):
    return sum(min_cost(*machine) for machine in machines)


def part2(data):
    total = 0
    for machine in data:
        ax, ay, bx, by, px, py = machine
        total += min_cost(ax, ay, bx, by, px + 10000000000000, py + 10000000000000)
    return total


def test():
    data = '''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279'''
    assert part1(parse(data)) == 480
    assert part2(parse(data)) == 875318608908


test()
data = read_data(2024, 13)
print('Part1:', part1(parse(data)))
print('Part2:', part2(parse(data)))
