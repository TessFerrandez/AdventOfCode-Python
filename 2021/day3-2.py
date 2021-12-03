numbers = [line.strip() for line in open('2021//input//day3.txt').readlines()]
numbers_copy = numbers.copy()

oxy_rating = 0
co2_rating = 0

for i in range(len(numbers[0])):
    num_ones = sum(int(numbers[j][i]) for j in range(len(numbers)))
    bit_i = "1" if num_ones >= (len(numbers) - num_ones) else "0"
    numbers = [number for number in numbers if number[i] == bit_i]
    if len(numbers) == 1:
        oxy_rating = int(numbers[0], 2)
        print(numbers[0], oxy_rating)
        break

numbers = numbers_copy

for i in range(len(numbers[0])):
    num_ones = sum(int(numbers[j][i]) for j in range(len(numbers)))
    bit_i = "0" if num_ones >= (len(numbers) - num_ones) else "1"
    numbers = [number for number in numbers if number[i] == bit_i]
    if len(numbers) == 1:
        co2_rating = int(numbers[0], 2)
        print(numbers[0], co2_rating)
        break

print(oxy_rating * co2_rating)
