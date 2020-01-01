def spinlock(skip=3, last=2017) -> list:
    buffer = [0]

    current_pos = 0
    for step in range(1, last + 1):
        current_pos = (current_pos + skip) % step + 1
        buffer.insert(current_pos, step)

    return buffer


def spinlock_0(skip=3, last=2017) -> int:
    # nothing is ever inserted at pos 1
    # since we always add 1 to the modulo
    # so num after 0 is last item placed in pos 1
    at_pos_1 = 0

    current_pos = 0
    for step in range(1, last + 1):
        current_pos = (current_pos + skip) % step + 1
        if current_pos == 1:
            at_pos_1 = step

    return at_pos_1


def puzzles():
    buffer = spinlock(345)
    i = buffer.index(2017)
    print("item after 2017:", buffer[i + 1])
    pos_1 = spinlock_0(345, 50000000)
    print("item after 0:", pos_1)


if __name__ == "__main__":
    puzzles()
