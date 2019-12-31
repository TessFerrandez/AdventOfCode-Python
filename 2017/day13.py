def update_scanners(scanners: dict):
    for i in scanners:
        scanner = scanners[i]
        if scanner[1] == scanner[0] - 1 or scanner[1] == 0:
            # change direction
            scanner[2] = -scanner[2]
        scanner[1] += scanner[2]


def read_input() -> dict:
    scanners = dict()
    scan_lines = [line.strip().split(": ") for line in open("input/day13.txt")]
    for line in scan_lines:
        layer, depth = line
        scanners[int(layer)] = int(depth)
    return scanners


def scan(scanners: dict, delay=0) -> list:
    max_layer = max(scanners) + 1
    caught = []
    for layer in range(max_layer):
        time = layer + delay
        if layer in scanners:
            layer_range = scanners[layer]
            # the layer is 0 periodically
            # the periodicity is time % (range * 2 - 2)
            if time % (layer_range * 2 - 2) == 0:
                caught.append(layer)

    return caught


def puzzles():
    scanners = read_input()

    # Part 1
    caught = scan(scanners)
    print("severity:", sum([layer * scanners[layer] for layer in caught]))

    # part 2
    caught = [1]
    i = 0
    while caught:
        i += 1
        caught = scan(scanners, i)

    print("delay:", i)


if __name__ == "__main__":
    puzzles()
