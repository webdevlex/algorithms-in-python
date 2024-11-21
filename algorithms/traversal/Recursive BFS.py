class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)


def dfs(node):
    visited = set()

    def dfs_helper(node):
        if node in visited:
            return

        visited.add(node)
        print(node.value)

        for neighbor in node.neighbors:
            dfs_helper(neighbor)

    dfs_helper(node)


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

dfs(node1)
