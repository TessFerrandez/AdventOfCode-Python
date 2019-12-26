def remove_exclamations(input_str: str) -> str:
    while True:
        try:
            start_excl = input_str.index("!")
            input_str = input_str[0:start_excl] + input_str[start_excl + 2 :]
        except ValueError:
            break

    return input_str


def remove_garbage(input_str: str) -> (str, int):
    garbage_count = 0
    while True:
        try:
            start_garbage = input_str.index("<")
            end_garbage = input_str.index(">", start_garbage)
            garbage_count += end_garbage - start_garbage - 1
            input_str = input_str[0:start_garbage] + input_str[end_garbage + 1 :]
        except ValueError:
            break

    return input_str, garbage_count


def count_groups(input_str: str) -> (int, int):
    group_level = 0
    total_groups = 0
    group_score = 0

    for char in input_str:
        if char == "{":
            group_level += 1
        if char == "}":
            group_score += group_level
            group_level -= 1
            total_groups += 1

    return total_groups, group_score


def puzzles():
    input_string = open("input/day9.txt").readline().strip()
    input_string = remove_exclamations(input_string)
    input_string, garbage_count = remove_garbage(input_string)
    total_groups, group_score = count_groups(input_string)
    print("groups:", total_groups)
    print("group score:", group_score)
    print("garbage count:", garbage_count)


if __name__ == "__main__":
    puzzles()
