import pytest
import hashlib
import progressbar


@pytest.mark.parametrize('data, expected',
                         [
                             ('abc', '18f47a30'),
                         ])
def test_part1(data: str, expected: int):
    assert part1(data) == expected


@pytest.mark.parametrize('data, expected',
                         [
                             ('abc', '05ace8e3'),
                         ])
def test_part2(data: str, expected: int):
    assert part2(data) == expected


def get_code(number: int, room_id: str) -> str:
    string_to_hash = room_id + str(number)
    hash_object = hashlib.md5(str(string_to_hash).encode('utf-8'))
    hex_hash = hash_object.hexdigest()
    if hex_hash.startswith('00000'):
        return hex_hash[5]
    return ''


def part1(room_id: str) -> str:
    code = ''
    number = 0

    with progressbar.ProgressBar() as p:
        while len(code) < 8:
            code += get_code(number, room_id)
            number += 1
            p.update(number)
    return code


def get_code_and_position(number: int, room_id: str) -> (str, str):
    string_to_hash = room_id + str(number)
    hash_object = hashlib.md5(str(string_to_hash).encode("utf-8"))
    hex_hash = hash_object.hexdigest()
    if hex_hash.startswith("00000"):
        return hex_hash[5], hex_hash[6]
    return '', ''


def part2(room_id: str) -> str:
    code = ['_', '_', '_', '_', '_', '_', '_', '_']
    number = 0
    found = 0

    with progressbar.ProgressBar() as p:
        while found < 8:
            index, char = get_code_and_position(number, room_id)
            if index != '' and index.isdigit():
                index = int(index)
                if index < 8 and code[index] == '_':
                    code[index] = char
                    print(''.join(code))
                    found += 1
            number += 1
            p.update(number)
    return ''.join(code)


def main():
    puzzle_input = 'wtnhxymk'
    print(f'Part 1: {part1(puzzle_input)}')
    print(f'Part 2: {part2(puzzle_input)}')


if __name__ == "__main__":
    main()
