from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallestRecursive(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(root, res=[]):
            if not root:
                return res
            
            res = inOrder(root.left, res)
            res.append(root.val)
            res = inOrder(root.right, res)

            return res
        
        res = inOrder(root)
        return res[k]
    
    def kthSmallestIterative(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right