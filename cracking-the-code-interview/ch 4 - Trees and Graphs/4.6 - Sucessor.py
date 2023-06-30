from MinimalTree import *


def successor(root):
    if root.right == None:
        given = root.value
        root = root.parent
        while root.value < given:
            if root.parent == None:
                return None
            root = root.parent
    else:
        root = root.right
        while root.left != None:
            root = root.left
    return root


valid = [1, 3, 4, 5, 6, 7, 8]
root = binaryTree(valid)
print(successor(root).value)
