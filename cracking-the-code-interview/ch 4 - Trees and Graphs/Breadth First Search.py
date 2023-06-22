from Graph import UndirectedGraph


def makeVisited(adjList):
    visited = {}
    for key in adjList:
        visited[key] = False
    return visited


def BFS(adjList):
    orderVisited = []
    que = []
    visited = makeVisited(adjList)
    firstKey = list(adjList.keys())[0]

    orderVisited.append(firstKey)
    que.append(firstKey)

    visited[firstKey] = True

    while len(que) != 0:
        currentVertex = que.pop(0)
        for adjVertex in adjList[currentVertex]:
            if not visited[adjVertex]:
                orderVisited.append(adjVertex)
                que.append(adjVertex)
                visited[adjVertex] = True

    return orderVisited


myGraph = UndirectedGraph()
myGraph.addEdge("A", "B")
myGraph.addEdge("A", "C")

orderVisited = BFS(myGraph.adjList)
print(orderVisited)
