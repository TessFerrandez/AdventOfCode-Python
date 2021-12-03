numbers = [line.strip() for line in open('2021//input//day3.txt').readlines()]

num_numbers = len(numbers)
print(num_numbers)

epsilon = ""
gamma = ""

for i in range(len(numbers[0])):
    num_ones = sum(int(numbers[j][i]) for j in range(num_numbers))
    if num_ones >= (num_numbers - num_ones):
        epsilon += "1"
        gamma += "0"
    else:
        epsilon += "0"
        gamma += "1"

print("epsilon", int(epsilon, 2))
print("gamma", int(gamma, 2))
print(int(epsilon, 2) * int(gamma, 2))
