def elves_say(number):
    last_digit = ""
    num_copies = 0
    out_string = ""

    for digit in number:
        num_copies += 1
        if last_digit != digit:
            if last_digit != "":
                out_string += str(num_copies) + last_digit
            num_copies = 0
        last_digit = digit
    out_string += str(num_copies + 1) + last_digit

    return out_string


def puzzles():
    number = "1113122113"
    for i in range(40):
        number = elves_say(number)
    print("length of result:", len(number))

    number = "1113122113"
    for i in range(50):
        number = elves_say(number)
    print("length of result:", len(number))


if __name__ == "__main__":
    puzzles()
