import re


def has_3_vowels(password):
    return True if re.search(r"[aeiou].*[aeiou].*[aeiou]", password, re.IGNORECASE) else False


def has_doubles(password):
    return True if re.search(r"(.)\1", password, re.IGNORECASE) else False


def doesnt_contain_strings(password):
    return False if re.search(r"(ab|cd|pq|xy)", password, re.IGNORECASE) else True


def is_nice(password):
    return has_3_vowels(password) and \
           has_doubles(password) and \
           doesnt_contain_strings(password)


def is_nice2(password):
    if len(re.findall(r"([a-z]{2}).*\1", password)) and \
       re.findall(r"([a-z]).\1", password):
        return True
    return False


def puzzle1():
    nice_passwords = sum(is_nice(line) for line in open('input/day5.txt'))
    print(nice_passwords, "nice passwords")


def puzzle2():
    nice_passwords = sum(is_nice2(line) for line in open('input/day5.txt'))
    print(nice_passwords, "extra nice passwords")


if __name__ == "__main__":
    puzzle1()
    puzzle2()