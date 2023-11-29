from input_processing import read_data


def parse(data):
    monkey_numbers = {}
    monkey_instructions = {}

    for line in data.splitlines():
        words = line.split(' ')
        if len(words) == 2:
            monkey_numbers[words[0][:-1]] = int(words[1])
        else:
            monkey_instructions[words[0][:-1]] = words[1:]

    return monkey_numbers, monkey_instructions


def part1(monkey_numbers, monkey_instructions):
    def get_monkey_number(name):
        if name not in monkey_numbers:
            m1_name, op, m2_name = monkey_instructions[name]
            m1 = get_monkey_number(m1_name)
            m2 = get_monkey_number(m2_name)

            match op:
                case '+': monkey_numbers[name] = m1 + m2
                case '-': monkey_numbers[name] = m1 - m2
                case '*': monkey_numbers[name] = m1 * m2
                case '/': monkey_numbers[name] = m1 // m2

        return monkey_numbers[name]

    return get_monkey_number('root')


def part2(monkey_numbers, monkey_instructions):
    def get_equations_monkeys_are_part_of():
        monkey_is_part_of = {}

        for monkey_name in monkey_instructions:
            monkey1, _, monkey2 = monkey_instructions[monkey_name]
            monkey_is_part_of[monkey1] = monkey_name
            monkey_is_part_of[monkey2] = monkey_name

        return monkey_is_part_of

    def calculate_number(monkey_name):
        monkey1, op, monkey2 = monkey_instructions[monkey_name]
        match op:
            case '+': return monkey1 + monkey2
            case '-': return monkey1 - monkey2
            case '*': return monkey1 * monkey2
            case '/': return monkey1 // monkey2

    def substitute_all_known_monkey_numbers():
        monkey_is_part_of = get_equations_monkeys_are_part_of()
        known_monkey_numbers = [monkey_name for monkey_name in monkey_numbers.keys() if monkey_name != 'humn']

        while known_monkey_numbers:
            new_known = []
            for known_monkey_name in known_monkey_numbers:
                monkey = monkey_is_part_of[known_monkey_name]
                if monkey_instructions[monkey][0] == known_monkey_name:
                    monkey_instructions[monkey][0] = monkey_numbers[known_monkey_name]
                if monkey_instructions[monkey][2] == known_monkey_name:
                    monkey_instructions[monkey][2] = monkey_numbers[known_monkey_name]
                if isinstance(monkey_instructions[monkey][0], int) and isinstance(monkey_instructions[monkey][2], int):
                    new_known.append(monkey)
                    monkey_numbers[monkey] = calculate_number(monkey)
                    del monkey_instructions[monkey]
            known_monkey_numbers = new_known

    def solve_the_root_monkey_equation():
        left_side_monkey = monkey_instructions['root'][0] if isinstance(monkey_instructions['root'][2], int) else monkey_instructions['root'][2]
        human_number = monkey_instructions['root'][2] if isinstance(monkey_instructions['root'][2], int) else monkey_instructions['root'][0]

        while left_side_monkey != 'humn':
            monkey1, op, monkey2 = monkey_instructions[left_side_monkey]
            match op:
                case '/':
                    human_number *= monkey2
                    left_side_monkey = monkey1
                case '+':
                    if isinstance(monkey1, int):
                        human_number -= monkey1
                        left_side_monkey = monkey2
                    else:
                        human_number -= monkey2
                        left_side_monkey = monkey1
                case '*':
                    if isinstance(monkey1, int):
                        human_number //= monkey1
                        left_side_monkey = monkey2
                    else:
                        human_number //= monkey2
                        left_side_monkey = monkey1
                case '-':
                    if isinstance(monkey2, int):
                        human_number += monkey2
                        left_side_monkey = monkey1
                    else:
                        human_number = monkey1 - human_number
                        left_side_monkey = monkey2

        return human_number

    substitute_all_known_monkey_numbers()
    human_number = solve_the_root_monkey_equation()
    return human_number


def test():
    sample = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""
    monkey_numbers, monkey_instructions = parse(sample)
    assert part1(monkey_numbers, monkey_instructions) == 152
    monkey_numbers, monkey_instructions = parse(sample)
    assert part2(monkey_numbers, monkey_instructions) == 301


test()
monkey_numbers, monkey_instructions = parse(read_data(2022, 21))
print('Part1:', part1(monkey_numbers, monkey_instructions))
monkey_numbers, monkey_instructions = parse(read_data(2022, 21))
print('Part2:', part2(monkey_numbers, monkey_instructions))
