import hashlib


def hash_starts_with(number, start_with="00000", secret_key="ckczppom"):
    string_to_hash = secret_key + str(number)
    hash_object = hashlib.md5(str(string_to_hash).encode("utf-8"))
    hex_hash = hash_object.hexdigest()
    return hex_hash.startswith(start_with)


def puzzle1():
    number = 0
    while not hash_starts_with(number):
        number += 1
    print("lowest number 00000: ", number)


def puzzle2():
    number = 0
    while not hash_starts_with(number, start_with="000000"):
        number += 1
    print("lowest number 000000: ", number)


if __name__ == "__main__":
    puzzle1()
    puzzle2()
