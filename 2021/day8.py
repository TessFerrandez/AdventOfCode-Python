from collections import Counter, defaultdict


entries = [[[pattern for pattern in part.split(' ')] for part in line.strip().split(' | ')] for line in open('2021//input//day8.txt').readlines()]
number_of = {'ABCEFG': '0', 'CF': '1', 'ACDEG': '2', 'ACDFG': '3', 'BCDF': '4', 'ABDFG': '5', 'ABDEFG': '6', 'ACF': '7', 'ABCDEFG': '8', 'ABCDFG': '9'}


def merge(lst1, lst2):
    if lst1 == []:
        return lst2
    return list(set(lst1) & set(lst2))


def get_translations(segments) -> dict:
    lengths = defaultdict(lambda: [])
    possible = defaultdict(lambda: [])

    for segment in segments:
        lengths[len(segment)].append(segment)

    # numbers in parenthesis below are the number of segments

    # one(2) and seven(3) - the common segments are C/F and the unique segment is A
    combo = Counter(lengths[2][0] + lengths[3][0])
    for key, value in combo.items():
        if value == 2:
            possible[key] = ['C', 'F']
        elif value == 1:
            possible[key] = ['A']

    # one(2) and four(4) share the common segments C/F, but the other two are B/D
    combo = Counter(lengths[2][0] + lengths[4][0])
    for key, value in combo.items():
        if value == 1:
            possible[key] = ['B', 'D']

    # two(5), three(5) and five(5) share the common segments A/D/G -- the unique segments are B/E
    combo = Counter(lengths[5][0] + lengths[5][1] + lengths[5][2])
    for key, value in combo.items():
        if value == 1:
            possible[key] = merge(possible[key], ['B', 'E'])
        if value == 3:
            possible[key] = merge(possible[key], ['A', 'D', 'G'])

    # zero(6), six(6), and nine(6) share the common segments A/B/F/G
    combo = Counter(lengths[6][0] + lengths[6][1] + lengths[6][2])
    for key, value in combo.items():
        if value == 2:
            possible[key] = merge(possible[key], ['C', 'D', 'E'])
        if value == 3:
            possible[key] = merge(possible[key], ['A', 'B', 'F', 'G'])

    # when all is merged, one segment will be A (3rd segment in 7),
    # and one segment will have A and another possible segment,
    # just remove the A since this is already marked as known
    for key, value in possible.items():
        if 'A' in value and len(value) > 1:
            value.remove('A')

    return {key: value[0] for key, value in possible.items()}


def translate(entry):
    segments = entry[0]
    translations = get_translations(segments)
    number_strings = entry[1]
    number = ''
    for number_string in number_strings:
        translated = ''
        for char in number_string:
            translated += translations[char]
        number += number_of[''.join(sorted(translated))]
    return(int(number))


def part1():
    return sum(sum(1 for pattern in entry[1] if len(pattern) <= 4 or len(pattern) == 7) for entry in entries)


print("part 1:", part1())
print("part 2:", sum(translate(entry) for entry in entries))
