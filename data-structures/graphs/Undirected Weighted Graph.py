class Undirected_Weighted_Graph:
    def __init__(self, num_nodes):
        self.graph = []
        self.dict = self.__init_dict(num_nodes)
        self.num_nodes = num_nodes

    def __init_dict(self, num_nodes):
        my_dict = {}
        for i in range(num_nodes):
            my_dict[i] = []
        return my_dict

    # ----------------------------------
    # Insert
    # ----------------------------------
    def insert(self, n1, n2, w):
        self.graph.append([n1, n2, w])
        self.graph.append([n2, n1, w])
        self.dict[n1].append([n1, n2, w])
        self.dict[n2].append([n2, n1, w])

    # ----------------------------------
    # Print
    # ----------------------------------
    def print_graph(self):
        print(self.graph)
        print(self.dict)

    # ----------------------------------
    # Prims
    # ----------------------------------
    def __add_nodes_edges(self, visited, myHeap, idx):
        visited[idx] = True
        for edge in self.dict[idx]:
            myHeap.push(edge)

    def prims(self):
        visited = [False] * self.num_nodes
        result = []

        myHeap = Heap_Weighted()
        self.__add_nodes_edges(visited, myHeap, 0)

        while len(result) != (self.num_nodes - 1):
            n1, n2, w = myHeap.pop()
            if not visited[n2]:
                result.append([n1, n2, w])
                self.__add_nodes_edges(visited, myHeap, n2)

        return result
