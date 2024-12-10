from input_processing import read_data


def parse(data):
    return [int(d) for d in data]


def part1(data):
    files = data[::2]
    spaces = data[1::2]
    file_spread = []
    for id, num in enumerate(files):
        file_spread += [id] * num
    total_files = len(file_spread)

    disk = []
    id = 0
    while file_spread and id < len(spaces):
        disk += [id] * files[id]
        for _ in range(spaces[id]):
            disk.append(file_spread.pop())
        id += 1

    return sum(i * id for i, id in enumerate(disk[:total_files]))


class DiskElement:
    pos: int
    size: int

    def __init__(self, pos, size):
        self.pos = pos
        self.size = size


def part2(data):
    files = []
    spaces = []
    pos = 0

    is_file = True
    for size in data:
        if is_file:
            files.append([pos, size])
        else:
            spaces.append([pos, size])
        is_file = not is_file
        pos += size

    for i in range(len(files) -1, -1, -1):
        for j in range(len(spaces)):
            if spaces[j][0] > files[i][0]:
                break
            if spaces[j][1] >= files[i][1]:
                files[i][0] = spaces[j][0]
                if spaces[j][1] == files[i][1]:
                    spaces.pop(j)
                else:
                    spaces[j][0] += files[i][1]
                    spaces[j][1] -= files[i][1]
                break

    result = 0
    for file_id in range(len(files)):
        result += file_id * sum(range(files[file_id][0], files[file_id][0] + files[file_id][1]))
    return result


def test():
    data = '''2333133121414131402'''
    assert part1(parse(data)) == 1928
    assert part2(parse(data)) == 2858

test()
data = read_data(2024, 9)
print('Part1:', part1(parse(data)))
print('Part2:', part2(parse(data)))
