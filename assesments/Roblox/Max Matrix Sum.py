def solution(matrix, size):
    numRows = len(matrix)
    numColumns = len(matrix[0])
    allMatricies = []

    maxMatrixSum = 0
    for i in range(numRows - (size - 1)):
        for j in range(numColumns - (size - 1)):
            currentMatrix = []
            currentMatrixSum = 0
            for i2 in range(i, i + size):
                for j2 in range(j, j + size):
                    currentNum = matrix[i2][j2]
                    currentMatrix.append(currentNum)
                    currentMatrixSum += currentNum

            allMatricies.append([currentMatrixSum, currentMatrix])
            if currentMatrixSum > maxMatrixSum:
                maxMatrixSum = currentMatrixSum

    result = set()
    for item in allMatricies:
        if item[0] == maxMatrixSum:
            result.update(item[1])
    print(sum(result))


matrix = [[1, 0, 1, 5, 6], [3, 3, 0, 3, 3], [2, 9, 2, 1, 2], [0, 2, 4, 2, 0]]

solution(matrix, 3)
