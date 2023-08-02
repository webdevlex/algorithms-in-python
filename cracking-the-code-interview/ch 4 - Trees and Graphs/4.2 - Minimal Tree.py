# Minimal Tree: Given a sorted (increasing order) array with unique integer
# elements, write an algorithm to create a binary search tree with minimal height.


from Tree import Node


def binaryTree(arr):
    return helper(arr, 0, len(arr) - 1, None)


def helper(arr, left, right, parent):
    node = None
    if left <= right:
        mid = (left + right) // 2
        node = Node(arr[mid])
        node.left = helper(arr, left, mid - 1, node)
        node.right = helper(arr, mid + 1, right, node)
        node.parent = parent
    return node


def inOrder(node):
    if node != None:
        inOrder(node.left)
        print(node.value)
        inOrder(node.right)


arr = [1, 2, 3, 4, 5]
root = binaryTree(arr)
inOrder(root)
