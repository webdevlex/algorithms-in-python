class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class UndirectedGraph:
    def __init__(self):
        self.adjList = {}

    # ----------------------------------
    # Insert
    # ----------------------------------
    def addEdge(self, v1, v2):
        if v1 not in self.adjList:
            self.adjList[v1] = [v2]
        else:
            self.adjList[v1].append(v2)

        if v2 not in self.adjList:
            self.adjList[v2] = [v1]
        else:
            self.adjList[v2].append(v1)

    # ----------------------------------
    # Print
    # ----------------------------------
    def print(self):
        print(self.adjList)


class DirectedGraph:
    def __init__(self):
        self.adjList = {}

    def addEdge(self, v1, v2):
        if v1 not in self.adjList:
            self.adjList[v1] = [v2]
        else:
            self.adjList[v1].append(v2)

        if v2 not in self.adjList:
            self.adjList[v2] = []

    def print(self):
        print(self.adjList)
