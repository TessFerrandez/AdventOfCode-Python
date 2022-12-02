from input_processing import read_data, lines_as_num_array, get_groups, read_sample_data


def parse(data):
    return [lines_as_num_array(group) for group in get_groups(data)]


def part1(data):
    return max(sum(elf_calories) for elf_calories in data)


def part2(data):
    calory_sums = [sum(elf_calories) for elf_calories in data]
    calory_sums.sort(reverse=True)
    return sum(calory_sums[:3])


def test():
    data = parse(read_sample_data(2022, 1))
    assert part1(data) == 24000
    assert part2(data) == 45000


test()
data = parse(read_data(2022, 1))
print('Part1:', part1(data))
print('Part2:', part2(data))
