from IntCode import IntCode


def calculate_output(program_string, noun, verb):
    program = (list(map(str, program_string.split(','))))
    program[1] = noun
    program[2] = verb
    program = ','.join(x for x in program)
    computer = IntCode(program)
    computer.run()
    return computer.memory[0]


def puzzle1():
    program_string = open('input/day2.txt').readline()
    result = calculate_output(program_string, '12', '2')
    print("result for 1202:", result)


def puzzle2():
    program_string = open('input/day2.txt').readline()

    for noun in range(100):
        for verb in range(100):
            result = calculate_output(program_string, str(noun), str(verb))
            if result == 19690720:
                print(str(noun)+str(verb), "produced 19690720")
                return


if __name__ == "__main__":
    puzzle1()
    puzzle2()
