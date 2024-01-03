from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif (not p and q) or (p and not q):
            return False
        
        leftSame = self.isSameTree(p.left, q.left)
        rightSame = self.isSameTree(p.right, q.right)

        return leftSame and rightSame and p.val == q.val