from Graph import DirectedGraph


def DFS(adjList):
    visited = makeVisited(adjList)
    orderVisited = []

    firstVertex = list(adjList)[0]
    helper(adjList, visited, orderVisited, firstVertex)
    return orderVisited


def makeVisited(adjList):
    visited = {}
    for key in adjList:
        visited[key] = False
    return visited


def helper(adjList, visited, orderVisited, currentVertex):
    visited[currentVertex] = True
    orderVisited.append(currentVertex)
    for adjVertex in adjList[currentVertex]:
        if not visited[adjVertex]:
            helper(adjList, visited, orderVisited, adjVertex)


myAdjList = DirectedGraph()
myAdjList.addEdge("A", "B")
myAdjList.addEdge("B", "C")
myAdjList.addEdge("C", "D")
myAdjList.addEdge("A", "E")
myAdjList.addEdge("E", "C")

print(myAdjList.adjList)

print(DFS(myAdjList.adjList))
