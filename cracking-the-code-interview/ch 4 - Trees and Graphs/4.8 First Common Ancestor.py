from MinimalTree import *


def firstComonAncestor(n1, n2):
    if search(n1, n2):
        return n1
    elif search(n2, n1):
        return n2

    current = n1
    parent = current.parent
    while parent != None:
        commonParentFound = False

        if current == parent.left:
            commonParentFound = search(parent.right, n2)
        else:
            commonParentFound = search(parent.left, n2)

        if commonParentFound:
            return parent

        current = parent
        parent = parent.parent

    return None


def search(root, nodeToFind):
    if root == None:
        return False
    elif root == nodeToFind:
        return True

    left = search(root.left, nodeToFind)
    right = search(root.right, nodeToFind)

    return left or right


valid = [1, 3, 4, 5, 6, 7, 8]
root = binaryTree(valid)
n1 = root.left.left
n2 = root.left.right
print(firstComonAncestor(n1, n2).value)
