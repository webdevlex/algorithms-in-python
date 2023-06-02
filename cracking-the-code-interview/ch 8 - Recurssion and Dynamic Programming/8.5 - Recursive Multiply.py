# # ----- Naive -----
# def recursiveMultiply(n, m):
#     if n == 0:
#         return 0
#     return recursiveMultiply(n - 1, m) + m


# # ----- Better -----
# def recursiveMultiply(n, m):
#     smaller = min(n, m)
#     bigger = max(n, m)

#     if smaller == 0:
#         return 0
#     elif smaller == 1:
#         return bigger

#     halfSmaller = smaller >> 1
#     side1 = recursiveMultiply(halfSmaller, bigger)
#     side2 = side1
#     if n % 2 == 1:
#         side2 = recursiveMultiply(smaller - halfSmaller, bigger)
#     return side1 + side2


# ----- Best -----
def recursiveMultiply(n, m, memo={}):
    smaller = min(n, m)
    bigger = max(n, m)

    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger
    elif n in memo:
        return memo[n]

    halfSmaller = smaller >> 1  # Compute half
    side1 = recursiveMultiply(halfSmaller, bigger)
    side2 = side1
    if n % 2 == 1:  # If uneven, compute other half.
        memo[n] = side1 + side2 + bigger
    else:
        memo[n] = side1 + side2

    return memo[n]  # If even, double it


print(recursiveMultiply(9, 7))
