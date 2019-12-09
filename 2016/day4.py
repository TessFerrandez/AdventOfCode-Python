import re, collections, string


def parse(input_line):
    input_line = input_line.strip()
    checksum = input_line.split('[')[1][:-1]
    code = input_line.split('[')[0]
    room_id = int(code.split('-')[-1])
    room_code = code[0:-3]
    return room_code, checksum, room_id


def validate(room_code, checksum):
    room_code = room_code.replace('-', '')
    uniq = set(room_code)
    frequencies = []
    for letter in uniq:
        frequencies.append((letter, room_code.count(letter)))
    frequencies = sorted(frequencies, key=lambda tup: (-tup[1], tup[0]))

    my_checksum = ''
    for i in range(0, 5):
        my_checksum += frequencies[i][0]

    return my_checksum == checksum


def puzzle1():
    sum_ids = 0

    with open('input/day4.txt') as f:
        for line in f:
            room_code, checksum, room_id = parse(line)
            if validate(room_code, checksum):
                sum_ids += room_id

    print("sum of IDs", sum_ids)


def decrypt(encrypted, room_id):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shift = room_id % 26 + -10
    cipher = alphabet[-shift:] + alphabet[:-shift]

    decrypted = ''
    for letter in encrypted:
        if letter == '-':
            decrypted += ' '
        else:
            decrypted += cipher[alphabet.index(letter)]

    return decrypted


def caesar_cipher(n):
    az = string.ascii_lowercase
    x = n % len(az)
    return str.maketrans(az, az[x:] + az[:x])


def puzzle2():
    ans1 = 0
    regex = r'([a-z-]+)(\d+)\[(\w+)\]'
    with open('input/day4.txt') as fp:
        for code, sid, checksum in re.findall(regex, fp.read()):
            sid = int(sid)
            letters = ''.join(c for c in code if c in string.ascii_lowercase)
            tops = [(-n, c) for c, n in collections.Counter(letters).most_common()]
            ranked = ''.join(c for n, c in sorted(tops))
            if ranked.startswith(checksum):
                ans1 += sid
                decoded = code.translate(caesar_cipher(sid))
                if 'north' in decoded:
                    print("decoded room:", decoded.replace('-', ' ').strip(), sid)


if __name__ == "__main__":
    puzzle1()
    puzzle2()
