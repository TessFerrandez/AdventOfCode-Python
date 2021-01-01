from collections import deque, defaultdict


def part1(num_players: int, last_marble: int) -> int:
    players = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            players[marble % num_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)
    return max(players.values())


def main():
    print(f'Part 1: {part1(423, 71944)}')
    print(f'Part 2: {part1(423, 71944 * 100)}')


if __name__ == "__main__":
    main()
