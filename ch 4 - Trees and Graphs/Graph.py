class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class UndirectedGraph:
    def __init__(self, numVertices):
        self.numVertices = numVertices
        self.adjList = [None] * numVertices

    def addEdge(self, n1, n2):
        node2 = Node(n2)
        node2.next = self.adjList[n1]
        self.adjList[n1] = node2

        node1 = Node(n1)
        node1.next = self.adjList[n2]
        self.adjList[n2] = node1

    def print(self):
        for i in range(len(self.adjList)):
            print(f"({i})", end="")
            currentNode = self.adjList[i]
            if currentNode != None:
                print(f" <-> ({currentNode.value})", end="")
                while currentNode.next != None:
                    currentNode = currentNode.next
                    print(f" <-> ({currentNode.value})", end="")
            print()


graph = UndirectedGraph(4)
graph.addEdge(0, 1)
graph.addEdge(1, 2)
graph.addEdge(2, 3)
graph.print()
