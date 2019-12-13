def get_closest(coord, coords):
    best_i = -1
    dist_draw = False
    best_distance = 1000000

    for i in range(len(coords)):
        distance = abs(coord[0] - coords[i][0]) + abs(coord[1] - coords[i][1])
        if distance < best_distance:
            best_distance = distance
            best_i = i
            dist_draw = False
        elif distance == best_distance:
            best_i = -1
            dist_draw = True

    if dist_draw:
        return -1
    else:
        return best_i


def get_maxes(coords):
    max_x, max_y = 0, 0
    for coord in coords:
        max_x = max(max_x, coord[0])
        max_y = max(max_y, coord[1])
    return max_x + 1, max_y + 1


def puzzle1():
    coords = [[int(x) for x in line.strip().split(', ')] for line in open("input/day6.txt").readlines()]
    num_coords = len(coords)
    coord_count = {-1: 0}
    is_excluded = {-1: True}

    max_x, max_y = get_maxes(coords)

    for i in range(num_coords):
        coord_count[i] = 0
        is_excluded[i] = False

    for col in range(max_x + 1):
        for row in range(max_y):
            closest_coord = get_closest((col, row), coords)
            if col == 0 or col == max_x or row == 0 or row == max_y:
                is_excluded[closest_coord] = True
            else:
                coord_count[closest_coord] += 1

    for coord in is_excluded:
        if is_excluded[coord]:
            coord_count[coord] = 0

    largest_area = max(coord_count[coord] for coord in coord_count)
    print("largest area:", largest_area)


def get_total_distance(this_coord, coords):
    total_distance = 0
    for coord in coords:
        total_distance += abs(this_coord[0] - coord[0]) + abs(this_coord[1] - coord[1])
    return total_distance


def puzzle2():
    coords = [[int(x) for x in line.strip().split(', ')] for line in open("input/day6.txt").readlines()]
    max_x, max_y = get_maxes(coords)

    in_area = 0
    for col in range(max_x + 1):
        for row in range(max_y + 1):
            total_distance = get_total_distance((col, row), coords)
            if total_distance < 10000:
                in_area += 1

    print("in area:", in_area)


if __name__ == "__main__":
    puzzle1()
    puzzle2()