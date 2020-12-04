from typing import List
import string


def parse_input() -> List[dict]:
    with open("input/day4.txt") as f:
        passport_strings = f.read().split("\n\n")
    passports = []
    for passport_string in passport_strings:
        parts = [part.strip() for part in passport_string.split()]
        passport = {}
        for part in parts:
            prop, value = part.split(":")
            passport[prop] = value
        passports.append(passport)
    return passports


checks = {
    "byr": lambda value: 1920 <= int(value) <= 2002,
    "iyr": lambda value: 2010 <= int(value) <= 2020,
    "eyr": lambda value: 2020 <= int(value) <= 2030,
    "hgt": lambda value: ("cm" in value and 150 <= int(value[:-2]) <= 193)
    or ("in" in value and 59 <= int(value[:-2]) <= 76),
    "hcl": lambda value: len(value) == 7
    and value[0] == "#"
    and all(c in string.hexdigits for c in value[1:]),
    "ecl": lambda value: value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda value: len(value) == 9 and int(value),
    "cid": lambda value: True,
}


def has_required_fields(passport: dict) -> bool:
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for password_property in required:
        if password_property not in passport:
            return False
    return True


def fields_are_valid(passport: dict) -> bool:
    for prop in passport:
        if not checks[prop](passport[prop]):
            return False
    return True


def puzzle1(passports: List[dict]) -> int:
    return sum(1 if has_required_fields(passport) else 0 for passport in passports)


def puzzle2(passports: List[dict]) -> int:
    num_valid = 0
    for passport in passports:
        if has_required_fields(passport) and fields_are_valid(passport):
            num_valid += 1
    return num_valid


def main():
    passports = parse_input()
    puzzle1_result = puzzle1(passports)
    print(f"Puzzle 1: {puzzle1_result}")
    puzzle2_result = puzzle2(passports)
    print(f"Puzzle 2: {puzzle2_result}")


if __name__ == "__main__":
    main()
