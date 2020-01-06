from anytree import Node, RenderTree


def read_input() -> list:
    # return [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
    return [int(num) for num in open("input/day8.txt").readline().strip().split(" ")]


def generate_doc_tree(file) -> (Node, int):
    # read header
    n_files, n_meta = file[0:2]
    node = Node("this", meta=None)
    ptr = 2

    # read files
    for _ in range(n_files):
        child_node, file_len = generate_doc_tree(file[ptr:])
        child_node.parent = node
        ptr += file_len

    # read meta data
    node.meta = file[ptr : ptr + n_meta]
    return node, ptr + n_meta


def get_meta_sum(node: Node) -> int:
    meta_sum = sum(node.meta)
    for child in node.children:
        meta_sum += get_meta_sum(child)
    return meta_sum


def get_value(node: Node) -> int:
    if not node.children:
        return sum(node.meta)

    value = 0
    for i in node.meta:
        if len(node.children) > i - 1:
            value += get_value(node.children[i - 1])
    return value


def puzzles():
    file = read_input()
    tree, _ = generate_doc_tree(file)
    print("meta sum:", get_meta_sum(tree))
    print("value:", get_value(tree))


if __name__ == "__main__":
    puzzles()
