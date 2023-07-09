from Tree import TreeNode


def pathWithSum(root, num):
    sumTable = {0: 1}
    return helper(root, num, 0, sumTable)


def helper(root, num, runningSum, sumTable):
    if root == None:
        return 0

    runningSum += root.value
    requiredNum = runningSum - num
    currentCount = sumTable[requiredNum] if requiredNum in sumTable else 0

    if runningSum in sumTable:
        sumTable[runningSum] += 1
    else:
        sumTable[runningSum] = 1

    print(f"current: {root.value}")
    print(f"running: {runningSum}")
    print(f"table: ", sumTable)
    print(f"requiredNum ", requiredNum)
    print("")

    leftCount = helper(root.left, num, runningSum, sumTable)
    rightCount = helper(root.right, num, runningSum, sumTable)
    sumTable[runningSum] -= 1

    return currentCount + leftCount + rightCount


root = TreeNode(
    1,
    TreeNode(2, TreeNode(3)),
)

print(pathWithSum(root, 6))
