def rotateMatrix(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False

    layers = len(matrix) // 2
    for i in range(layers):
        endIdx = len(matrix) - 1 - i
        for j in range(i, endIdx):
            offset = j - i
            temp = matrix[i][j]
            matrix[i][j] = matrix[endIdx - offset][i]
            matrix[endIdx - offset][i] = matrix[endIdx][endIdx - offset]
            matrix[endIdx][endIdx - offset] = matrix[j][endIdx]
            matrix[j][endIdx] = temp
    return matrix


def printFormatted(matrix):
    for arr in matrix:
        print(arr)


input = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
print(f"\ninput:")
printFormatted(input)

output = rotateMatrix(input)
print(f"\noutput:")
printFormatted(output)
