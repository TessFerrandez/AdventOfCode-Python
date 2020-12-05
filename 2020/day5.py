import pytest
from typing import List


@pytest.mark.parametrize(
    "boarding_pass, expected_seat",
    [
        ("FBFBBFFRLR", (44, 5)),
        ("BFFFBBFRRR", (70, 7)),
        ("FFFBBBFRRR", (14, 7)),
        ("BBFFBBFRLL", (102, 4)),
    ],
)
def test_decode_boarding_pass(boarding_pass: str, expected_seat: (int, int)):
    assert decode_boarding_pass(boarding_pass) == expected_seat


def decode_boarding_pass(boarding_pass: str) -> (int, int):
    row = "".join("1" if i == "B" else "0" for i in boarding_pass[:7])
    col = "".join("1" if i == "R" else "0" for i in boarding_pass[7:])
    return int(row, 2), int(col, 2)


def get_seat_id(boarding_pass: str) -> int:
    row, col = decode_boarding_pass(boarding_pass)
    return row * 8 + col


def puzzle2(seat_ids: List[int]) -> int:
    missing_seat = 0
    prev_seat_id = seat_ids[0] - 1
    for seat_id in seat_ids:
        if seat_id != prev_seat_id + 1:
            missing_seat = seat_id - 1
            break
        prev_seat_id += 1
    return missing_seat


def main():
    boarding_passes = [line.strip() for line in open("input/day5.txt").readlines()]
    seat_ids = sorted([get_seat_id(boarding_pass) for boarding_pass in boarding_passes])
    puzzle1_result = seat_ids[-1]
    print(f"Puzzle 1: {puzzle1_result}")
    puzzle2_result = puzzle2(seat_ids)
    print(f"Puzzle 2: {puzzle2_result}")


if __name__ == "__main__":
    main()
