"""
matrix, represents the elements in each cell of the matrix of size N*M.
"""


def funcHopSkipJump(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    top = 0
    left = 0
    bottom = rows - 1
    right = columns - 1

    while True:
        # top
        if top > bottom:
            break
        else:
            topCurrent = top
            for i in range(top, bottom, 2):
                topCurrent += 2

            if topCurrent > bottom:
                left += 1
            top += 1

        # left
        if right < left:
            break
        else:
            leftCurrent = left
            for i in range(left, right, 2):
                leftCurrent += 2

            if leftCurrent > right:
                bottom -= 1
            left += 1

        # bottom
        if top > bottom:
            break
        else:
            bottomCurrent = bottom
            for i in range(bottom, top, -2):
                bottomCurrent -= 2

            if bottomCurrent <= top:
                right -= 1
            bottom -= 1

        # right
        if right < left:
            break
        else:
            rightCurrent = right
            for i in range(right, left, -2):
                rightCurrent -= 2

            if rightCurrent <= left:
                left += 1
            right -= 1

        return matrix[top][left - 1]

    return


def main():
    # input for matrix
    matrix = []
    matrix_rows, matrix_cols = map(int, input().split())
    for idx in range(matrix_rows):
        matrix.append(list(map(int, input().split())))

    result = funcHopSkipJump(matrix)
    print(result)


if __name__ == "__main__":
    main()
