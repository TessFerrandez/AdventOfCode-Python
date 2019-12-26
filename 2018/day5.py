def reduce(the_string):
    reduced = True
    while reduced:
        remove_strings = []
        string_len = len(the_string)

        for i in range(string_len - 1):
            if abs(ord(the_string[i]) - ord(the_string[i + 1])) == 32:
                remove_strings.append(the_string[i] + the_string[i + 1])

        if len(remove_strings) > 0:
            reduced = True
            for remove_str in remove_strings:
                the_string = the_string.replace(remove_str, "")
        else:
            reduced = False

    return the_string


def puzzle1():
    result = reduce(open("input/day5.txt").readline())
    print("puzzle 1:", len(result))


def puzzle2():
    alphabet_low = "abcdefghijklmnopqrstuvwxyz"
    alphabet_cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    original = open("input/day5.txt").readline()
    min_len = 1000000
    for i in range(26):
        reduced = original.replace(alphabet_low[i], "").replace(alphabet_cap[i], "")
        result = reduce(reduced)
        if len(result) < min_len:
            min_len = len(result)

    print("puzzle 2:", min_len)


if __name__ == "__main__":
    puzzle1()
    puzzle2()
