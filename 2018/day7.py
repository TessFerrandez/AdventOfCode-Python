import networkx as nx


def puzzle1():
    graph = nx.DiGraph([(s[1], s[7]) for s
                        in map(str.split, open("input/day7.txt").readlines())])
    print("puzzle1:", ''.join(nx.lexicographical_topological_sort(graph)))


if __name__ == "__main__":
    puzzle1()
