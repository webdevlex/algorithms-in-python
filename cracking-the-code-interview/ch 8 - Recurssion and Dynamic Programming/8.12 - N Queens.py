def nQueens(board):
    helper(board, 0)


def helper(board, column):
    if column >= len(board):
        return True

    for i in range(len(board)):
        if isSafe(board, i, column):
            board[i][column] = 1
            if helper(board, column + 1):
                print(board.copy())
            board[i][column] = 0
    return False


def isSafe(board, row, column):
    boardLength = len(board)

    for i in range(boardLength):
        # Check Row
        if board[row][i] == 1 and i != column:
            return False

        # Check Column
        if board[i][column] == 1 and i != row:
            return False

        # Check diag toward Top Left
        if row - i >= 0 and column - i >= 0 and board[row - i][column - i] == 1:
            return False

        # Check diag toward Bottom Right
        if (
            row + i < boardLength
            and column + i < boardLength
            and board[row + i][column + i] == 1
        ):
            return False

        # Check diag toward Bottom Left
        if (
            row + i < boardLength
            and column - i >= 0
            and board[row + i][column - i] == 1
        ):
            return False

        # Check diag toward Top Right
        if (
            row - i >= 0
            and column + i < boardLength
            and board[row - i][column + i] == 1
        ):
            return False

    return True


def printFormatted(board):
    for row in board:
        print(row)

    print()


board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
nQueens(board)
