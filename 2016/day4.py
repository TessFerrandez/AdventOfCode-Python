import pytest
from collections import Counter
from typing import List, Tuple


@pytest.mark.parametrize('room_name, checksum, expected',
                         [
                             ('aaaaa-bbb-z-y-x', 'abxyz', True),
                             ('a-b-c-d-e-f-g-h', 'abcde', True),
                             ('not-a-real-room', 'oarel', True),
                             ('totally-real-room', 'decoy', False)
                         ])
def test_is_real_room(room_name: str, checksum: str, expected: int):
    assert is_real_room(room_name, checksum) == expected


@pytest.mark.parametrize('room_name, room_id, expected',
                         [
                             ('qzmt-zixmtkozy-ivhz', 343, 'very encrypted name'),
                         ])
def test_decode(room_name: str, room_id: int, expected: str):
    assert decode(room_name, room_id) == expected


def parse_input(filename: str) -> List[Tuple[int, str, str]]:
    rooms = []
    lines = [line.strip() for line in open(filename).readlines()]
    for line in lines:
        room, checksum = line[:-1].split('[')
        *room_name_parts, room_id = room.split('-')
        room_name = '-'.join(room_name_parts)
        room_id = int(room_id)
        rooms.append((room_id, room_name, checksum))
    return rooms


def decode(room_name: str, room_id: int) -> str:
    decoded = ''
    for ch in room_name:
        if ch == '-':
            decoded += ' '
        else:
            val = ord(ch) - ord('a')
            val = (val + room_id) % 26 + ord('a')
            decoded += chr(val)
    return decoded


def is_real_room(room_name: str, checksum: str) -> bool:
    counts = Counter(room_name)
    counts['-'] = 0
    letters = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    room_checksum = ''
    for i in range(5):
        room_checksum += letters[i][0]

    return room_checksum == checksum


def part1(rooms: List[Tuple[int, str, str]]) -> int:
    total = 0
    for room in rooms:
        room_id, room_name, checksum = room
        if is_real_room(room_name, checksum):
            total += room_id
    return total


def part2(rooms: List[Tuple[int, str, str]]) -> int:
    for room in rooms:
        room_id, room_name, _ = room
        decoded_room_name = decode(room_name, room_id)
        if 'north' in decoded_room_name:
            print(room_id, decoded_room_name)
            return room_id
    return 0


def main():
    rooms = parse_input('input/day4.txt')
    print(f'Part 1: {part1(rooms)}')
    print(f'Part 2: {part2(rooms)}')


if __name__ == "__main__":
    main()
