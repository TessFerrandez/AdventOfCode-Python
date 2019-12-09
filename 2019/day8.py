import numpy as np
from collections import Counter
import matplotlib.pyplot as plt


def checksum(encoded_image, width, height):
    img = np.array(list(encoded_image))
    img = np.reshape(img, (-1, width * height))

    best_layer = -1
    min_zero = 10000
    layer_index = 0
    for layer in img:
        num_zeros = Counter(layer)['0']
        if num_zeros < min_zero:
            min_zero = num_zeros
            best_layer = layer_index
        layer_index += 1

    counters = Counter(img[best_layer])
    return counters['1'] * counters['2']


def decode(encoded_image, width, height):
    img = np.array(list(encoded_image))
    img = np.reshape(img, (-1, height, width))

    new_img = np.full((height, width), 2)
    for layer in img:
        for x in range(0, width):
            for y in range(0, height):
                if new_img[y][x] == 2:
                    if layer[y][x] == '0':
                        new_img[y][x] = 1
                    elif layer[y][x] == '1':
                        new_img[y][x] = 0
    plt.imshow(new_img)
    plt.show()


def puzzle1():
    print("checksum:", checksum(open('input/day8.txt').read(), 25, 6))


def puzzle2():
    decode(open('input/day8.txt').read(), 25, 6)


if __name__ == "__main__":
    puzzle1()
    puzzle2()
