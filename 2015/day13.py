from itertools import permutations


people = []
relations = dict()


def parse_input():
    global people
    global relations

    lines = [line.strip()[0:-1] for line in open("input/day13.txt").readlines()]
    for line in lines:
        parts = line.split(' ')
        person_from = parts[0]
        person_to = parts[10]
        people.append(person_from)
        people.append(person_to)

        happiness = int(parts[3])
        if parts[2] == "lose":
            happiness = 0 - happiness

        relations[(person_from, person_to)] = happiness

    people = list(set(people))


def calculate_happiness(table):
    happiness = 0
    num_people = len(table)
    for i in range(num_people):
        happiness += relations[(table[i], table[(i - 1) % num_people])]
        happiness += relations[(table[i], table[(i + 1) % num_people])]
    return happiness


def find_best_arrangement():
    tables = [calculate_happiness(table) for table in permutations(people)]
    return max(tables)


def add_yourself():
    for person in people:
        relations[(person, 'me')] = 0
        relations[('me', person)] = 0
    people.append('me')


def puzzles():
    parse_input()
    print("best table:", find_best_arrangement())
    add_yourself()
    print("best table:", find_best_arrangement())


if __name__ == "__main__":
    puzzles()
