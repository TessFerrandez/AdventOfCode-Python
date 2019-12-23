from anytree import Node


def get_discs() -> (dict, dict):
    discs = dict()
    weights = dict()
    lines = [line.strip() for line in open("input/day7.txt").readlines()]

    for line in lines:
        parts = line.split(' -> ')
        bottom_parts = parts[0].split(' ')
        bottom = bottom_parts[0]
        weights[bottom] = int(bottom_parts[1].replace('(', '').replace(')', ''))
        tops = parts[1].split(', ') if len(parts) == 2 else None
        discs[bottom] = tops

    return discs, weights


def get_bottom_disc(discs: dict) -> str:
    sub_discs = []
    for disc in discs:
        if discs[disc]:
            sub_discs += discs[disc]

    for disc in discs:
        if disc not in sub_discs:
            return disc


def add_children(discs: dict, weights: dict, parent: Node):
    children = discs[parent.name]
    total = 0
    if children is None:
        return 0
    for child in children:
        child_node = Node(child, weight=weights[child], parent=parent)
        child_total = add_children(discs, weights, child_node)
        this_total = weights[child] + child_total
        child_node.total = this_total
        total += this_total
    return total


def generate_tree(discs: dict, weights: dict, bottom_disc: str) -> Node:
    root = Node(bottom_disc, weight=weights[bottom_disc])
    root.total = weights[bottom_disc] + add_children(discs, weights, root)
    return root


def get_unbalanced(root: Node) -> Node:
    totals = [child.total for child in root.children]
    for child in root.children:
        if totals.count(child.total) == 1:
            unbalanced_child = get_unbalanced(child)
            if unbalanced_child is None:
                return child
            else:
                return unbalanced_child
    return None


def puzzles():
    discs, weights = get_discs()
    bottom_disc = get_bottom_disc(discs)
    print("bottom disc:", bottom_disc)
    root = generate_tree(discs, weights, bottom_disc)

    # print(RenderTree(root).by_attr(lambda n: n.name + " (" + str(n.total) + ":" + str(n.weight) + ")"))
    unbalanced_child = get_unbalanced(root)
    unbalanced_total = unbalanced_child.total
    for child in unbalanced_child.parent.children:
        if child.total != unbalanced_total:
            diff = unbalanced_total - child.total
            print("unbalanced weight:", unbalanced_child.weight)
            print("adjusted weight:", unbalanced_child.weight - diff)
            break


if __name__ == "__main__":
    puzzles()
