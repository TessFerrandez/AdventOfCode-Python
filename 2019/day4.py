"""
Validating passwords
"""


def always_increases(password):
    last = 0
    for digit in password:
        if digit < last:
            return False
        last = digit
    return True


def has_double_or_more(password):
    last = 0
    for digit in password:
        if last == digit:
            return True
        last = digit
    return False


def has_double(password):
    for i in range(1, 10):
        if password.count(i) == 2:
            return True
    return False


def is_good_password(password):
    digits = [int(d) for d in str(password)]
    return always_increases(digits) and has_double_or_more(digits)


def is_good_password_v2(password):
    digits = [int(d) for d in str(password)]
    return always_increases(digits) and has_double(digits)


def puzzle1():
    total_good = sum(
        int(is_good_password(potential_pwd)) for potential_pwd in range(124075, 580770)
    )
    print(total_good, "good passwords")


def puzzle2():
    total_good = sum(
        int(is_good_password_v2(potential_pwd))
        for potential_pwd in range(124075, 580770)
    )
    print(total_good, "good passwords")


if __name__ == "__main__":
    puzzle1()
    puzzle2()
