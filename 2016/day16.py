def dragon_curve(input_string: str, size: int) -> str:
    a = input_string
    while len(a) < size:
        b = a[::-1]
        b = b.replace("0", "x").replace("1", "0").replace("x", "1")
        a += "0" + b
    return a[:size]


def get_checksum(input_string: str) -> str:
    checksum = input_string

    while len(checksum) % 2 == 0:
        pairs = [(checksum[i : i + 2]) for i in range(0, len(checksum), 2)]
        checksum = ""
        for pair in pairs:
            checksum += "1" if pair[0] == pair[1] else "0"

    return checksum


def puzzles():
    generated_string = dragon_curve("10111100110001111", 272)
    checksum = get_checksum(generated_string)
    print("checksum:", checksum)
    generated_string = dragon_curve("10111100110001111", 35651584)
    checksum = get_checksum(generated_string)
    print("checksum:", checksum)


if __name__ == "__main__":
    puzzles()
