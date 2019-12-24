from itertools import count
from math import sqrt
from progressbar import ProgressBar


def get_factors(n: int) -> set:
    factors = set()
    for i in range(1, int(sqrt(n)) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            factors.add(i)
            factors.add(div)
    return factors


def get_gifts(number: int, gifts_per_number=10, limit=None) -> int:
    if limit is None:
        n_visits = sum(i for i in get_factors(number))
    else:
        n_visits = sum(i for i in get_factors(number) if number <= i * limit)
    return n_visits * gifts_per_number


def get_house(target: int, gifts_per_number=10, limit=None) -> int:
    pbar = ProgressBar(maxval=1000000)
    pbar.start()

    for i in count(1):
        if i % 100000 == 0:
            pbar.update(i)
        if get_gifts(i, gifts_per_number, limit) >= target:
            return i

    pbar.finish()


def puzzles():
    print("house:", get_house(33100000))
    print("house:", get_house(33100000, 11, 50))


if __name__ == "__main__":
    puzzles()
