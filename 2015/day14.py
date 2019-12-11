deer = []


def parse_input():
    global deer

    lines = [line.split(' ') for line in open("input/day14.txt").readlines()]
    deer = [[line[0], int(line[3]), int(line[6]), int(line[13])]
            for line in lines]


def traveled_after(deer_info, num_seconds):
    distance = 0
    total_seconds = 0
    distances = []

    while True:
        for i in range(deer_info[2]):
            total_seconds += 1
            if total_seconds > num_seconds:
                return distance, distances
            distance += deer_info[1]
            distances.append(distance)

        for i in range(deer_info[3]):
            total_seconds += 1
            if total_seconds > num_seconds:
                return distance, distances
            distances.append(distance)


def puzzles():
    parse_input()
    max_distance = 0
    all_distances = []
    for doe in deer:
        distance, distances = traveled_after(doe, 2503)
        all_distances.append(distances)
        if distance > max_distance:
            max_distance = distance

    print("max distance:", max_distance)

    num_deer = len(deer)
    deer_points = [0] * num_deer
    for i in range(2503):
        second_distances = [all_distances[j][i] for j in range(num_deer)]
        best_distance = max(second_distances)
        leaders = [i for i, x in enumerate(second_distances)
                   if x == best_distance]
        for doe in leaders:
            deer_points[doe] += 1

    print("max points:", max(deer_points))


if __name__ == "__main__":
    puzzles()
