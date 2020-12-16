from collections import defaultdict
from typing import List


def value_to_bot(bot: int, value: int, bots: dict):
    bots[bot].append(value)
    bots[bot].sort()


def parse_input(filename: str) -> (dict, dict):
    bots = defaultdict(lambda: [])
    instructions = {}

    lines = [line.strip().split() for line in open(filename).readlines()]

    for line in lines:
        if line[0] == 'value':
            bot, value = int(line[5]), int(line[1])
            value_to_bot(bot, value, bots)
        else:
            bot = int(line[1])
            if line[5] == 'output':
                low_bot, low_out = int(line[6]), True
            else:
                low_bot, low_out = int(line[6]), False
            if line[10] == 'output':
                high_bot, high_out = int(line[11]), True
            else:
                high_bot, high_out = int(line[11]), False
            instructions[bot] = [low_bot, low_out, high_bot, high_out]
    return bots, instructions


def process_bot(bot: int, bots: dict, outputs: List[int], instructions: dict):
    low_bot, low_out, high_bot, high_out = instructions[bot]
    low, high = bots[bot]
    if low_out:
        outputs[low_bot] = low
    else:
        value_to_bot(low_bot, low, bots)
    if high_out:
        outputs[high_bot] = high
    else:
        value_to_bot(high_bot, high, bots)
    bots[bot] = []


def part1(bots: dict, instructions: dict, outputs: List[int]) -> int:
    bot_processing_17_61 = 0

    while True:
        bots_to_process = []
        for bot in bots:
            if len(bots[bot]) == 2:
                bots_to_process.append(bot)

        if not bots_to_process:
            break

        for bot in bots_to_process:
            if bots[bot] == [17, 61]:
                bot_processing_17_61 = bot
            process_bot(bot, bots, outputs, instructions)

    return bot_processing_17_61


def part2(outputs: List[int]) -> int:
    return outputs[0] * outputs[1] * outputs[2]


def main():
    bots, instructions = parse_input('input/day10.txt')
    outputs = [0] * 210
    print(f'Part 1: {part1(bots, instructions, outputs)}')
    print(f'Part 2: {part2(outputs)}')


if __name__ == "__main__":
    main()
