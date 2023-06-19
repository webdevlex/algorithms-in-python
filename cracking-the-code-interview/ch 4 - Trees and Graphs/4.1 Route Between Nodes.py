from Graph import DirectedGraph


def routeBetweenNodes(adjList, n1, n2):
    node1 = adjList.getNodeAt(n1)
    while node1 != None:
        if node1.value == n2:
            return True
        node1 = adjList.getNodeAt(node1.value)

    node2 = adjList.getNodeAt(n2)
    while node2 != None:
        if node2.value == n1:
            return True
        node2 = adjList.getNodeAt(node2.value)
    return False


myAdjList = DirectedGraph(4)
myAdjList.addEdge(0, 1)
myAdjList.addEdge(1, 3)
myAdjList.addEdge(2, 3)
myAdjList.print()

print(routeBetweenNodes(myAdjList, 1, 2))
