"""
based on solution by leftfish
I started with an extrememly similar solution but kept getting stuck on a pesky issue with the larget test data
Probably ordering of splittable and explosive nodes - so just gave up and started over with this solution
My solution would explode - and then react to any resulting reactions --
This solution simply picks the next explosive - and if no explosive exists, pick the next splittable
I must have read the instructions wrong...
"""
from json import loads
import logging


logging.getLogger().setLevel(logging.INFO)

EXPLOSIVE_DEPTH = 4
SPLITTABLE = 10


class Node:
    def __init__(self, data, parent=None, depth=1):
        self.left = None
        self.right = None
        self.parent = None
        self.value = None
        self.parent = parent
        self.depth = depth

        if data is None:
            # new empty node for addition
            self.parent = None
        elif type(data) is list:
            # add list of nodes
            self.left = Node(data[0], self, depth + 1)
            self.right = Node(data[1], self, depth + 1)
        else:
            # add value node
            self.value = data

    def _add_tree(self, other_node):
        def update_depth(root):
            if root:
                update_depth(root.left)
                root.depth += 1
                update_depth(root.right)

        new_root = Node(data=None, depth=0)
        new_root.left = self
        new_root.right = Node(other_node, new_root)
        self.parent = new_root

        # update depth of all nodes (simple in-order traversal)
        update_depth(new_root)
        return new_root

    def _explode_node(self):
        if self.value is not None:
            raise Exception('This type of node cannot explode!')

        left, right = self.left._find_left_leaf(), self.right._find_right_leaf()

        if left:
            left.value += self.left.value
        if right:
            right.value += self.right.value

        self.value = 0
        self.left = None
        self.right = None

    def _find_first_explosive_node(self):
        # in-order traversal until an explosive node is found
        current = self
        stack = []

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                if current._is_explosive() and current._has_only_leafs():
                    return current
                current = current.right
            else:
                break
        return None

    def _find_left_leaf(self):
        current_parent = self.parent

        if current_parent.left.value is not None and current_parent.left is not self:
            # left on same level
            return current_parent.left
        else:
            prev_parent = current_parent.parent
            if current_parent.parent is None:
                # we tried going left but reached root - no lefts
                return None
            elif current_parent == prev_parent.right:
                # we went up to a 'right' node - looking in its 'left' neighbor
                return prev_parent.left._find_rightmost_leaf()
            else:
                # we went up, not at root yet, let's go up until we're in a 'right' node
                return current_parent._find_left_leaf()

    def _find_leftmost_leaf(self):
        if self.value is not None:
            return self
        else:
            return self.left._find_leftmost_leaf()

    def _find_right_leaf(self):
        current_parent = self.parent

        if current_parent.right.value is not None and current_parent.right is not self:
            # right on the same level?
            return current_parent.right
        else:
            prev_parent = current_parent.parent
            if current_parent.parent is None:
                # we tried going right but reached root - no rights!
                return None
            elif current_parent == prev_parent.left:
                # we went up to a 'left' node - looking in its 'right' neighbor
                return prev_parent.right._find_leftmost_leaf()
            else:
                # we went up, not at root yet, let's go up until we're in a 'left' node
                return current_parent._find_right_leaf()

    def _find_rightmost_leaf(self):
        if self.value is not None:
            return self
        else:
            return self.right._find_rightmost_leaf()

    def _find_first_splitting_node(self):
        # in-order traversal until a value to split is found
        current = self
        stack = []

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                if current._should_split():
                    return current
                current = current.right
            else:
                break
        return None

    def _has_only_leafs(self):
        return (self.left and self.left.value is not None) and (self.right and self.right.value is not None)

    def _is_explosive(self):
        return self.depth > EXPLOSIVE_DEPTH

    def _reduce_tree(self):
        explosive, splittable = self._find_first_explosive_node(), self._find_first_splitting_node()

        while explosive or splittable:
            logging.debug(f'   ---> Now to explode: {explosive}. To split: {splittable}')
            if explosive:
                logging.debug(f'BOOM {explosive}')
                explosive._explode_node()
                logging.debug(f'After explode:\t{self}')
            elif splittable:
                logging.debug(f'SPLIT {splittable}')
                splittable._split_node()
                logging.debug(f'After split:\t{self}')
            explosive, splittable = self._find_first_explosive_node(), self._find_first_splitting_node()

    def _should_split(self):
        return self.value and self.value >= SPLITTABLE

    def _split_node(self):
        if self.value is None or self.value < SPLITTABLE:
            raise Exception('This type of node cannot split!')

        left_value = self.value // 2
        right_value = self.value - left_value

        self.value = None
        self.left = Node(left_value, self, self.depth + 1)
        self.right = Node(right_value, self, self.depth + 1)

    def __repr__(self):
        return f'{self.value}' if self.value is not None else f'[{self.left},{self.right}]'

    def add_line(self, line: list):
        tree = self._add_tree(line)
        tree._reduce_tree()
        return tree

    def calculate_magnitude(self) -> int:
        acc = 0
        if self.left.value is not None:
            acc += 3 * self.left.value
        else:
            acc += 3 * self.left.calculate_magnitude()
        if self.right.value is not None:
            acc += 2 * self.right.value
        else:
            acc += 2 * self.right.calculate_magnitude()
        return acc


def part1(data: list) -> int:
    tree = Node(loads(data[0]), None)
    for line in data[1:]:
        new_line = loads(line)
        tree = tree.add_line(new_line)
        # print(tree)
    return tree.calculate_magnitude()


def part2(data: list) -> int:
    maximum = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if i == j:
                continue
            tree = Node(loads(data[i]), None)
            new_tree = tree.add_line(loads(data[j]))
            mag = new_tree.calculate_magnitude()
            maximum = max(maximum, mag)
    return maximum


raw_data = '''[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]'''

print('Tests...')
data = raw_data.splitlines()
print('Part 1:', part1(data) == 4140)
print('Part 2:', part2(data) == 3993)
print('---------------------')

print('Solution...')
with open('2021/input/day18.txt', mode='r') as input_file:
    raw_data = input_file.read()
    data = raw_data.splitlines()
    print('Part1:', part1(data))
    print('Part2:', part2(data))
