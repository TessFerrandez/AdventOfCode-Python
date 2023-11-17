from input_processing import read_data


def get_directory_contents(data):
    all_contents = []
    directory_contents = [0]
    rows = data.splitlines()

    for row in rows:
        if row.startswith("$ cd /"):
            pass
        elif row.startswith("dir"):
            pass
        elif row.startswith("$ ls"):
            pass
        elif row.startswith("$ cd .."):
            contents = directory_contents.pop()
            all_contents.append(contents)
            directory_contents[-1] += contents
        elif row.startswith("$ cd "):
            directory_contents.append(0)
        else:
            file_size = int(row.split()[0])
            directory_contents[-1] += file_size

    while directory_contents:
        contents = directory_contents.pop()
        all_contents.append(contents)
        if directory_contents:
            directory_contents[-1] += contents

    return all_contents


def part1(contents):
    return sum(content for content in contents if content <= 100000)


def part2(contents):
    contents.sort()
    needed = 30000000 - (70000000 - contents[-1])
    for content in contents:
        if content >= needed:
            return content


def test():
    sample = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
    contents = get_directory_contents(sample)
    assert part1(contents) == 95437
    assert part2(contents) == 24933642


test()
contents = get_directory_contents(read_data(2022, 7))
print('Part1:', part1(contents))
print('Part2:', part2(contents))
