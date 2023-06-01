# ----- Recursion -----
def uniquePaths(r, c):
    if r == 1 or c == 1:
        return 1
    return uniquePaths(r - 1, c) + uniquePaths(r, c - 1)


# ----- Memoization -----
def uniquePaths(r, c, memo=None):
    rIdx = r - 1
    cIdx = c - 1

    if not memo:
        memo = [([-1] * c) for i in range(r)]

    if memo[rIdx][cIdx] != -1:
        return memo[rIdx][cIdx]
    elif r == 1 or c == 1:
        memo[rIdx][cIdx] = 1
    else:
        memo[rIdx][cIdx] = uniquePaths(r - 1, c, memo) + uniquePaths(r, c - 1, memo)
    return memo[rIdx][cIdx]


# ----- Tabulation -----
def uniquePaths(r, c):
    table = createTable(r, c)
    print(table)
    for i in range(1, r):
        for j in range(1, c):
            table[i][j] = table[i - 1][j] + table[i][j - 1]

    return table[r - 1][c - 1]


def createTable(rows, columns):
    table = []

    for i in range(rows):
        row = [0] * columns
        row[0] = 1
        table.append(row)

    for j in range(columns):
        table[0][j] = 1

    return table


print(uniquePaths(2, 2))
