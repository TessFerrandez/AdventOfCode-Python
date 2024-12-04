from input_processing import read_data
from collections import defaultdict


def parse(data):
    xes, ms = [], []
    word_soup = defaultdict(lambda: "")
    for i, line in enumerate(data.splitlines()):
        for j, char in enumerate(line):
            word_soup[(i,j)] = char
            if char == 'X':
                xes.append((i,j))
            if char == 'M':
                ms.append((i,j))
    return word_soup, xes, ms


def part1(word_soup, xes):
    left = [(0, 0), (-1, 0), (-2, 0), (-3, 0)]
    right = [(0, 0), (1, 0), (2, 0), (3, 0)]
    up = [(0, 0), (0, -1), (0, -2), (0, -3)]
    down = [(0, 0), (0, 1), (0, 2), (0, 3)]
    northeast = [(0, 0), (1, -1), (2, -2), (3, -3)]
    northwest = [(0, 0), (-1, -1), (-2, -2), (-3, -3)]
    southeast = [(0, 0), (1, 1), (2, 2), (3, 3)]
    southwest = [(0, 0), (-1, 1), (-2, 2), (-3, 3)]
    directions = [left, right, up, down, northeast, northwest, southeast, southwest]

    def find_xmas(x, y):
        count_found = 0
        for direction in directions:
            word = "".join([word_soup[(x+dx, y+dy)] for dx, dy in direction])
            if word == "XMAS":
                count_found += 1
        return count_found

    return sum([find_xmas(x, y) for x, y in xes])


def part2(word_soup, ms):
    northeast = [(0, 0), (1, -1), (2, -2)]
    northwest = [(0, 0), (-1, -1), (-2, -2)]
    southeast = [(0, 0), (1, 1), (2, 2)]
    southwest = [(0, 0), (-1, 1), (-2, 2)]
    directions = [northeast, northwest, southeast, southwest]

    def find_mas(x, y):
        centers = []
        for direction in directions:
            word = "".join([word_soup[(x+dx, y+dy)] for dx, dy in direction])
            if word == "MAS":
                centers.append((x + direction[1][0], y + direction[1][1]))
        return centers

    xmas_found = 0
    centers_found = set()
    for m in ms:
        centers = find_mas(m[0], m[1])
        for center in centers:
            if center in centers_found:
                xmas_found += 1
            else:
                centers_found.add(center)
    return xmas_found


def test():
    data = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''
    word_soup, xes, ms = parse(data)
    assert part1(word_soup, xes) == 18
    assert part2(word_soup, ms) == 9
    print('Test passed')


test()
data = read_data(2024, 4)
word_soup, xes, ms = parse(data)
print('Part1:', part1(word_soup, xes))
print('Part2:', part2(word_soup, ms))
