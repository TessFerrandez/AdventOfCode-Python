import progressbar


def part1(a: int, b: int) -> int:
    factor_a, factor_b = 16807, 48271
    div_by = 2147483647

    num_pairs = 0
    with progressbar.ProgressBar(max_value=40000000) as p:
        for i in range(40000000):
            p.update(i)
            a = (a * factor_a) % div_by
            b = (b * factor_b) % div_by
            if bin(a)[-16:] == bin(b)[-16:]:
                num_pairs += 1
    return num_pairs


def part2(a: int, b: int) -> int:
    factor_a, factor_b = 16807, 48271
    div_by = 2147483647

    num_pairs = 0
    with progressbar.ProgressBar(max_value=5000000) as p:
        for i in range(5000000):
            p.update(i)
            while True:
                a = (a * factor_a) % div_by
                if a % 4 == 0:
                    break
            while True:
                b = (b * factor_b) % div_by
                if b % 8 == 0:
                    break
            if bin(a)[-16:] == bin(b)[-16:]:
                num_pairs += 1
    return num_pairs


def main():
    a, b = 703, 516
    # a, b = 65, 8921
    print(f'Part 1: {part1(a, b)}')
    print(f'Part 2: {part2(a, b)}')


if __name__ == "__main__":
    main()
