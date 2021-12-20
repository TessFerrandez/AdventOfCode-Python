from collections import defaultdict
from typing import Tuple, DefaultDict
from tqdm import tqdm


def read_input() -> Tuple[str, DefaultDict, int, int]:
    algorithm, raw_image = open('2021/input/day20.txt').read().split("\n\n")
    image_lines = raw_image.splitlines()

    image = defaultdict(lambda: "0")

    for row, line in enumerate(image_lines):
        for col, c in enumerate(line):
            if c == "#":
                image[(col, row)] = "1"

    return algorithm, image, len(image_lines[0]), len(image_lines)


def enhance_image(image, algorithm, minx, maxx, miny, maxy):
    new_image = defaultdict(lambda: "0")

    for y in range(miny + 1, maxy):
        for x in range(minx + 1, maxx):
            binary = "".join(image[(dx, dy)] for dy in range(y - 1, y + 2) for dx in range(x - 1, x + 2))
            if algorithm[int(binary, 2)] == "#":
                new_image[(x, y)] = "1"

    return new_image


def flip_outer_rim(image, minx, maxx, miny, maxy, n):
    value = "0" if n % 2 else "1"
    for y in range(miny, maxy + 1):
        image[(minx, y)] = value
        image[(maxx, y)] = value
    for x in range(minx, maxx + 1):
        image[(x, miny)] = value
        image[(x, maxy)] = value
    return image


def run_enhancements(image, width, height, algorithm, steps) -> Tuple[DefaultDict, int]:
    padding = 2 * steps

    # pad the image (with all 0s) - enough layers to cover all the steps
    minx, miny = 0 - padding, 0 - padding
    maxx, maxy = width + padding, height + padding

    for step in tqdm(range(steps)):
        image = enhance_image(image, algorithm, minx, maxx, miny, maxy)
        # flip the outer rim - to account for what is outside the image
        image = flip_outer_rim(image, minx, maxx, miny, maxy, step)

    return image, sum(1 for c in image.values() if c == "1")


algorithm, image, width, height = read_input()
image, num_lit = run_enhancements(image, width, height, algorithm, 2)
print("Part 1:", num_lit)

algorithm, image, width, height = read_input()
image, num_lit = run_enhancements(image, width, height, algorithm, 50)
print("Part 2:", num_lit)
