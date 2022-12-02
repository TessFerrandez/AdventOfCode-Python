from collections import Counter
from typing import List
import numpy as np
import matplotlib.pyplot as plt


def get_layers(raw_image, pixels) -> List[str]:
    num_layers = len(raw_image) // pixels
    return [raw_image[layer * pixels: (layer + 1) * pixels] for layer in range(num_layers)]


def validate_image(raw_image, pixels) -> int:
    layers = get_layers(raw_image, pixels)

    best_0, best_1, best_2 = pixels + 1, 0, 0
    for layer in layers:
        counts = Counter(layer)
        if counts['0'] < best_0:
            best_0 = counts['0']
            best_1 = counts['1']
            best_2 = counts['2']

    return best_1 * best_2


def decode_image(raw_image, pixels) -> str:
    layers = get_layers(raw_image, pixels)
    final = ['2' for _ in range(pixels)]
    for layer in layers:
        for pixel in range(pixels):
            if final[pixel] == '2':
                final[pixel] = layer[pixel]
    return ''.join(final)


def print_image(image_str, width, height):
    image = np.zeros((height, width))
    for y in range(height):
        for x in range(width):
            image[y, x] = image_str[y * width + x]
    plt.imshow(image)
    plt.show()


def tests():
    assert validate_image('123456789012', 3 * 2) == 1
    assert decode_image('0222112222120000', 4) == "0110"


tests()


raw_image = open('2019/input/day8.txt').read().strip()
print("Part 1:", validate_image(raw_image, 25 * 6))
print("Part 2:")
print_image(decode_image(raw_image, 25 * 6), 25, 6)
