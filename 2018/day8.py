from typing import List


def parse_input(filename: str) -> List[int]:
    return [int(d) for d in open(filename).read().strip().split(' ')]


def get_metadata(data: List[int]) -> int:
    num_children = data.pop(0)
    num_metadata = data.pop(0)

    # get the metadata values for all the children
    total = 0
    for _ in range(num_children):
        total += get_metadata(data)

    # and add the meta data for this node
    for _ in range(num_metadata):
        total += data.pop(0)

    return total


def part1(data: List[int]) -> int:
    return get_metadata(data)


def get_value(data: List[int]) -> int:
    num_children = data.pop(0)
    num_metadata = data.pop(0)

    # get all children's values
    child_values = []
    for _ in range(num_children):
        child_values.append(get_value(data))

    # get all metadata values
    metadata_values = []
    for _ in range(num_metadata):
        metadata_values.append(data.pop(0))

    # if no children - return the total meta data
    if num_children == 0:
        return sum(metadata_values)

    # else - return the values for the children pointed out by the metadata
    total = 0
    for child in metadata_values:
        if 0 < child <= num_children:
            total += child_values[child - 1]

    return total


def part2(data: List[int]) -> int:
    return get_value(data)


def main():
    data = parse_input('input/day8.txt')
    print(f'Part 1: {part1(data)}')
    data = parse_input('input/day8.txt')
    print(f'Part 2: {part2(data)}')


if __name__ == "__main__":
    main()
