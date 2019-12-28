from hashlib import md5
from collections import defaultdict


def matches_3(hash_string):
    for i in range(len(hash_string) - 2):
        if hash_string[i] == hash_string[i + 1] == hash_string[i + 2]:
            return hash_string[i]
    return None


def matches_5(hash_string):
    for i in range(len(hash_string) - 4):
        if (
            hash_string[i]
            == hash_string[i + 1]
            == hash_string[i + 2]
            == hash_string[i + 3]
            == hash_string[i + 4]
        ):
            return hash_string[i]
    return None


def get_64th_hash(salt="ahsbgdzn", stretch=2016):
    i = 0
    keys = []
    threes = defaultdict(list)

    while not (len(keys) > 64 and (i - keys[-1][0]) > 1000):
        key_hash = md5(("%s%s" % (salt, i)).encode("utf-8")).hexdigest()
        for _ in range(stretch):
            key_hash = md5(key_hash.encode("utf-8")).hexdigest()

        match = matches_5(key_hash)

        if match is not None:
            for (m_idx, value) in threes[match]:
                if (i - m_idx) <= 1000:
                    keys.append((m_idx, key_hash))
                    # print("Found: ", m_idx)
            keys.sort()
            threes[match] = []

        match = matches_3(key_hash)
        if match is not None:
            threes[match].append((i, key_hash))

        i += 1

    print("Last hash", keys[63])


def puzzles():
    salt = "ahsbgdzn"
    get_64th_hash(salt, 0)
    get_64th_hash(salt, 2016)


if __name__ == "__main__":
    puzzles()
