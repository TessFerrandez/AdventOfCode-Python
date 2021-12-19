from collections import Counter
from typing import Tuple, List


def get_scanners():
    raw_scanners = [scanner for scanner in open('2021/input/day19.txt').read().split('\n\n')]

    scanners = []
    for raw_scanner in raw_scanners:
        scanner = [[int(d) for d in line.strip().split(',')] for line in raw_scanner.splitlines()[1:]]
        scanners.append(scanner)

    return scanners


def check_if_scanners_overlap(scanners, base: int, to_check: int) -> Tuple[List[int], List[Tuple[int, int]]]:
    """
    Check if two scanners overlap (have 12+ beacons in common)

    1. We can check this one "direction" at a time as there are no beacons with duplicate x, y, or z coordinates
    2. We can assume that the base scanner (0) is aligned at X, Y, Z (whatever its alignment is, well just call it X, Y, Z)
    3. The other scanner will be aligned at a random combo of [X, -X, Y, -Y, Z, -Z] (24 options)

    Once we find a direction where we have 12 common, we've found our scanner and know its orientation and offset
    If they overlap, offsets, and orientations will not be empty
    """
    offsets, orientation = [], []
    base_scanner = scanners[base]
    scanner_to_check = scanners[to_check]

    # the base scanner is aligned at X, Y, Z => Column [0, 1, 2]
    # We want to find the offset and the orientation of the pair scanner in all 3 dirs
    for base_i in range(3):

        # the scanner to check, can have any combination of [X, -X, Y, -Y, Z, -Z]
        # we check one orientation/direction at a time (X = (1,0) -Y = (-1, 1) etc.)
        for sign, dir in [(1, 0), (-1, 0), (1, 1), (-1, 1), (1, 2), (-1, 2)]:

            # get all the diffs between the base and the possible orientations/directions of the check_scanner
            diffs = [beacon0[base_i] - sign * beacon1[dir]
                     for beacon1 in scanner_to_check
                     for beacon0 in base_scanner]

            # if we have 12+ matched in any direction, we have found our pair scanner
            # and we know the offset, and also the orientation/direction of this column
            offset, matching_beacons = Counter(diffs).most_common()[0]

            if matching_beacons >= 12:
                offsets.append(offset)
                orientation.append((sign, dir))

    return offsets, orientation


def find_overlapping(scanner: int, to_check: List[int]) -> Tuple[int, List[int], List[Tuple[int, int]]]:
    for other_scanner in to_check:
        offsets, orientation = check_if_scanners_overlap(scanners, scanner, other_scanner)
        if len(offsets) > 0:
            return other_scanner, offsets, orientation
    return -1, [], []


def align_scanner(scanner, offsets, orientation):
    to_align = scanners[scanner]

    # align orientation
    sign0, col0 = orientation[0]
    sign1, col1 = orientation[1]
    sign2, col2 = orientation[2]
    to_align = [[sign0 * beacon[col0], sign1 * beacon[col1], sign2 * beacon[col2]] for beacon in to_align]

    # align offset
    to_align = [[beacon[0] + offsets[0], beacon[1] + offsets[1], beacon[2] + offsets[2]] for beacon in to_align]

    scanners[scanner] = to_align


def align_scanners(scanners):
    aligned_scanners = [0]
    un_aligned_scanners = [i for i in range(1, len(scanners))]

    all_offsets = []

    while un_aligned_scanners:
        for i in aligned_scanners:
            overlapping_scanner, offsets, orientation = find_overlapping(i, un_aligned_scanners)
            if overlapping_scanner != -1:
                print("Found overlapping scanners:", i, overlapping_scanner, offsets, orientation)
                align_scanner(overlapping_scanner, offsets, orientation)
                un_aligned_scanners.remove(overlapping_scanner)
                aligned_scanners.append(overlapping_scanner)
                all_offsets.append(offsets)

    return all_offsets


def count_beacons(scanners):
    unique_beacons = set()

    for scanner in scanners:
        for beacon in scanner:
            unique_beacons.add((beacon[0], beacon[1], beacon[2]))

    return len(unique_beacons)


def get_biggest_manhattan_distance(offsets) -> int:
    biggest_distance = 0

    for i in range(len(offsets)):
        for j in range(i + 1, len(offsets)):
            manhattan = abs(offsets[i][0] - offsets[j][0]) + abs(offsets[i][1] - offsets[j][1]) + abs(offsets[i][2] - offsets[j][2])
            biggest_distance = max(biggest_distance, manhattan)

    return biggest_distance


scanners = get_scanners()
offsets = align_scanners(scanners)

print("Part1:", count_beacons(scanners))
print("Part2:", get_biggest_manhattan_distance(offsets))
