from progressbar import ProgressBar


def part1(puzzle_input: int) -> str:
    recipes = [3, 7]
    elf1, elf2 = 0, 1

    while len(recipes) < (puzzle_input + 10):
        recipe_sum = recipes[elf1] + recipes[elf2]
        tens = recipe_sum // 10
        ones = recipe_sum % 10
        if tens > 0:
            recipes.append(tens)
        recipes.append(ones)
        elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
        elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)
    return ''.join([str(d) for d in recipes[puzzle_input: puzzle_input + 10]])


def part2(puzzle_input: str) -> int:
    puzzle_input_len = len(puzzle_input)

    recipes = [3, 7]
    elf1, elf2 = 0, 1

    i = 0
    with ProgressBar() as p:
        while puzzle_input not in ''.join(str(d) for d in recipes[-(puzzle_input_len + 1):]):
            recipe_sum = recipes[elf1] + recipes[elf2]
            tens = recipe_sum // 10
            ones = recipe_sum % 10
            if tens > 0:
                recipes.append(tens)
            recipes.append(ones)
            elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
            elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)
            i += 1
            p.update(i)
    if ''.join(str(d) for d in recipes[-puzzle_input_len:]) == puzzle_input:
        return len(recipes) - puzzle_input_len
    else:
        return len(recipes) - puzzle_input_len - 1


def main():
    puzzle_input = 320851
    print(f'Part 1: {part1(puzzle_input)}')
    puzzle_input = '320851'
    print(f'Part 2: {part2(puzzle_input)}')


if __name__ == "__main__":
    main()
