from collections import Counter


def has_2_or_more_matching(pw_str: str) -> bool:
    for i in range(5):
        if pw_str[i] == pw_str[i + 1]:
            return True
    return False


def has_exactly_2_matching(pw_str: str) -> bool:
    counts = Counter(pw_str)
    for i in counts:
        if counts[i] == 2:
            return True
    return False


def part1(range_from: int, range_to: int) -> int:
    num_passwords = 0

    for password in range(range_from, range_to + 1):
        pw_str = str(password)
        if not pw_str == ''.join(sorted(pw_str)):
            continue
        if not has_2_or_more_matching(pw_str):
            continue
        num_passwords += 1

    return num_passwords


def part2(range_from: int, range_to: int) -> int:
    num_passwords = 0

    for password in range(range_from, range_to + 1):
        pw_str = str(password)
        if not pw_str == ''.join(sorted(pw_str)):
            continue
        if not has_exactly_2_matching(pw_str):
            continue
        num_passwords += 1

    return num_passwords


def main():
    range_from = 124075
    range_to = 580769
    print(f'Part 1: {part1(range_from, range_to)}')
    print(f'Part 2: {part2(range_from, range_to)}')


if __name__ == "__main__":
    main()
