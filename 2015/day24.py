import itertools


def get_product(lst: list) -> int:
    product = 1
    for item in lst:
        product *= item
    return product


def puzzles():
    numbers = [int(num.strip()) for num in open("input/day24.txt").readlines()]
    # total = 1548
    # Group size = 516 (1548 / 3)
    # sample group 113, 109, 107, 103, 71, 13 (6)
    sequence_products = [get_product(seq) for seq in itertools.combinations(numbers, 6) if sum(seq) == 516]
    print("lowest quantum entanglement:", min(sequence_products))
    # Group size = 387 (1548 / 4)
    # sample group 113, 109, 107, 53, 5 (5)
    sequence_products = [get_product(seq) for seq in itertools.combinations(numbers, 5) if sum(seq) == 387]
    print("lowest quantum entanglement:", min(sequence_products))


if __name__ == "__main__":
    puzzles()
