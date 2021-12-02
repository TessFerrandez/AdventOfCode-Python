instructions = [line.strip() for line in open('2021//input//day2.txt')]

position = 0
depth = 0
aim = 0

for instruction in instructions:
    parts = instruction.split()
    op, val = parts[0], int(parts[1])
    if op == 'forward':
        position += val
        depth += aim * val
    elif op == 'up':
        aim -= val
    elif op == 'down':
        aim += val

print(depth, position, aim, depth * position)
