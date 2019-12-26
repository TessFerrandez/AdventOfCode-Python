def calculate_escape_chars(code_string):
    decoded = bytes(code_string, "utf-8").decode("unicode_escape")
    return len(code_string) - (len(decoded) - 2)


def encode(code_string):
    encoded_string = code_string.replace("\\", "\\\\")
    encoded_string = encoded_string.replace('"', '\\"')
    return encoded_string


def calculate_extra_escape_chars(code_string):
    encoded = encode(code_string)
    return len(encoded) - (len(code_string) - 2)


def puzzles():
    code_strings = [code.strip() for code in open("input/day8.txt").readlines()]
    sum_escape_chars = sum(calculate_escape_chars(code) for code in code_strings)
    print("escape chars:", sum_escape_chars)
    sum_extra_escape_chars = sum(
        calculate_extra_escape_chars(code) for code in code_strings
    )
    print("extra escape chars:", sum_extra_escape_chars)


if __name__ == "__main__":
    puzzles()
