class Node:
    def __init__(self, value=None):
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


class DirectedGraph:
    def __init__(self, numVertices):
        self.numVertices = numVertices
        self.adjList = [None] * numVertices

    def getNodeAt(self, i):
        if i >= self.numVertices:
            return "Out of bound"
        return self.adjList[i]

    def addEdge(self, n1, n2):
        node2 = Node(n2)
        node2.next = self.adjList[n1]
        self.adjList[n1] = node2

    def print(self):
        for i in range(len(self.adjList)):
            print(f"({i})", end="")
            currentNode = self.adjList[i]
            if currentNode != None:
                print(f" -> ({currentNode.value})", end="")
                while currentNode.next != None:
                    currentNode = currentNode.next
                    print(f" -> ({currentNode.value})", end="")
            print()
