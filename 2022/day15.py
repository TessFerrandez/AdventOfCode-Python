from input_processing import read_data, get_numbers_from_lines
import numpy as np
import matplotlib.pyplot as plt


def parse(data):
    return [[sx, sy, abs(sx - bx) + abs(sy - by)] for sx, sy, bx, by in get_numbers_from_lines(data)]


def calculate_intervals(sensor_data, row):
    '''
    for each sensor in sensor data
    if the row we are looking for is in view
    add the intervals that are in view
    '''
    intervals = []

    for sx, sy, sensor_range in sensor_data:
        row_dist = abs(row - sy)
        if row_dist <= sensor_range:
            side_view = sensor_range - row_dist
            intervals.append([sx - side_view, sx + side_view])

    return intervals


def merge_intervals(intervals):
    result = []
    intervals.sort()

    for start, end in intervals:
        if result and result[-1][1] >= start - 1:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])

    return result


def part1(sensor_data, row):
    intervals = calculate_intervals(sensor_data, row)
    intervals = merge_intervals(intervals)
    return sum(end - start for start, end in intervals)


def possible_sensor(intervals, max_pos):
    for _, end in intervals:
        if end < 0:
            continue
        if end < max_pos:
            return end + 1
        else:
            return None

    return 0


# 19 seconds - look through all rows
def part2_all_rows(sensor_data, max_pos):
    for y in range(max_pos + 1):
        intervals = calculate_intervals(sensor_data, y)
        intervals = merge_intervals(intervals)
        sensor_x = possible_sensor(intervals, max_pos)
        if sensor_x:
            return sensor_x * 4000000 + y


def in_sensor_range(px, py, sensor_data):
    for sx, sy, sensor_range in sensor_data:
        if abs(px - sx) + abs(py - sy) <= sensor_range:
            return True
    return False


# 10 seconds - look at the perimeter of all diamonds
def part2_perimeters(sensor_data, max_pos):
    for x, y, sensor_range in sensor_data:
        min_y = max(y - sensor_range - 1, 0)
        max_y = min(y, max_pos)
        for py in range(min_y, max_y + 1):
            px = x + sensor_range - abs(y - py) + 1
            if 0 <= px <= max_pos:
                if not in_sensor_range(px, py, sensor_data):
                    return px * 4000000 + py


def rotate_45(x, y):
    return (x + y), (y - x)


def rotate_back_45(x, y):
    return (x - y) // 2, (x + y) // 2


def find_missing(rotated_sensors):
    for _, s_bottom_right in rotated_sensors:
        x, _ = s_bottom_right
        merged_intervals = []

        # find all sensors in range of x
        # merge the y intervals to see what y:s they cover
        for top_left, bottom_right in rotated_sensors:
            left_x, top_y = top_left
            right_x, bottom_y = bottom_right

            if left_x <= x + 1 <= right_x:
                merged_intervals.append((top_y, bottom_y))

        merged_intervals = merge_intervals(merged_intervals)

        # if we have a gap on a row we have 2+ intervals
        # the gap is right after the end of the first interval
        if len(merged_intervals) > 1:
            _, y = merged_intervals[0]
            return rotate_back_45(x + 1, y + 1)


# solution heavily based on Daniels - rotating 45 degrees - super quick
def part2(sensors):
    """
    We want to find any positions along the \\ perimeter that can not be seen by any other sensors
    (could have picked any perimeter, but one is enough)
    In order to not have to look at every spot (as in my perimeter code), we rotate 45 degrees
    and look at intervals of other sensors

    ..a..    a---b
    ./.\\.    |...|
    c...b  =>|...|
    .\\./.    |...|
    ..c..    d---c

    we're looking for the missing (X) here

       ┌---┐
    a---b  |
    |..└|--┘
    |...|X
    |..┌|--┐
    d---c  |
       └---┘
    """
    # the boxes that the sensors can see - rotated 45 deg right
    rotated_sensors = [[rotate_45(x, y - range),    # top left
                        rotate_45(x, y + range)]    # bottom right
                       for x, y, range in sensors]

    x, y = find_missing(rotated_sensors)
    return x * 4000000 + y


def draw_map(sensor_data):
    min_x = min([sx - sensor_range for sx, _, sensor_range in sensor_data])
    max_x = max([sx + sensor_range for sx, _, sensor_range in sensor_data])
    min_y = min([sy - sensor_range for _, sy, sensor_range in sensor_data])
    max_y = max([sy + sensor_range for _, sy, sensor_range in sensor_data])

    width, height = max_x - min_x + 1, max_y - min_y + 1
    offset_x, offset_y = -min_x, -min_y

    grid = np.zeros((height, width))

    sensor_num = 1
    for sx, sy, sensor_range in sensor_data:
        for y in range(sy - sensor_range, sy + sensor_range + 1):
            dx = sensor_range - abs(y - sy)
            grid[y + offset_y: y + 1 + offset_y,
                 sx - dx + offset_x: sx + dx + 1 + offset_x] = sensor_num * 5
        sensor_num += 1

    plt.imshow(grid, extent=[min_x, max_x, max_y, min_y])
    plt.show()


def test():
    sample = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""
    sensor_data = parse(sample)
    draw_map(sensor_data)
    assert part1(sensor_data, 10) == 26
    assert part2(sensor_data) == 56000011


test()
data = parse(read_data(2022, 15))
print('Part1:', part1(data, 2000000))
print('Part2:', part2(data))
