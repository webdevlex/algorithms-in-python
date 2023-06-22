from Graph import DirectedGraph


def makeVisited(adjList):
    visited = {}
    for key in adjList:
        visited[key] = False
    return visited


def routeBetweenNodes(adjList, v1, v2):
    que = []
    visited = makeVisited(adjList)

    que.append(v1)
    visited[v1] = True

    while len(que) != 0:
        currentVertex = que.pop(0)
        for adjVertex in adjList[currentVertex]:
            if not visited[adjVertex]:
                if adjVertex == v2:
                    return True
                que.append(adjVertex)
                visited[adjVertex] = True

    return False


myAdjList = DirectedGraph()
myAdjList.addEdge("A", "B")
myAdjList.addEdge("A", "C")
myAdjList.addEdge("A", "D")
myAdjList.addEdge("D", "B")

print(routeBetweenNodes(myAdjList.adjList, "A", "C"))
