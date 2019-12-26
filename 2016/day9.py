def decompress(input_string: str) -> str:
    output_string = ""

    i = 0
    while i < len(input_string):
        if input_string[i] == "(":
            x_index = input_string.index("x", i)
            num_chars = int(input_string[i + 1 : x_index])
            right_index = input_string.index(")", x_index)
            times = int(input_string[x_index + 1 : right_index])
            chars_to_duplicate = input_string[
                right_index + 1 : right_index + 1 + num_chars
            ]
            output_string += chars_to_duplicate * times
            i = right_index + 1 + num_chars
        else:
            output_string += input_string[i]
            i += 1

    return output_string


def decompress_recursive_count(input_string: str) -> int:
    decompressed_length = 0
    i = 0
    while i < len(input_string):
        if input_string[i] == "(":
            x_index = input_string.index("x", i)
            num_chars = int(input_string[i + 1 : x_index])
            right_index = input_string.index(")", x_index)
            times = int(input_string[x_index + 1 : right_index])
            chars_to_duplicate = input_string[
                right_index + 1 : right_index + 1 + num_chars
            ]
            decompressed_length += times * decompress_recursive_count(
                chars_to_duplicate
            )
            i = right_index + 1 + num_chars
        else:
            decompressed_length += 1
            i += 1
    return decompressed_length


def puzzles():
    input_string = open("input/day9.txt").readline().strip()
    out = decompress(input_string)
    print("decompressed length:", len(out))
    input_string = open("input/day9.txt").readline().strip()
    print("decompressed length (V2):", decompress_recursive_count(input_string))


if __name__ == "__main__":
    puzzles()
