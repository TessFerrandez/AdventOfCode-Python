import numpy as np
import matplotlib.pyplot as plt


def parse_input(filename: str) -> str:
    return open(filename).read().strip()


def part1(data: str) -> int:
    num_layers = len(data) // 150

    fewest_zeros = float('inf')
    best_layer = ''

    for i in range(num_layers):
        layer = data[i * 150: (i + 1) * 150]
        num_zeros = layer.count('0')
        if num_zeros < fewest_zeros:
            fewest_zeros = num_zeros
            best_layer = layer

    return best_layer.count('1') * best_layer.count('2')


def part2(data: str) -> int:
    num_layers = len(data) // 150
    layers = [data[i * 150: (i + 1) * 150] for i in range(num_layers)]

    image = np.zeros((6, 25))

    pixel = -1
    for y in range(6):
        for x in range(25):
            pixel += 1
            for layer in layers:
                if layer[pixel] == '0':
                    break
                if layer[pixel] == '1':
                    image[y][x] = 255
                    break

    plt.imshow(image)
    plt.show()
    return 0


def main():
    data = parse_input('input/day8.txt')
    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')


if __name__ == "__main__":
    main()
