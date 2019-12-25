def get_order(col: int, row: int) -> int:
    order = 0
    for i in range(col + 1):
        order += i
    for i in range(col, col + row - 1):
        order += i

    return order


def calculate_code(order: int) -> int:
    start = 20151125
    times = 252533
    divisor = 33554393

    code = start
    for i in range(order - 1):
        code = (code * times) % divisor
    return code


def puzzles():
    order = get_order(3019, 3010)
    print("code:", calculate_code(order))


if __name__ == "__main__":
    puzzles()
