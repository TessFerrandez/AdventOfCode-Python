def get_score(spoons: list, restrict_calories=False) -> int:
    properties = [
        [4, -2, 0, 0, 5],
        [0, 5, -1, 0, 8],
        [-1, 0, 5, 0, 6],
        [0, 0, -2, 2, 1],
    ]

    n_items = len(spoons)

    if restrict_calories:
        calorie_count = 0
        for ingredient in range(n_items):
            calorie_count += spoons[ingredient] * properties[ingredient][4]

        if calorie_count != 500:
            return 0

    total_score = 1
    for prop in range(4):
        score = 0
        for ingredient in range(n_items):
            score += spoons[ingredient] * properties[ingredient][prop]
        score = max(score, 0)
        total_score *= score
    return total_score


def find_best_combo(spoons: int, restrict_calories=False):
    max_score = 0
    for frosting in range(1, spoons - 2):
        for candy in range(1, spoons - frosting - 1):
            for butter in range(1, spoons - frosting - candy):
                sugar = spoons - frosting - candy - butter
                max_score = max(
                    max_score,
                    get_score([frosting, candy, butter, sugar], restrict_calories),
                )

    return max_score


def puzzles():
    max_score = find_best_combo(100, restrict_calories=False)
    print("max score", max_score)
    max_score = find_best_combo(100, restrict_calories=True)
    print("max score", max_score)


if __name__ == "__main__":
    puzzles()
