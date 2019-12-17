def redistribute(blocks: list) -> list:
    num_blocks = len(blocks)
    blocks_to_distribute = max(blocks)
    index = blocks.index(blocks_to_distribute)

    blocks[index] = 0
    while blocks_to_distribute > 0:
        index = (index + 1) % num_blocks
        blocks[index] += 1
        blocks_to_distribute -= 1

    return blocks


def get_states(blocks: list) -> (list, int):
    states = [blocks.copy()]

    while True:
        blocks = redistribute(blocks)
        if blocks in states:
            break
        states.append(blocks.copy())

    return blocks, len(states)


def puzzles():
    blocks = [int(block) for block in open("input/day6.txt").readline().split('\t')]

    blocks_after, num_states = get_states(blocks)
    print("number of states:", num_states)
    blocks_after, num_states = get_states(blocks_after)
    print("number of states:", num_states)


if __name__ == "__main__":
    puzzles()
