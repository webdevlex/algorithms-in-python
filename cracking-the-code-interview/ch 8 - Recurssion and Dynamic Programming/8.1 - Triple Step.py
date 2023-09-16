# Triple Step: A child is running up a staircase with n steps and can hop either
# 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible
# ways the child can run up the stairs.


# Recurssion
def tripleStep(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return tripleStep(n - 1) + tripleStep(n - 2) + tripleStep(n - 3)


# ----- Memoization -----
def tripleStep(n, memo={}):
    if n in memo:
        return memo[n]

    if n < 0:
        memo[n] = 0
    elif n == 0:
        memo[n] = 1
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
