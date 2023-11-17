from input_processing import read_data_no_strip


def parse_crates(crate_data):
    crate_lines = crate_data.splitlines()[:-1]
    n_crates = (max(len(line) for line in crate_lines) + 1) // 4
    crates = [[] for _ in range(n_crates)]
    for line in crate_lines:
        for i in range(n_crates):
            if len(line) > i * 4 + 1 and line[i * 4 + 1] != ' ':
                crates[i].append(line[i * 4 + 1])
    return [crates[i][::-1] for i in range(n_crates)]


def parse_instructions(instruction_data):
    instructions = []
    for line in instruction_data.splitlines():
        _, n, _, from_crate, _, to_crate = line.split()
        instructions.append((int(n), int(from_crate) - 1, int(to_crate) - 1))

    return instructions


def parse(data):
    crate_data, instruction_data = data.split("\n\n")

    crates = parse_crates(crate_data)
    instructions = parse_instructions(instruction_data)
    return crates, instructions


def part1(crates, instructions):
    for n, from_crate, to_crate in instructions:
        for _ in range(n):
            crates[to_crate].append(crates[from_crate].pop())
    return ''.join(crate[-1] for crate in crates)


def part2(crates, instructions):
    for n, from_crate, to_crate in instructions:
        crates[to_crate] += crates[from_crate][-n:]
        crates[from_crate] = crates[from_crate][:-n]

    return ''.join(crate[-1] for crate in crates)


def test():
    sample = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
    crates, instructions = parse(sample)
    assert part1(crates, instructions) == "CMZ"
    crates, instructions = parse(sample)
    assert part2(crates, instructions) == "MCD"


test()
crates, instructions = parse(read_data_no_strip(2022, 5))
print('Part1:', part1(crates, instructions))
crates, instructions = parse(read_data_no_strip(2022, 5))
print('Part2:', part2(crates, instructions))
