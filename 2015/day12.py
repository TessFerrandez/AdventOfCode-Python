import re
import json


def get_numbers(content):
    numbers = [int(number) for number in re.findall(r'[-\d]+', content)]
    return numbers


def hook(obj):
    if "red" in obj.values():
        return {}
    else:
        return obj


def get_non_red_numbers(content):
    elements = str(json.loads(content, object_hook=hook))
    return map(int, re.findall(r'[-\d]+', elements))


def puzzles():
    print("sum numbers:", sum(get_numbers(open("input/day12.txt").readline())))
    print("sum non red numbers:", sum(get_non_red_numbers(open("input/day12.txt").readline())))


if __name__ == "__main__":
    puzzles()
