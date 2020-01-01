def generate(previous: int, fact: int) -> int:
    return previous * fact % 2147483647


def is_pair(number1: int, number2: int) -> bool:
    binary1 = format(number1, "0>32b")
    binary2 = format(number2, "0>32b")
    return binary1[-16:] == binary2[-16:]


def puzzle1():
    prevA, prevB = 703, 516
    num_pairs = 0
    for i in range(40000000):
        if i % 4000000 == 0:
            print(".", end="")
        prevA = generate(prevA, 16807)
        prevB = generate(prevB, 48271)
        if is_pair(prevA, prevB):
            num_pairs += 1
    print("pairs:", num_pairs)


def puzzle2():
    prevA, prevB = 703, 516
    # prevA, prevB = 65, 8921
    num_pairs = 0
    i = 0
    while i < 5000000:
        if i % 1000000 == 0:
            print(i)
        while True:
            prevA = generate(prevA, 16807)
            if prevA % 4 == 0:
                break
        while True:
            prevB = generate(prevB, 48271)
            if prevB % 8 == 0:
                break
        i += 1
        if is_pair(prevA, prevB):
            num_pairs += 1
    print("pairs:", num_pairs)


if __name__ == "__main__":
    puzzle1()
    puzzle2()
