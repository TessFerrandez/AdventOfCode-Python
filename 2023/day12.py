from functools import cache
from input_processing import read_data


def parse_row(row):
    springs, groups = row.split(' ')
    groups = [int(group) for group in groups.split(',')]
    return springs, groups


def get_arrangements(springs, groups):
    @cache
    def arrangements(spring_pos, group_pos, current_length):
        n_springs = len(springs)
        n_groups = len(groups)

        if spring_pos == n_springs:
            if group_pos == n_groups and current_length == 0:
                return 1
            elif group_pos == n_groups - 1 and groups[group_pos] == current_length:
                return 1
            else:
                return 0

        spring = springs[spring_pos]

        num_arrangements = 0
        if spring in ('?', '.'):
            if current_length == 0:
                num_arrangements += arrangements(spring_pos + 1, group_pos, 0)
            elif current_length > 0 and group_pos < n_groups and groups[group_pos] == current_length:
                num_arrangements += arrangements(spring_pos + 1, group_pos + 1, 0)
        if spring in ('?', '#'):
            num_arrangements += arrangements(spring_pos + 1, group_pos, current_length + 1)

        return num_arrangements

    return arrangements(0, 0, 0)


def part1(data):
    num_arrangements = 0
    for row in data.splitlines():
        springs, groups = parse_row(row)
        num_arrangements += get_arrangements(springs, groups)
    return num_arrangements


def part2(data):
    num_arrangements = 0
    for row in data.splitlines():
        springs, groups = parse_row(row)
        springs = springs + '?'
        springs = (springs * 5)[:-1]
        groups = groups * 5
        num_arrangements += get_arrangements(springs, groups)
    return num_arrangements


def test():
    sample = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''
    print(part1(sample))
    print(part2(sample))


test()
data = read_data(2023, 12)
print('Part1:', part1(data))
print('Part2:', part2(data))
