from functools import cache


def advance(position, score, roll_sum):
    new_position = ((position - 1 + roll_sum) % 10) + 1
    return new_position, score + new_position


# Part 1
def play_practice_game(positions) -> int:
    player = 0
    scores = [0, 0]
    num_rolls = 0
    roll = 0

    while max(scores) <= 1000:
        rolls = [roll := (roll % 100) + 1 for _ in range(3)]
        positions[player], scores[player] = advance(positions[player], scores[player], sum(rolls))
        player = 1 - player
        num_rolls += 3

    # to appease flake 8
    _ = roll

    if scores[0] >= 1000:
        return scores[1] * num_rolls
    else:
        return scores[0] * num_rolls


# Part 2
throw_frequencies = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


@cache
def get_wins(pos1, pos2, score1, score2, player=1):
    if score1 >= 21:
        return [1, 0]

    if score2 >= 21:
        return [0, 1]

    wins = [0, 0]
    for dice_sum, frequency in throw_frequencies.items():
        if player == 1:
            pos, score = advance(pos1, score1, dice_sum)
            wins1, wins2 = get_wins(pos, pos2, score, score2, 2)
        else:
            pos, score = advance(pos2, score2, dice_sum)
            wins1, wins2 = get_wins(pos1, pos, score1, score, 1)

        wins[0] += wins1 * frequency
        wins[1] += wins2 * frequency

    return wins


positions = [6, 8]
print("Part 1:", play_practice_game([6, 8]))
print("Part 2:", max(get_wins(6, 8, 0, 0)))
