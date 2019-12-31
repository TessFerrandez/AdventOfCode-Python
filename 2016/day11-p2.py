# from bovard
items_part_one = [4, 5, 1, 0]
items_part_two = [8, 5, 1, 0]


def get_moves(items):
    """
    Through playing around with bolts and nuts,
    I came across the optimal strategy, move things up a floor at a time

    I also discovered to move n items up 1 floor,
        it requires 2 * (n - 1) - 1 moves

    So assuming a "good" start state, it doesn't matter what is on what floor
    Just the number of things per floor
    """
    moves = 0
    while items[-1] != sum(items):
        # print moves, items
        lowest_floor = 0
        while items[lowest_floor] == 0:
            lowest_floor += 1
        moves += 2 * (items[lowest_floor] - 1) - 1
        items[lowest_floor + 1] += items[lowest_floor]
        items[lowest_floor] = 0
    return moves


print("Part One")
print(get_moves(items_part_one))
print("")
print("Part Two")
print(get_moves(items_part_two))
