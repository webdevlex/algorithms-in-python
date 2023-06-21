from Tree import Node


def binaryTree(arr):
    return helper(arr, 0, len(arr) - 1)


def helper(arr, left, right):
    node = None
    if left <= right:
        mid = (left + right) // 2
        node = Node(arr[mid])
        node.left = helper(arr, left, mid - 1)
        node.right = helper(arr, mid + 1, right)
    return node


def inOrder(node):
    if node != None:
        inOrder(node.left)
        print(node.value)
        inOrder(node.right)


arr = [1, 2, 3, 4, 5]
root = binaryTree(arr)
inOrder(root)
