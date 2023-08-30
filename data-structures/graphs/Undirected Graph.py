class Undirected_Graph:
    def __init__(self, num_nodes):
        self.graph = [[] for i in range(num_nodes)]
        self.num_nodes = num_nodes

    # ----------------------------------
    # Insert
    # ----------------------------------
    def insert(self, n1, n2):
        self.graph[n1].append(n2)
        self.graph[n2].append(n1)

    # ----------------------------------
    # Print
    # ----------------------------------
    def print_graph(self):
        print(self.graph)

    # ----------------------------------
    # Depth First Search (Recursive)
    # ----------------------------------
    def DFS_helper(self, current_idx, visited, result):
        visited[current_idx] = True
        for node in self.graph[current_idx]:
            if not visited[node]:
                self.DFS_helper(node, visited, result)
        result.append(current_idx)

    def DFS(self):
        visited = [False] * self.num_nodes
        result = []
        self.DFS_helper(0, visited, result)
        return result

    # ----------------------------------
    # Breadth First Search (Iterative)
    # ----------------------------------
    def BFS_iter(self):
        visited = [False] * self.num_nodes
        visited[0] = True
        result = [0]

        current_idx = 0
        while len(result) != self.num_nodes:
            for node in self.graph[current_idx]:
                if not visited[node]:
                    visited[node] = True
                    result.append(node)
            current_idx += 1
        return result
