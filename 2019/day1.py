"""
Calculate the fuel needed for the santa rocket
"""


def calculate_fuel(mass):
    return int(mass) // 3 - 2


def calculate_fuel_v2(mass):
    fuel = calculate_fuel(mass)
    if fuel <= 0:
        return 0
    fuel += calculate_fuel_v2(fuel)
    return fuel


def puzzle1():
    total_fuel = sum(calculate_fuel(mass) for mass in open('input/day1.txt'))
    print("total fuel (v1): ", total_fuel)


def puzzle2():
    total_fuel = sum(calculate_fuel_v2(mass)
                     for mass in open('input/day1.txt'))
    print("total fuel (v2): ", total_fuel)


if __name__ == "__main__":
    puzzle1()
    puzzle2()
