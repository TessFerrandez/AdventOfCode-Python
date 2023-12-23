from queue import PriorityQueue
from input_processing import read_data


class Brick:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.floor = self.start[2]
        self.height = self.end[2] - self.start[2]
        self.support = []
        self.supporting = []

    def __lt__(self, other):
        return self.floor < other.floor


def parse(data):
    bricks = PriorityQueue()

    for start, end in [line.split('~') for line in data.splitlines()]:
        start = tuple(map(int, start.split(',')))
        end = tuple(map(int, end.split(',')))
        brick = Brick(start, end)
        bricks.put(brick)

    return bricks


def settle_bricks(bricks):
    def brick_supports(brick, stable_brick):
        return stable_brick.start[0] <= brick.end[0] and brick.start[0] <= stable_brick.end[0] and \
            stable_brick.start[1] <= brick.end[1] and brick.start[1] <= stable_brick.end[1]

    floor_level = 1
    stable_bricks = []

    while not bricks.empty():
        brick = bricks.get()
        if brick.floor == floor_level:
            stable_bricks.append(brick)
        else:
            support, support_level = [], 0

            for stable_brick in stable_bricks:
                if brick_supports(brick, stable_brick):
                    stable_brick_top = stable_brick.floor + stable_brick.height
                    if stable_brick_top > support_level:
                        support, support_level = [], stable_brick_top
                    if stable_brick_top == support_level:
                        support.append(stable_brick)

            brick.support = support
            brick.floor = support_level + 1
            stable_bricks.append(brick)

            for support_brick in support:
                support_brick.supporting.append(brick)

    return stable_bricks


def part1(stable_bricks):
    count = 0

    for stable_brick in stable_bricks:
        if len(stable_brick.supporting) > 0:
            bricks_we_support_that_are_supported_by_others = sum([1 for support in stable_brick.supporting if len(support.support) > 1])
            if bricks_we_support_that_are_supported_by_others == len(stable_brick.supporting):
                count += 1
        else:
            count += 1

    return count


def part2(stable_bricks):
    count = 0
    for stable_brick in stable_bricks:
        fall_stack = [s for s in stable_brick.supporting if len(s.support) == 1]
        fallen = set()
        while len(fall_stack) > 0:
            falling_brick = fall_stack.pop(0)
            fallen.add(falling_brick)
            fall_stack.extend([s for s in falling_brick.supporting if len(set(s.support).difference(fallen)) == 0])
        count += len(fallen)
    return count


def test():
    sample = '''1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9'''
    bricks = parse(sample)
    stable_bricks = settle_bricks(bricks)
    assert part1(stable_bricks) == 5
    assert part2(stable_bricks) == 7


test()
data = read_data(2023, 22)
bricks = parse(data)
stable_bricks = settle_bricks(bricks)
print('Part1:', part1(stable_bricks))
print('Part2:', part2(stable_bricks))
