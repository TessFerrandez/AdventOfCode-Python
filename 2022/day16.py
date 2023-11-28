from input_processing import read_data
from collections import defaultdict
from math import inf
from copy import copy


def parse(data):
    valve_flows = {}
    caves = {}

    for line in data.splitlines():
        _, valve, _, _, flow, _, _, _, _, *neighbors = line.split(' ')
        flow = int(flow[5: -1])
        if flow > 0:
            valve_flows[valve] = flow
        caves[valve] = [neighbors.replace(',', '') for neighbors in neighbors]
    return valve_flows, caves


# floyd-warshall
def get_distances(cave):
    distances = {valve: defaultdict(lambda: inf) for valve in cave}

    for valve in cave:
        distances[valve][valve] = 0
        for neighbor in cave[valve]:
            distances[valve][neighbor] = 1

    for valve1 in cave:
        for valve2 in cave:
            for valve3 in cave:
                distances[valve2][valve3] = min(distances[valve2][valve3], distances[valve2][valve1] + distances[valve1][valve3])

    return distances


def get_flow(order, minutes_left, flows, distances):
    current_valve = 'AA'
    flow = 0

    for next_valve in order:
        minutes_left -= distances[current_valve][next_valve] + 1
        flow += flows[next_valve] * minutes_left
        current_valve = next_valve

    return flow


def get_possible_orders(current_valve, open_valves, minutes_left, valves, distance):
    for next_valve in valves:
        if next_valve not in open_valves and distance[current_valve][next_valve] <= minutes_left:
            open_valves.append(next_valve)
            yield from get_possible_orders(next_valve, open_valves, minutes_left - distance[current_valve][next_valve] - 1, valves, distance)
            open_valves.pop()

    yield copy(open_valves)


def part1(valve_flows, distances):
    valves = list(valve_flows.keys())
    return max(get_flow(order, 30, valve_flows, distances) for order in get_possible_orders('AA', [], 30, valves, distances))


def part2(valve_flows, distances):
    valves = list(valve_flows.keys())
    possible_orders = list(get_possible_orders('AA', [], 30, valves, distances))

    highest_flows = defaultdict(int)
    for order in possible_orders:
        sorted_order = tuple(sorted(order))
        flow = get_flow(order, 26, valve_flows, distances)
        highest_flows[sorted_order] = max(highest_flows[sorted_order], flow)

    highest_flows = list(highest_flows.items())

    highest_flow = 0
    for my_order in range(len(highest_flows)):
        for elephant_order in range(my_order + 1, len(highest_flows)):
            my_valves, my_flow = highest_flows[my_order]
            elephant_valves, elephant_flow = highest_flows[elephant_order]

            if len(set(my_valves) & set(elephant_valves)) == 0:
                highest_flow = max(highest_flow, my_flow + elephant_flow)

    return highest_flow


def test():
    sample = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""
    valve_flows, caves = parse(sample)
    distances = get_distances(caves)
    assert part1(valve_flows, distances) == 1651
    assert part2(valve_flows, distances) == 1707


test()
valve_flows, caves = parse(read_data(2022, 16))
distances = get_distances(caves)
print("Part1:", part1(valve_flows, distances))
print("Part2:", part2(valve_flows, distances))
