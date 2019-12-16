def execute_jumps(pointers: list) -> int:
    ptr, steps = 0, 0
    max_ptr = len(pointers)
    while ptr < max_ptr:
        next_move = pointers[ptr]
        pointers[ptr] += 1
        ptr += next_move
        steps += 1

    return steps


def execute_jumps_v2(pointers: list) -> int:
    ptr, steps = 0, 0
    max_ptr = len(pointers)
    while ptr < max_ptr:
        next_move = pointers[ptr]
        if next_move >= 3:
            pointers[ptr] -= 1
        else:
            pointers[ptr] += 1
        ptr += next_move
        steps += 1

    return steps


def puzzles():
    pointers = [int(line) for line in open("input/day5.txt").readlines()]
    print("steps:", execute_jumps(pointers))
    pointers = [int(line) for line in open("input/day5.txt").readlines()]
    print("steps:", execute_jumps_v2(pointers))


if __name__ == "__main__":
    puzzles()
