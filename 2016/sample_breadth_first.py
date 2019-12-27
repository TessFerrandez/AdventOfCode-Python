from collections import deque

# 1. Check starting node and add its neighbors to the queue
# 2. Mark the start node as explored
# 3. Get the first node from the queue, remove it from teh queue
# 4. Check if node has already been visited
# 5. If not, go through the neighbors of the node
# 6. Add the neighbor nodes to the queue
# 7. Mark the node as explored
# 8. Loop through steps 3 to 7 until the queue is empty


def breath_first(graph, start):
    # visited nodes
    explored = []
    # nodes to be checked
    queue = deque()
    queue.append(start)

    while queue:
        node = queue.popleft()
        if node not in explored:
            explored.append(node)
            neighbors = graph[node]

            for neighbor in neighbors:
                queue.append(neighbor)

    return explored


def bfs_shortest_path(graph, start, goal):
    explored = []
    queue = [[start]]

    if start == goal:
        return "That was easy! Start == goal"

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbors = graph[node]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor == goal:
                    return new_path
            explored.append(node)
    return "Sorry, no connected paths"


def main():
    graph = {
        "A": ["B", "C", "E"],
        "B": ["A", "D", "E"],
        "C": ["A", "F", "G"],
        "D": ["B"],
        "E": ["A", "B", "D"],
        "F": ["C"],
        "G": ["C"],
    }
    explored = breath_first(graph, "A")
    print(explored)
    path = bfs_shortest_path(graph, "G", "D")
    print(path)


if __name__ == "__main__":
    main()
