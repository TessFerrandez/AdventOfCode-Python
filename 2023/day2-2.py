# based on solution board
from input_processing import read_data
import re


data = read_data(2023, 2)
p1, p2 = 0, 0

for game, line in enumerate(data.split("\n"), start=1):
    valid = True
    min_red = min_green = min_blue = 0

    for s in line.split(": ")[-1].split("; "):
        # sum each color per set
        red = sum(int(n) for n in re.findall(r"(\d+)\sred", s))
        green = sum(int(n) for n in re.findall(r"(\d+)\sgreen", s))
        blue = sum(int(n) for n in re.findall(r"(\d+)\sblue", s))

        # set the minimum quantity required for this set
        min_red = max(min_red, red)
        min_green = max(min_green, green)
        min_blue = max(min_blue, blue)

        # if the game breaks the 12, 13, 14 rule set it as invalid
        if red > 12 or green > 13 or blue > 14:
            valid = False

    # if the game is valid add the id to the part 1 total
    if valid:
        p1 += game

    # add product of minimum required cubes to the part 2 total
    p2 += min_red * min_green * min_blue

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
