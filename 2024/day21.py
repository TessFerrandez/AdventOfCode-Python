# code from https://github.com/drz416/aoc/blob/main/2024/Day21/d21p2.py
from functools import lru_cache


def solve(codes, robots=2):
    numpad = {
        "A": {"0": ("<A",),
              "1": ("<^<A", "^<<A",),
              "2": ("<^A", "^<A",),
              "3": ("^A",),
              "4": ("<^<^A", "<^^<A", "^<<^A", "^<^<A", "^^<<A",),
              "5": ("<^^A", "^<^A", "^^<A",),
              "6": ("^^A",),
              "7": ("<^<^^A", "<^^<^A", "<^^^<A", "^<<^^A", "^<^<^A", "^<^^<A",
                    "^^<<^A", "^^<^<A", "^^^<<A",),
              "8": ("<^^^A", "^<^^A", "^^<^A", "^^^<A",),
              "9": ("^^^A",)},
        "0": {"0": ("A",),
              "1": ("^<A",),
              "2": ("^A",),
              "3": ("^>A", ">^A",),
              "4": ("^<^A", "^^<A",),
              "5": ("^^A",),
              "6": ("^^>A", "^>^A", ">>^A",),
              "7": ("^<^^A", "^^<^A", "^^^<A",),
              "8": ("^^^A",),
              "9": ("^^^>A", "^^>^A", "^>^^A", ">^^^A",)},
        "1": {"1": ("A",),
              "2": (">A",),
              "3": (">>A",),
              "4": ("^A",),
              "5": ("^>A", ">^A",),
              "6": ("^>>A", ">^>A", ">>^A",),
              "7": ("^^A",),
              "8": ("^^>A", "^>^A", ">>^A",),
              "9": ("^^>>A", "^>^>A", "^>>^A", ">^^>A", ">^>^A", ">>^^A",)},
        "2": {"2": ("A",),
              "3": (">A",),
              "4": ("<^A", "^<A",),
              "5": ("^A",),
              "6": ("^>A", ">^A",),
              "7": ("<^^A", "^<^A", "^^<A",),
              "8": ("^^A",),
              "9": ("^^>A", "^>^A", ">^^A",)},
        "3": {"3": ("A",),
              "4": ("<<^A", "<^<A", "^<<A",),
              "5": ("<^A", "^<A",),
              "6": ("^A",),
              "7": ("<<^^A", "<^<^A", "<^^<A", "^<<^A", "^<^<A", "^^<<A",),
              "8": ("<^^A", "^<^A", "^^<A",),
              "9": ("^^A",)},
        "4": {"4": ("A",),
              "5": (">A",),
              "6": (">>A",),
              "7": ("^A",),
              "8": ("^>A", ">^A",),
              "9": ("^>>A", ">^>A", ">>^A",)},
        "5": {"5": ("A",),
              "6": (">A",),
              "7": ("<^A", "^<A",),
              "8": ("^A",),
              "9": ("^>A", ">^A",)},
        "6": {"6": ("A",),
              "7": ("<<^A", "<^<A", "^<<A",),
              "8": ("<^A", "^<A",),
              "9": ("^A",)},
        "7": {"7": ("A",),
              "8": (">A",),
              "9": (">>A",)},
        "8": {"8": ("A",),
              "9": (">A",)},
        "9": {"9": ("A",),},
    }

    # Start recursive search with memoization
    human_at_level = robots + 1
    ans = 0
    for code in codes:
        prev_button = "A"
        final_length = 0
        for next_button in code:
            shortest_sequence = 10 ** 20
            try:
                possible_paths = numpad[prev_button][next_button]
            except KeyError:
                possible_paths = reverse_sequences(numpad[next_button][prev_button])
            for path in possible_paths:
                shortest_sequence = min(shortest_sequence, find_shortest(path, robot_level=1, human_level=human_at_level))
            final_length += shortest_sequence
            prev_button = next_button

        # print(f"{code} {final_length=}")
        ans += final_length * int(code[:-1])

    return ans


@lru_cache
def reverse_sequences(directions: tuple[str]) -> tuple[str]:
    reversal_map = {
        "^": "v",
        ">": "<",
        "v": "^",
        "<": ">",
    }
    reversed_possibilities = tuple()
    for direction in directions:
        rev = ""
        for c in direction[-2::-1]:
            rev += reversal_map[c]
        reversed_possibilities += (rev+"A",)
    return reversed_possibilities


@lru_cache
def find_shortest(path: str, robot_level: int, human_level: int) -> int:
    if robot_level == human_level:
        return len(path)

    prev_button = "A"
    final_length = 0
    for next_button in path:
        shortest_sequence = 10 ** 20
        possible_paths = get_dirpad_paths(prev_button, next_button)
        for path in possible_paths:
            shortest_sequence = min(shortest_sequence, find_shortest(path, robot_level=robot_level+1, human_level=human_level))
        final_length += shortest_sequence
        prev_button = next_button
    return final_length


@lru_cache
def get_dirpad_paths(from_key: str, to_key: str) -> tuple[str]:
    dirpad = {
        "A": {"A": ("A",),
              "^": ("<A",),
              "<": ("<v<A", "v<<A",),
              "v": ("<vA", "v<A",),
              ">": ("vA",)},
        "^": {"^": ("A",),
              "<": ("v<A",),
              "v": ("vA",),
              ">": ("v>A", ">vA",)},
        "<": {"<": ("A",),
              "v": (">A",),
              ">": (">>A",)},
        "v": {"v": ("A",),
              ">": (">A",)},
        ">": {">": ("A",),},
    }
    try:
        possible_paths = dirpad[from_key][to_key]
    except KeyError:
        possible_paths = reverse_sequences(dirpad[to_key][from_key])
    return possible_paths


def parse(data):
    return data.split('\n')


def part1(codes):
    return solve(codes, robots=2)


def part2(codes):
    return solve(codes, robots=25)


def test():
    data = '''029A
980A
179A
456A
379A'''
    assert part1(parse(data)) == 126384


test()
data = '''286A
480A
140A
413A
964A'''
print('Part1:', part1(parse(data)))
print('Part2:', part2(parse(data)))

