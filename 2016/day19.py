from collections import deque


def who_gets_the_gifts(elf_count: int) -> int:
    pos = 1
    for i in range(1, elf_count + 1):
        if pos > i:
            pos = 1
        # print(i, pos)
        pos += 2
    return pos - 2


def who_gets_the_gifts_p2(elf_count: int) -> int:
    left = deque()
    right = deque()
    for i in range(1, elf_count + 1):
        if i < (elf_count // 2) + 1:
            left.append(i)
        else:
            right.appendleft(i)

    while left and right:
        if len(left) > len(right):
            left.pop()
        else:
            right.pop()

        # rotate
        right.appendleft(left.popleft())
        left.append(right.pop())
    return left[0] or right[0]


def puzzles():
    pos = who_gets_the_gifts(3014387)
    print("3014387 elfs:", pos)

    pos = who_gets_the_gifts_p2(3014387)
    print("3014387 elfs:", pos)


if __name__ == "__main__":
    puzzles()
