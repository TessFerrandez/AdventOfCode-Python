def get_fuel(mass):
    return int(mass / 3) - 2


def get_fuel_ex(mass):
    fuel = get_fuel(mass)
    extra_fuel = get_fuel(fuel)

    while extra_fuel > 0:
        fuel += extra_fuel
        extra_fuel = get_fuel(extra_fuel)

    return fuel


def tests():
    assert get_fuel(12) == 2
    assert get_fuel(14) == 2
    assert get_fuel(1969) == 654
    assert get_fuel(100756) == 33583
    assert get_fuel_ex(14) == 2
    assert get_fuel_ex(1969) == 966
    assert get_fuel_ex(100756) == 50346


tests()

# ----
masses = [int(mass) for mass in open('2019/input/day1.txt')]

fuels = sum(get_fuel(mass) for mass in masses)
print("Part 1:", fuels)

fuels = sum(get_fuel_ex(mass) for mass in masses)
print("Part 2:", fuels)
