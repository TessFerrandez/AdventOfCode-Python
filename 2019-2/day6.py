from functools import lru_cache


inputs = '''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L'''

inputs2 = '''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN'''


def parse(inputs):
    return {line.strip().split(')')[1]: line.strip().split(')')[0] for line in inputs.splitlines()}


file_inputs = open('2019/input/day6.txt').read().strip()
orbits = parse(file_inputs)


@lru_cache()
def get_num_orbits_for(object) -> int:
    if object not in orbits:
        return 0
    return 1 + get_num_orbits_for(orbits[object])


def orbits_for(object):
    my_orbits = [object]
    orbiting = orbits[object]

    while orbiting in orbits:
        my_orbits.append(orbiting)
        orbiting = orbits[orbiting]
    my_orbits.append(orbiting)

    return my_orbits


def part2() -> int:
    you_orbits = orbits_for('YOU')
    san_orbits = orbits_for('SAN')

    i = 1
    while (you_orbits[-i] == san_orbits[-i]):
        i += 1

    return len(you_orbits) + len(san_orbits) - 2 * i


print("Part 1:", sum(get_num_orbits_for(object) for object in orbits))
print("Part 2:", part2())
