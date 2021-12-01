depths = [int(line.strip()) for line in open('2021/input/day1.txt')]

num_increases = sum(1 for i in range(1, len(depths)) if depths[i] > depths[i - 1])
print(num_increases)
