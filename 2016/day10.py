bots = dict()
outputs = [0] * 210
instructions = dict()


def give_value_to_bot(bot, value):
    if bot in bots:
        bots[bot].append(value)
        bots[bot].sort()
    else:
        bots[bot] = [value]


def parse_input():
    lines = [line.strip().split() for line in open("input/day10.txt").readlines()]
    for line in lines:
        if line[0] == "value":
            bot = int(line[5])
            value = int(line[1])
            give_value_to_bot(bot, value)
        else:
            bot = int(line[1])
            if line[5] == "output":
                low_bot = int(line[6])
                low_out = True
            else:
                low_bot = int(line[6])
                low_out = False
            if line[10] == "output":
                high_bot = int(line[11])
                high_out = True
            else:
                high_bot = int(line[11])
                high_out = False
            instructions[bot] = [low_bot, low_out, high_bot, high_out]


def process_bot(bot):
    values = bots[bot]
    if values == [17, 61]:
        print("bot", bot, "compares 17 and 61")
    instruction = instructions[bot]
    if instruction[1]:
        outputs[instruction[0]] = values[0]
    else:
        give_value_to_bot(instruction[0], values[0])
    if instruction[3]:
        outputs[instruction[2]] = values[1]
    else:
        give_value_to_bot(instruction[2], values[1])


def follow_instructions():
    while True:
        bot_to_process = -1
        for bot in bots:
            if len(bots[bot]) == 2:
                bot_to_process = bot
                break

        if bot_to_process == -1:
            break

        process_bot(bot_to_process)
        bots[bot_to_process] = []


def puzzles():
    parse_input()
    follow_instructions()
    print(outputs[0:3])
    print("multiply:", outputs[0] * outputs[1] * outputs[2])


if __name__ == "__main__":
    puzzles()
