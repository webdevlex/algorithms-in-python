def legos(rowA, rowB):
    rowASum = 0
    rowAZeros = 0
    for num in rowA:
        rowASum += num
        if num == 0:
            rowAZeros += 1

    rowBSum = 0
    rowBZeros = 0
    for num in rowB:
        rowBSum += num
        if num == 0:
            rowBZeros += 1

    if (rowASum != rowBSum) and (rowAZeros == 0 or rowBZeros == 0):
        return -1

    rowAMinSum = rowASum + rowAZeros
    rowBMinSum = rowBSum + rowBZeros
    return max(rowAMinSum, rowBMinSum)


print(legos([1, 0, 2], [1, 3, 0, 0]))
print(legos([2, 5, 0, 1, 1], [2, 1, 0, 0]))
print(legos([0, 0, 0], [1, 1]))
