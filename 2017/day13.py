import progressbar


def parse_input(filename: str) -> dict:
    lines = [line.strip() for line in open(filename).readlines()]
    depths = {}
    for line in lines:
        layer, depth = line.split(': ')
        depths[int(layer)] = int(depth)
    return depths


def play(depths: dict) -> int:
    current = {}
    directions = {}
    for depth in depths:
        current[depth] = 0
        directions[depth] = 1

    caught = []
    max_layer = max(depths)

    for pico_second in range(max_layer + 1):
        if pico_second in current and current[pico_second] == 0:
            caught.append(pico_second)

        for depth in current:
            if current[depth] == depths[depth] - 1 or (current[depth] == 0 and pico_second != 0):
                directions[depth] = -directions[depth]
            current[depth] += directions[depth]

    return sum([c * depths[c] for c in caught])


def play_simplified(depths: dict) -> int:
    rounds = {}
    for depth in depths:
        rounds[depth] = (depths[depth] - 1) * 2

    caught = [depth for depth in rounds if depth % rounds[depth] == 0]
    return sum([c * depths[c] for c in caught])


def part1(depths: dict) -> int:
    # return play(depths)
    return play_simplified(depths)


def play_with_delay(rounds: dict, delay: int) -> bool:
    for depth in rounds:
        if (depth + delay) % rounds[depth] == 0:
            return True
    return False


def part2(depths: dict) -> int:
    rounds = {}
    for depth in depths:
        rounds[depth] = (depths[depth] - 1) * 2

    with progressbar.ProgressBar() as p:
        delay = 0
        while play_with_delay(rounds, delay):
            delay += 1
            p.update(delay)
    return delay


def main():
    depths = parse_input('2017/input/day13.txt')
    print(f'Part 1: {part1(depths)}')
    print(f'Part 2: {part2(depths)}')


if __name__ == "__main__":
    main()
