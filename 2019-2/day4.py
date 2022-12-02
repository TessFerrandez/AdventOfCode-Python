MIN, MAX = 124075, 580759


def never_decreses(password: str) -> bool:
    for i in range(len(password) - 1):
        if password[i] > password[i + 1]:
            return False
    return True


def has_double(password: str) -> bool:
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            return True
    return False


def has_true_double(password: str) -> bool:
    password = "." + password + "."
    for i in range(1, len(password) - 2):
        if password[i] == password[i + 1] and password[i] != password[i - 1] and password[i] != password[i + 2]:
            return True
    return False


def is_valid(password: int) -> bool:
    password_str: str = str(password)
    return has_double(password_str) and never_decreses(password_str)


def is_valid2(password: int) -> bool:
    password_str = str(password)
    return never_decreses(password_str) and has_true_double(password_str)


def part1() -> int:
    return sum(1 for password in range(MIN, MAX + 1) if is_valid(password))


def part2() -> int:
    return sum(1 for password in range(MIN, MAX + 1) if is_valid2(password))


def tests():
    assert is_valid(111111)
    assert not is_valid(223450)
    assert not is_valid(123789)
    assert is_valid2(112233)
    assert not is_valid2(123444)
    assert is_valid2(111122)


tests()
print("Part 1:", part1())
print("Part 2:", part2())
