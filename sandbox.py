def transpose(adjMatrix):
    numVerticies = len(adjMatrix)

    transposedMatrix = []
    for i in range(numVerticies):
        currentArr = []
        for j in range(numVerticies):
            currentArr.append(0)
        transposedMatrix.append(currentArr)

    for i in range(numVerticies):
        for j in range(numVerticies):
            if adjMatrix[i][j] == 1:
                transposedMatrix[j][i] = 1

    return transposedMatrix


adjMatrix = [
    [0, 1, 1, 0, 0],  # 0
    [0, 0, 1, 0, 0],  # 1
    [0, 0, 0, 1, 0],  # 2
    [0, 1, 0, 0, 1],  # 3
    [0, 0, 1, 0, 0],  # 4
]
output = transpose(adjMatrix)
for item in output:
    print(item)

adjMatrix = [
    [0, 0, 0, 0, 0],  # 0
    [1, 0, 0, 1, 0],  # 1
    [1, 1, 0, 0, 1],  # 2
    [0, 0, 1, 0, 0],  # 3
    [0, 0, 0, 1, 0],  # 4
]
