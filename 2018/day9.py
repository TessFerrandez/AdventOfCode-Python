from collections import deque, defaultdict


def play(players: int, last: int) -> int:
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)
    return max(scores.values())


if __name__ == "__main__":
    print("score:", play(423, 71944))
    print("score:", play(423, 71944 * 100))
