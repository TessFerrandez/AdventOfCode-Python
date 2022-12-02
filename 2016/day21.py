import re
from itertools import permutations


def read_input() -> list:
    return [instruction.strip() for instruction in open("input/day21.txt").readlines()]


def rotate_string(lst: list, steps: int) -> list:
    steps = steps % len(lst)
    return lst[steps:] + lst[:steps]


def scramble(string: str, instructions: list) -> str:
    l_str = list(string)
    for instr in instructions:
        digits = [int(digit) for digit in re.findall(r"\d+", instr)]
        if instr.startswith("swap position"):
            x, y = digits
            l_str[x], l_str[y] = l_str[y], l_str[x]
        elif instr.startswith("swap letter"):
            x, y = instr[12], instr[-1]
            in_x, in_y = l_str.index(x), l_str.index(y)
            l_str[in_x], l_str[in_y] = l_str[in_y], l_str[in_x]
        elif instr.startswith("rotate left"):
            steps = digits[0]
            l_str = rotate_string(l_str, steps)
        elif instr.startswith("rotate right"):
            steps = digits[0]
            l_str = rotate_string(l_str, -steps)
        elif instr.startswith("reverse"):
            x, y = digits
            l_str[x : y + 1] = l_str[x : y + 1][::-1]
        elif instr.startswith("rotate based"):
            ch = instr[-1]
            index = l_str.index(ch)
            index += (index >= 4) + 1
            l_str = rotate_string(l_str, -index)
        elif instr.startswith("move"):
            x, y = digits
            ch = l_str.pop(x)
            l_str = l_str[:y] + [ch] + l_str[y:]

    return "".join(l_str)


def puzzles():
    instructions = read_input()
    result = scramble("abcdefgh", instructions)
    print("scrambled:", result)
    for permutation in permutations("fbgdceah"):
        if scramble(permutation, instructions) == "fbgdceah":
            print("original:", "".join(permutation))
            break


if __name__ == "__main__":
    puzzles()
