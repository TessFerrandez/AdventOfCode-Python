from typing import List
from collections import defaultdict


def parse_input(filename: str) -> dict:
    chains = defaultdict(lambda: [])
    lines = [line.strip().split(' ') for line in open(filename).readlines()]
    for line in lines:
        before, after = line[1], line[7]
        chains[after].append(before)
    return chains


def update_chains(chains: dict, step: str) -> List[str]:
    available = []
    for chain in chains:
        if step in chains[chain]:
            chains[chain].remove(step)
            if not chains[chain]:
                if step not in available:
                    available.append(chain)
    return available


def part1(chains: dict, states: str) -> str:
    available = [step for step in states if not chains[step]]
    order = ''

    while available:
        available.sort()
        step = available.pop(0)
        order += step
        available += update_chains(chains, step)

    return order


def elfs_done(elfs: List) -> bool:
    for time_left, step in elfs:
        if time_left != 0:
            return False
        if step != '.':
            return False
    return True


def part2(chains: dict, states: str, num_elfs: int, delay: int) -> int:
    available = [step for step in states if not chains[step]]

    elfs = []
    for _ in range(num_elfs):
        elfs.append([0, '.'])

    seconds = 0

    while available or not elfs_done(elfs):
        seconds += 1
        for i in range(num_elfs):
            time_left, step = elfs[i]
            if time_left == 0:
                # we finished a step - release it
                if step != '.':
                    available += update_chains(chains, step)

        for i in range(num_elfs):
            time_left, step = elfs[i]
            if time_left == 0:
                # take a new step
                if available:
                    step = available.pop(0)
                    elfs[i] = [ord(step) - ord('A') + delay, step]
                else:
                    elfs[i][1] = '.'
            else:
                elfs[i][0] -= 1

    return seconds - 1


def main():
    # chains = parse_input('input/day7_test.txt')
    # states = 'ABCDEF'
    states = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chains = parse_input('input/day7.txt')
    print(f'Part 1: {part1(chains, states)}')
    chains = parse_input('input/day7.txt')
    print(f'Part 2: {part2(chains, states, 5, 60)}')


if __name__ == "__main__":
    main()
