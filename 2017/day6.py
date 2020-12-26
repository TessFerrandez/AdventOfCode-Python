from typing import List, Tuple


def parse_input(filename: str) -> List[int]:
    return [int(d) for d in open(filename).read().strip().split('\t')]


def redistribute_blocks(memory_banks: List[int]) -> List[Tuple]:
    num_banks = len(memory_banks)
    seen = []

    while tuple(memory_banks) not in seen:
        seen.append(tuple(memory_banks))
        max_size = max(memory_banks)
        max_index = memory_banks.index(max_size)
        memory_banks[max_index] = 0
        for i in range(max_size):
            next_index = (max_index + i + 1) % num_banks
            memory_banks[next_index] += 1
    seen.append(tuple(memory_banks))
    return seen


def part1(seen: List[Tuple]) -> int:
    return len(seen) - 1


def part2(seen: List[Tuple]) -> int:
    last_seen = len(seen) - 1
    first_seen = seen.index(seen[-1])
    return last_seen - first_seen


def main():
    memory_banks = parse_input('input/day6.txt')
    # memory_banks = [0, 2, 7, 0]
    seen = redistribute_blocks(memory_banks)
    print(f'Part 1: {part1(seen)}')
    print(f'Part 2: {part2(seen)}')


if __name__ == "__main__":
    main()
