import math
from MinimalTree import *


def validateVST(root):
    return helper(root, -math.inf, math.inf)


def helper(root, min, max):
    if root == None:
        return True

    if min <= root.value and root.value < max:
        leftValid = helper(root.left, min, root.value)
        rightValid = helper(root.right, root.value, max)

        if leftValid and rightValid:
            return True

    return False


invalid = [1, 3, 6, 5, 6, 8, 9]
root = binaryTree(invalid)
print(validateVST(root))

valid = [1, 3, 4, 5, 6, 7, 8]
root = binaryTree(valid)
print(validateVST(root))
