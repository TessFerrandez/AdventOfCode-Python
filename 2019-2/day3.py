inputs1 = '''R8,U5,L5,D3
U7,R6,D4,L4'''

inputs2 = '''R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83'''

inputs3 = '''R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'''


def get_wires(inputs):
    return [line.strip().split(',') for line in inputs.splitlines()]


def get_positions(path):
    positions, pos = [], 0

    for p in path:
        dir = {'R': 1, 'U': 1j, 'L': -1, 'D': -1j}[p[0]]
        steps = int(p[1:])
        for _ in range(steps):
            pos = pos + dir
            positions.append(pos)

    return positions


def intersect(list1, list2):
    return list(set(list1) & set(list2))


def manhattan(pos: complex) -> int:
    return abs(int(pos.imag)) + abs(int(pos.real))


def get_closest_cross(wires):
    crosses = intersect(get_positions(wires[0]), get_positions(wires[1]))
    return min(manhattan(pos) for pos in crosses)


def tests():
    wire1, wire2 = get_wires(inputs1)
    assert intersect(get_positions(wire1), get_positions(wire2)) == [(3 + 3j), (6 + 5j)]

    assert get_closest_cross(get_wires(inputs2)) == 159
    assert get_closest_cross(get_wires(inputs3)) == 135


def part2(wires):
    wire1, wire2 = wires
    w1positions = get_positions(wire1)
    w2positions = get_positions(wire2)
    crosses = intersect(w1positions, w2positions)
    steps1 = [w1positions.index(cross) for cross in crosses]
    steps2 = [w2positions.index(cross) for cross in crosses]
    cross_steps = [steps1[i] + steps2[i] for i in range(len(steps1))]
    return min(cross_steps) + 2


tests()

inputs = open('2019/input/day3.txt').read().strip()
wires = get_wires(inputs)
print("Part 1:", get_closest_cross(wires))
print("Part 2:", part2(wires))
