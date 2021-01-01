from datetime import datetime
from typing import List
from collections import defaultdict, Counter


GUARD = 0
SLEEP = 1
WAKE = 2


def parse_input(filename: str):
    lines = [line.strip() for line in open(filename).readlines()]
    log = []
    for line in lines:
        date_str, time_str, p1, p2, *p3 = line.split(' ')
        time_stamp = datetime.strptime((date_str + ' ' + time_str)[1:-1], '%Y-%m-%d %H:%M')
        if p1 == 'Guard':
            action = GUARD
            value = int(p2[1:])
        elif p1 == 'falls':
            action = SLEEP
            value = time_stamp.minute
        else:
            action = WAKE
            value = time_stamp.minute
        log.append([time_stamp, action, value])
    log.sort()
    return log


def part1(guards: dict) -> int:

    max_sleep = 0
    sleepiest_guard = 0
    for guard in guards:
        if len(guards[guard]) > max_sleep:
            max_sleep = len(guards[guard])
            sleepiest_guard = guard

    max_count = 0
    max_value = 0
    counts = Counter(guards[sleepiest_guard])
    for val in counts:
        if counts[val] > max_count:
            max_count = counts[val]
            max_value = val

    return sleepiest_guard * max_value


def part2(guards: dict) -> int:
    max_count = 0
    max_guard = 0
    for guard in guards:
        counts = Counter(guards[guard])
        max_sleep = max(counts.values())
        if max_sleep > max_count:
            max_count = max_sleep
            max_guard = guard

    counts = Counter(guards[max_guard])
    for minute in counts:
        if counts[minute] == max_count:
            return minute * max_guard

    return 0


def parse_log(log: List[List]) -> dict:
    current_guard = 0
    sleep = 0

    guards = defaultdict(lambda: [])

    for _, action, value in log:
        if action == GUARD:
            current_guard = value
        elif action == SLEEP:
            sleep = value
        elif action == WAKE:
            guards[current_guard] += [d for d in range(sleep, value)]

    return dict(guards)


def main():
    log = parse_input('input/day4.txt')
    guards = parse_log(log)
    print(f'Part 1: {part1(guards)}')
    print(f'Part 2: {part2(guards)}')


if __name__ == "__main__":
    main()
