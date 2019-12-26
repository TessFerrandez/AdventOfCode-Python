def has_one_difference(string1, string2):
    num_chars = len(string1)

    diffs = 0
    for i in range(0, num_chars):
        if string1[i] != string2[i]:
            diffs += 1
        if diffs > 1:
            return False

    return diffs == 1


def has_double(the_input):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for c in alphabet:
        if the_input.count(c) == 2:
            return True
    return False


def has_triple(the_input):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for c in alphabet:
        if the_input.count(c) == 3:
            return True
    return False


def puzzle1():
    doubles = 0
    triples = 0
    with open("input/day2.txt") as f:
        for line in f:
            if has_double(line):
                doubles += 1
            if has_triple(line):
                triples += 1
    print("checksum:", doubles * triples)


def common(string1, string2):
    common_letters = ""
    for i in range(len(string1)):
        common_letters += string1[i] if string1[i] == string2[i] else ""
    return common_letters


def puzzle2():
    words = []
    with open("input/day2.txt") as f:
        for line in f:
            words.append(line)

    num_words = len(words)
    for i in range(num_words):
        for j in range(i + 1, num_words):
            result = has_one_difference(words[i], words[j])
            if result:
                print("common:", common(words[i], words[j]))
                return


if __name__ == "__main__":
    puzzle1()
    puzzle2()
