# Recurssion
def tripleStep(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return tripleStep(n - 1) + tripleStep(n - 2) + tripleStep(n - 3)


# ----- Memoization -----
def tripleStep(n, memo={}):
    if n in memo:
        return memo[n]

    if n == 1:
        memo[n] = 1
    elif n == 2:
        memo[n] = 2
    elif n == 3:
        memo[n] = 4
    else:
        memo[n] = (
            tripleStep(n - 1, memo) + tripleStep(n - 2, memo) + tripleStep(n - 3, memo)
        )
    return memo[n]


def tripleStep(n):
    table = [0] * n
    table[0] = 1
    table[1] = 2
    table[2] = 4
    for i in range(3, n):
        table[i] = table[i - 1] + table[i - 2] + table[i - 3]
    return table[n - 1]


print(tripleStep(30))
