from Tree import TreeNode


def binaryTree(arr):
    return helper(arr, 0, len(arr) - 1, None)


def helper(arr, left, right, parent):
    node = None
    if left <= right:
        mid = (left + right) // 2
        node = TreeNode(arr[mid])
        node.left = helper(arr, left, mid - 1, node)
        node.right = helper(arr, mid + 1, right, node)
        node.parent = parent
    return node


def inOrder(node):
    if node != None:
        inOrder(node.left)
        print(node.value)
        inOrder(node.right)
