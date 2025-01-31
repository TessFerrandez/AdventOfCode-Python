from input_processing import read_data


def parse(data):
    keys = []
    locks = []
    sections = data.split('\n\n')
    for section in sections:
        if section[0][0] == "#":
            key = [0] * 5
            for r, row in enumerate(section.splitlines()):
                for c, cell in enumerate(row):
                    if cell == "#":
                        key[c] = r
            keys.append(key)
        else:
            lock = [0] * 5
            for r, row in enumerate(section.splitlines()[::-1]):
                for c, cell in enumerate(row):
                    if cell == "#":
                        lock[c] = r
            rev_lock = [5 - col for col in lock]
            locks.append(rev_lock)

    return keys, locks


def part1(keys, locks):
    def fits(key, lock):
        for key_col, lock_col in zip(key, lock):
            if key_col > lock_col:
                return False
        return True

    count = 0
    for key in keys:
        for lock in locks:
            if fits(key, lock):
                count += 1
    return count


def test():
    data = '''#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####'''
    keys, locks = parse(data)
    assert part1(keys, locks) == 3


test()
data = read_data(2024, 25)
keys, locks = parse(data)
print('Part1:', part1(keys, locks))
