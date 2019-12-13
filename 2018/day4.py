def parse_log(log_lines):
    guards = dict()
    guard_minutes = dict()
    current_guard = ""
    sleep_start = 0

    for log_line in log_lines:

        parts = log_line.split(" ")
        minute = int(parts[1][3:5])
        command, guard_id = parts[2], parts[3]

        if command == "Guard":
            current_guard = guard_id
        if command == "falls":
            sleep_start = minute
        if command == "wakes":
            sleep_end = minute

            if current_guard not in guards:
                guards[current_guard] = sleep_end - sleep_start
                guard_minutes[current_guard] = [0] * 60
            else:
                guards[current_guard] += sleep_end - sleep_start

            for i in range(sleep_start, sleep_end):
                guard_minutes[current_guard][i] += 1

    max_minutes = 0
    best_guard = ""
    for guard in guards:
        if guards[guard] > max_minutes:
            max_minutes = guards[guard]
            best_guard = guard

    print(best_guard)
    max_guard_minutes = guard_minutes[best_guard]
    best_hour = max_guard_minutes.index(max(max_guard_minutes))
    print("part 1:", best_hour * int(best_guard[1:]))

    max_minute = 0
    for guard in guard_minutes:
        guard_max = max(guard_minutes[guard])
        if guard_max > max_minute:
            best_guard = guard
            max_minute = guard_max

    print("part 2:", guard_minutes[best_guard].index(max_minute) * int(best_guard[1:]))


def puzzles():
    log_lines = open("input/day4.txt").readlines()
    log_lines = sorted(log_lines, key=lambda x: x[1: 17])
    parse_log(log_lines)


if __name__ == "__main__":
    puzzles()
