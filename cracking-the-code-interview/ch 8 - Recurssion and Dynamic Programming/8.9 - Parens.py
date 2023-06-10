# def parens(n):
#     if n == 1:
#         return ["()"]

#     result = []
#     combos = parens(n - 1)
#     for combo in combos:
#         i = 0
#         while combo[i] != ")":
#             result.append(combo[:i] + "()" + combo[i:])
#             i += 1
#         result.append(combo[:i] + "()" + combo[i:])
#     return result


def parens(n):
    combo = [""] * (n * 2)
    result = []
    helper(result, n, n, combo, 0)
    return result


def helper(result, leftRem, rightRem, combo, idx):
    if leftRem < 0 or rightRem < leftRem:
        return

    if leftRem == 0 and rightRem == 0:
        result.append("".join(combo))
    else:
        combo[idx] = "("
        helper(result, leftRem - 1, rightRem, combo, idx + 1)

        combo[idx] = ")"
        helper(result, leftRem, rightRem - 1, combo, idx + 1)


print(parens(3))
