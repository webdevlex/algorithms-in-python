from LinkedList import Node
from MinimalTree import *


def listOfDepth(root):
    result = []
    helper(root, result, 0)
    result.pop()
    return result


def helper(root, result, level):
    if len(result) == level:
        result.append(None)

    if root != None:
        node = Node(root.value, result[level])
        print(f"adding {root.value} to level {level}")
        result[level] = node
        helper(root.left, result, level + 1)
        helper(root.right, result, level + 1)


nodes = [3, 1, 2, 0, 5, 2, 6]
root = binaryTree(nodes)
listOfDepth = listOfDepth(root)
print(listOfDepth)

for linkedList in listOfDepth:
    while linkedList != None:
        print(f"{linkedList.value} -> ", end="")
        linkedList = linkedList.next
    print()
