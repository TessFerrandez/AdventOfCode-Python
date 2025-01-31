from collections import defaultdict
from input_processing import read_data


def parse(data):
    return [line.split('-') for line in data.split('\n')]


def part1(network_map):
    connections = defaultdict(set)
    combos = set()
    for a, b in network_map:
        connections[a].add(b)
        connections[b].add(a)

    for first in connections:
        if first[0] == 't':
            for second in connections[first]:
                common = connections[first] & connections[second]
                for third in common:
                    combo = tuple(sorted([first, second, third]))
                    combos.add(combo)

    return len(combos)


def part2(network_map):
    # find max cliques
    connections = defaultdict(set)
    for a, b in network_map:
        connections[a].add(b)
        connections[b].add(a)

    # https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
    # start with a maximal clique of one node, and add nodes one at a time
    def bron_kerbosch(current_clique, candidates, excluded):
        # exclude nodes are nodes that are adjacent but that we've already
        # considered in a previous recursive call
        if not candidates and not excluded:
            yield ','.join(sorted(current_clique))
        while candidates:
            node = candidates.pop()
            yield from bron_kerbosch(current_clique | {node}, candidates & connections[node], excluded & connections[node])
            excluded.add(node)

    def max_cliques():
        yield from bron_kerbosch(set(), set(connections), set())

    return max(max_cliques(), key=len)


def test():
    data = '''kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn'''
    assert part1(parse(data)) == 7
    assert part2(parse(data)) == "co,de,ka,ta"


test()
data = read_data(2024, 23)
print('Part1:', part1(parse(data)))
print('Part2:', part2(parse(data)))
