import hashlib


def get_code(number, room_id="wtnhxymk"):
    string_to_hash = room_id + str(number)
    hash_object = hashlib.md5(str(string_to_hash).encode("utf-8"))
    hex_hash = hash_object.hexdigest()
    if hex_hash.startswith("00000"):
        print(".")
        return hex_hash[5]
    return ""


def get_code_and_pos(number, room_id="wtnhxymk"):
    string_to_hash = room_id + str(number)
    hash_object = hashlib.md5(str(string_to_hash).encode("utf-8"))
    hex_hash = hash_object.hexdigest()
    if hex_hash.startswith("00000"):
        return hex_hash[5], hex_hash[6]
    return "", ""


def puzzle1():
    print("puzzle1")
    code = ""
    num = 0
    while len(code) < 8:
        code += get_code(num)
        num += 1
    print(code)


def puzzle2():
    print("puzzle2")
    code = ["_", "_", "_", "_", "_", "_", "_", "_"]
    num = 0
    found = 0
    while found < 8:
        index, code_char = get_code_and_pos(num)
        if index != "":
            if index.isdigit():
                index = int(index)
                if index < 8 and code[index] == "_":
                    code[index] = code_char
                    print("".join([c for c in code]))
                    found += 1
        num += 1


if __name__ == "__main__":
    puzzle1()
    puzzle2()
