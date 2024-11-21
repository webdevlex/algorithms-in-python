from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)


def bfs(node):
    que = deque([node])

    visited = set()
    visited.add(node)

    while que:
        current = que.popleft()
        print(current.value)

        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                que.append(neighbor)


# Initialize nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Manually add edges (neighbors) to represent a graph
node1.add_neighbor(node2)  # Edge from node1 to node2
node1.add_neighbor(node3)  # Edge from node1 to node3
node2.add_neighbor(node4)  # Edge from node2 to node4
node3.add_neighbor(node4)  # Edge from node3 to node4

bfs(node1)
