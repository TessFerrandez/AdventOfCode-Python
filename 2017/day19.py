from typing import List


def parse_input(filename: str) -> List[str]:
    original_lines = [line.replace('\n', '') for line in open(filename).readlines()]
    max_len = max(len(line) for line in original_lines)
    lines = [' ' + line + ' ' * (max_len + 1 - len(line)) for line in original_lines]
    lines.append(' ' * (max_len + 2))
    return lines


def part1(lines: List[str]) -> (str, int):
    pos = lines[0].index('|')
    direction = 1j

    path = ''
    steps = 0
    while True:
        pos += direction
        steps += 1
        x, y = int(pos.real), int(pos.imag)
        ch = lines[y][x]
        if ch == '+':
            if direction == 1 or direction == -1:
                direction = 1j if lines[y - 1][x] == ' ' else -1j
            elif direction == 1j or direction == -1j:
                direction = 1 if lines[y][x - 1] == ' ' else -1
        elif ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            path += ch
        elif ch == ' ':
            break
    return path, steps


def main():
    data = parse_input('input/day19.txt')
    path, steps = part1(data)
    print(f'Part 1: {path}')
    print(f'Part 2: {steps}')


if __name__ == "__main__":
    main()
