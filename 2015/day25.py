def get_order(col: int, row: int) -> int:
    order = 0
    for i in range(col + 1):
        order += i
    for i in range(col, col + row - 1):
        order += i
    return order


def part1(col: int, row: int) -> int:
    start = 20151125
    times = 252533
    divisor = 33554393

    order = get_order(col, row)
    code = start
    for i in range(order - 1):
        code = (code * times) % divisor
    return code


def main():
    print(f'Part 1: {part1(3019, 3010)}')


if __name__ == "__main__":
    main()
