from functools import reduce


def calc_knot_hash(nums: list, lengths: list, pos: int, skip: int) -> (int, int):
    for l in lengths:
        to_reverse = []
        for i in range(l):
            n = (pos + i) % 256
            to_reverse.append(nums[n])
        to_reverse.reverse()
        for i in range(l):
            n = (pos + i) % 256
            nums[n] = to_reverse[i]
        pos = (pos + l + skip) % 256
        skip += 1

    return pos, skip


def puzzle1():
    input_string = open("input/day10.txt").read().strip()
    lengths = [int(n) for n in input_string.split(",")]

    nums = [n for n in range(256)]
    calc_knot_hash(nums, lengths, 0, 0)

    print("puzzle 1:", nums[0] * nums[1])


def puzzle2():
    input_string = open("input/day10.txt").read().strip()
    lengths = [ord(char) for char in input_string]
    lengths.extend([17, 31, 73, 47, 23])
    nums = [n for n in range(256)]
    pos, skip = 0, 0

    for _ in range(64):
        pos, skip = calc_knot_hash(nums, lengths, pos, skip)

    dense = []
    for i in range(16):
        sub_slice = nums[16 * i : 16 * i + 16]
        dense.append("%02x" % reduce((lambda x, y: x ^ y), sub_slice))
    print("puzzle 2:", "".join(dense))


def puzzles():
    puzzle1()
    puzzle2()


if __name__ == "__main__":
    puzzles()
