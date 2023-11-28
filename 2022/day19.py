from input_processing import read_data


ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3


def parse_blueprint(blueprint):
    words = blueprint.split()
    ore = (int(words[6]), 0, 0, 0)
    clay = (int(words[12]), 0, 0, 0)
    obsidian = (int(words[18]), int(words[21]), 0, 0)
    geode = (int(words[27]), 0, int(words[30]), 0)
    return ore, clay, obsidian, geode


def parse(data):
    return [parse_blueprint(blueprint) for blueprint in data.splitlines()]


def get_max_geodes(blueprint, minutes):
    resources = (0, 0, 0, 0)
    robots = (1, 0, 0, 0)
    max_needed = [max(blueprint[robot][resource_type] for robot in range(4)) for resource_type in range(4)]

    todo = [(minutes, resources, robots, None)]
    max_geodes = 0

    while todo:
        minutes_left, resources, robots, last_robot = todo.pop()

        if minutes_left == 0:
            max_geodes = max(max_geodes, resources[GEODE])
            continue

        # shortcut the path if we can't beat our current max
        if max_geodes - resources[GEODE] >= (minutes_left * (2 * robots[GEODE] + minutes_left - 1)) // 2:
            continue

        minutes_left -= 1
        waiting_for_robot = False

        for robot_type, ingredients in enumerate(blueprint):
            # skip if we already have enough robots of this type
            if robot_type != GEODE and robots[robot_type] * minutes_left + resources[robot_type] > max_needed[robot_type] * minutes_left:
                continue

            # skip if we could have created one last minute
            if (not last_robot or last_robot == robot_type) and all(resources_needed <= resources[resource_type] - robots[resource_type] for resource_type, resources_needed in enumerate(ingredients)):
                continue

            # skip if we don't have enough resources to create the robot
            if any(resources[res_type] < res_needed for res_type, res_needed in enumerate(ingredients)):
                waiting_for_robot = waiting_for_robot or \
                    all(robots[res_type] > 0 for res_type in range(4) if ingredients[res_type] > 0)
                continue

            # let's buy this robot
            next_resources = tuple([count + robots[res_type] - ingredients[res_type] for res_type, count in enumerate(resources)])
            next_robots = tuple([count + int(robot_type == resource_type) for resource_type, count in enumerate(robots)])

            todo.append((minutes_left, next_resources, next_robots, robot_type))

        if waiting_for_robot:
            # just gather supplies
            next_resources = tuple([count + robots[res_type] for res_type, count in enumerate(resources)])
            todo.append((minutes_left, next_resources, robots, None))

    return max_geodes


def part1(blueprints):
    total_quality = 0

    for i, blueprint in enumerate(blueprints):
        total_quality += (i + 1) * get_max_geodes(blueprint, 24)

    return total_quality


def part2(blueprints):
    blueprint_product = 1

    for blueprint in blueprints[:3]:
        blueprint_product *= get_max_geodes(blueprint, 32)

    return blueprint_product


def test():
    sample = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""
    blueprints = parse(sample)
    assert part1(blueprints) == 33
    assert part2(blueprints) == 3472


test()
blueprints = parse(read_data(2022, 19))
print('Part1:', part1(blueprints))
print('Part2:', part2(blueprints))
