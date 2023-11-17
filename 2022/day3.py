from input_processing import read_data


def priority(ch):
    if ch == ch.lower():
        return ord(ch) - ord('a') + 1
    else:
        return ord(ch) - ord('A') + 27


def get_common_item_in_compartments(rucksack):
    half = len(rucksack) // 2
    compartment1, compartment2 = rucksack[:half], rucksack[half:]
    compartment1 = set(list(compartment1))
    compartment2 = set(list(compartment2))

    for ch in compartment1:
        if ch in compartment2:
            return ch
    return None


def get_common_item_in_elf_group(elf_group):
    elf1, elf2, elf3 = elf_group
    elf1 = set(list(elf1))
    elf2 = set(list(elf2))
    elf3 = set(list(elf3))

    for ch in elf1:
        if ch in elf2 and ch in elf3:
            return ch
    return None


def part1(rucksacks):
    return sum(priority(get_common_item_in_compartments(rucksack)) for rucksack in rucksacks)


def part2(rucksacks):
    elf_groups = [rucksacks[i: i + 3] for i in range(0, len(rucksacks), 3)]
    return sum(priority(get_common_item_in_elf_group(elf_group)) for elf_group in elf_groups)


def test():
    sample = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines()
    assert part1(sample) == 157
    assert part2(sample) == 70


test()
data = read_data(2022, 3).splitlines()
print('Part1:', part1(data))
print('Part2:', part2(data))
