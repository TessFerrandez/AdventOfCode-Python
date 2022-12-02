from sys import argv
from aocd.models import Puzzle


if __name__ == "__main__":
    if len(argv) < 3:
        print('Usage: download-input year day')
        exit

    year = int(argv[1])
    day = int(argv[2])

    path = f"{year}\\input\\day{day}.in"

    print(f"Downloading puzzle data for: {year}, {day} to {path}")
    puzzle = Puzzle(year=year, day=day)
    f = open(path, "w")
    f.write(puzzle.input_data)
    f.close()
