def find_loop_size(key: int) -> int:
    subject_number = 7
    value = 1
    i = 0
    while value != key:
        i += 1
        value *= subject_number
        value = value % 20201227
    return i


def transform(subject_number: int, loop_size: int) -> int:
    value = 1
    for _ in range(loop_size):
        value *= subject_number
        value = value % 20201227
    return value


def part1(card_key: int, door_key: int) -> int:
    card_loop = find_loop_size(card_key)
    return transform(door_key, card_loop)


def main():
    # card_pub_key = 5764801
    # door_pub_key = 17807724
    card_pub_key = 8987316
    door_pub_key = 14681524
    print(f'Part 1: {part1(card_pub_key, door_pub_key)}')


if __name__ == "__main__":
    main()
