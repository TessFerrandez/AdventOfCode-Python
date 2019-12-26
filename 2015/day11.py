from string import ascii_lowercase
from itertools import groupby


def valid(s):
    if len(set("iol") & set(s)) > 0:
        return False
    if not any([ascii_lowercase[n : n + 3] in s for n in range(24)]):
        return False
    if (
        sum([2 if len(list(y)) >= 4 else 1 for x, y in groupby(s) if len(list(y)) >= 2])
        < 2
    ):
        return False
    return True


def inc(s):
    if s == "":
        return "a"
    elif s[-1] < "z":
        return s[0:-1] + chr(ord(s[-1]) + 1)
    else:
        return inc(s[:-1]) + "a"


def puzzles():
    password = "hepxcrrq"
    while not valid(password):
        password = inc(password)
    print("Part 1: Next password is {0}".format(password))
    password = inc(password)
    while not valid(password):
        password = inc(password)
    print("Part 2: Next password is {0}".format(password))


if __name__ == "__main__":
    puzzles()
