def helper(amount, denoms, index):
    if index >= len(denoms) - 1:
        return 1  # last denom
    denomAmount = denoms[index]
    ways = 0
    for i in range(amount // denomAmount + 1):
        amountRemaining = amount - i * denomAmount
        print(denomAmount)
        ways += helper(amountRemaining, denoms, index + 1)

    return ways


def makeChange(n):
    denoms = [25, 10, 5, 1]
    return helper(n, denoms, 0)


print(makeChange(4))
