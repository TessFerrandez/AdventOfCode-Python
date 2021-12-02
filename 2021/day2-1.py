instructions = [line.strip() for line in open('2021//input//day2.txt')]

position = 0
depth = 0

for instruction in instructions:
    parts = instruction.split()
    op, val = parts[0], int(parts[1])
    if op == 'forward':
        position += val
    elif op == 'up':
        depth -= val
    elif op == 'down':
        depth += val

print(depth, position, depth * position)
