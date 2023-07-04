from MinimalTree import *


def checkSubtree(t1, t2):
    if t1 == None and t2 == None:
        return True
    if t1 == None:
        return False
    elif t1.value == t2.value:
        if areEqual(t1, t2):
            return True

    leftHasMatch = checkSubtree(t1.left, t2)
    rightHasMatch = checkSubtree(t1.right, t2)

    return leftHasMatch or rightHasMatch


def areEqual(root1, root2):
    if root1 == None and root2 == None:
        return True
    elif root1 == None and root2 != None:
        return False
    elif root2 != None and root2 == None:
        return False

    leftSame = areEqual(root1.left, root2.left)
    if root1.value != root2.value:
        return False
    rightSame = areEqual(root1.right, root2.right)

    return leftSame and rightSame


tree1 = [1, 3, 4, 5, 6, 7, 8]
t1 = binaryTree(tree1)

tree2 = [6, 7, 8]
t2 = binaryTree(tree2)

print(checkSubtree(t1, t2))
