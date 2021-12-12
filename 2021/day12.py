from collections import defaultdict, Counter
from typing import Dict, List


def get_caves() -> Dict[str, List[str]]:
    lines = [line.strip().split('-') for line in open('2021//input//day12.txt').readlines()]
    caves = defaultdict(list)
    for p1, p2 in lines:
        if p1 == "start":
            caves[p1].append(p2)
        elif p2 == "end":
            caves[p1].append(p2)
        elif p1 == "end":
            caves[p2].append(p1)
        else:
            caves[p1].append(p2)
            caves[p2].append(p1)
    return caves


def get_paths(caves, path_so_far, target):
    paths = []
    for cave in caves[path_so_far[-1]]:
        if cave == target:
            paths.append(path_so_far + [cave])
        elif cave.isupper() or cave not in path_so_far:
            paths += get_paths(caves, path_so_far + [cave], target)
    return paths


def get_paths2(caves, path_so_far, target, has_double=False):
    paths = []
    for cave in caves[path_so_far[-1]]:
        if cave == target:
            paths.append(path_so_far + [cave])
        elif cave.isupper() or cave not in path_so_far:
            paths += get_paths2(caves, path_so_far + [cave], target, has_double)
        elif has_double:
            continue
        else:
            paths += get_paths2(caves, path_so_far + [cave], target, True)
    return paths


caves = get_caves()
paths = get_paths(caves, ['start'], 'end')
print("Part 1:", len(paths))

paths = get_paths2(caves, ['start'], 'end')
print("Part 2:", len(paths))
