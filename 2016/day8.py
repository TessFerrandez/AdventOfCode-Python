import re
import numpy as np
import matplotlib.pyplot as plt


def display(screen):
    print("\n".join("".join("X" if p else " " for p in row) for row in screen))


def count_lit(screen):
    return sum(sum(screen))


def run(width, height, lines):
    screen = np.zeros((height, width), dtype=bool)
    for line in lines:
        p = re.split(r"[ =]", line)
        if p[0] == "rect":
            w, h = map(int, p[1].split("x"))
            screen[:h, :w] = True
        elif p[0] == "rotate":
            if p[1] == "row":
                cy, n = int(p[3]), int(p[5])
                screen[cy] = np.roll(screen[cy], n)
            else:
                cx, n = int(p[3]), int(p[5])
                screen[:, cx] = np.roll(screen[:, cx], n)
    return screen


def puzzle1():
    resulting_screen = run(50, 6, open("input/day8.txt"))
    plt.imshow(resulting_screen)
    plt.show()
    print("number lit:", count_lit(resulting_screen))


if __name__ == "__main__":
    puzzle1()
