from Tree import TreeNode
import math


# ---------------- Solution 1 --------------------
def getHeight(root):
    if root is None:
        return -1  # Base case
    return max(getHeight(root.left), getHeight(root.right)) + 1


def checkBalanced(root):
    if root is None:
        return True  # Base case

    height_diff = getHeight(root.left) - getHeight(root.right)
    if abs(height_diff) > 1:
        return False
    else:
        return checkBalanced(root.left) and checkBalanced(root.right)


# ---------------- Solution 2 --------------------
def checkBalanced(root):
    return helper(root) != -math.inf


def helper(root):
    if root == None:
        return 0

    leftHeight = helper(root.left)
    if leftHeight == -math.inf:
        return -math.inf

    rightHeight = helper(root.right)
    if rightHeight == -math.inf:
        return -math.inf

    print(leftHeight, rightHeight)
    if abs(leftHeight - rightHeight) > 1:
        return -math.inf

    return max(leftHeight, rightHeight) + 1


root = TreeNode(0, TreeNode(1))
print(checkBalanced(root))
