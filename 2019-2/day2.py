from ComputerV1 import Computer


def part1(inputs: str) -> int:
    computer = Computer(inputs, 12, 2)
    computer.run()
    return computer.memory[0]


def part2(inputs: str) -> str:
    for noun in range(100):
        for verb in range(100):
            computer = Computer(inputs, noun, verb)
            computer.run()
            if computer.memory[0] == 19690720:
                return str(noun) + str(verb)
    return ""


inputs = open('2019/input/day2.txt').read().strip()

print("Part 1:", part1(inputs))
print("part 2:", part2(inputs))
