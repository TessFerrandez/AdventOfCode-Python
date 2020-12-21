from hashlib import md5
from typing import List, Set
from collections import defaultdict


def find_5_match(s: str) -> str:
    for i in range(len(s) - 4):
        if s[i] == s[i + 1] == s[i + 2] == s[i + 3] == s[i + 4]:
            return s[i]
    return None


def find_3_match(s: str) -> str:
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] == s[i + 2]:
            return s[i]
    return None


def get_64th_key(salt: str, stretch: int = 0) -> int:
    keys = []
    i = 0
    threes = defaultdict(list)

    while not (len(keys) > 64 and (i - keys[-1][0]) > 1000):
        key_hash = md5(('%s%s' % (salt, i)).encode('utf-8')).hexdigest()

        for _ in range(stretch):
            key_hash = md5(key_hash.encode('utf-8')).hexdigest()

        match = find_5_match(key_hash)
        if match:
            for idx, value in threes[match]:
                if (i - idx) <= 1000:
                    keys.append((idx, key_hash))
            keys.sort()
            threes[match] = []

        match = find_3_match(key_hash)
        if match:
            threes[match].append((i, key_hash))

        i += 1

    return keys[63][0]


def part1(salt: str) -> int:
    return get_64th_key(salt)


def part2(salt: str, stretch: int = 2016) -> int:
    return get_64th_key(salt, stretch)


def main():
    input_string = 'ahsbgdzn'
    print(f'Part 1: {part1(input_string)}')
    print(f'Part 2: {part2(input_string)}')


if __name__ == "__main__":
    main()
