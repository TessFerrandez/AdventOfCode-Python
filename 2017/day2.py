def quote_of(numbers):
    num_numbers = len(numbers)
    for i in range(num_numbers - 1):
        for j in range(i + 1, num_numbers):
            if numbers[i] % numbers[j] == 0:
                quote = int(numbers[i] / numbers[j])
                return quote
    return 0


def puzzles():
    lines = [
        sorted([int(x) for x in line.split("\t")], reverse=True)
        for line in open("input/day2.txt").readlines()
    ]
    min_max_sum = sum(max(numbers) - min(numbers) for numbers in lines)
    quote_sum = sum(quote_of(numbers) for numbers in lines)
    print("sum of max-min:", min_max_sum)
    print("sum of divisions:", quote_sum)


if __name__ == "__main__":
    puzzles()
