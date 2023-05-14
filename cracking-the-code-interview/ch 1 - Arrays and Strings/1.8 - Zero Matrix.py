def zeroMatrix(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return matrix

    m = len(matrix)
    n = len(matrix[0])

    rows = [False] * m
    columns = [False] * n

    for rowIdx in range(m):
        for columnIdx in range(n):
            if matrix[rowIdx][columnIdx] == 0:
                rows[rowIdx] = True
                columns[columnIdx] = True

    for rowIdx in range(m):
        if rows[rowIdx]:
            fillRow(rowIdx, matrix)

    for columnIdx in range(n):
        if columns[columnIdx]:
            fillColumn(columnIdx, matrix)

    return matrix


def fillRow(rowIdx, matrix):
    for columnIdx in range(len(matrix[0])):
        matrix[rowIdx][columnIdx] = 0


def fillColumn(columnIdx, matrix):
    for rowIdx in range(len(matrix)):
        matrix[rowIdx][columnIdx] = 0


def printFormatted(matrix):
    for arr in matrix:
        print(arr)


input = [[1, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
print(f"\ninput:")
printFormatted(input)

output = zeroMatrix(input)
print(f"\noutput:")
printFormatted(output)
