from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def recure(root, subRoot):
            if not root and not subRoot:
                return True
            elif (not root and subRoot) or (root and not subRoot):
                return False

            leftRes = recure(root.left, subRoot.left)
            rightRes = recure(root.right, subRoot.right)

            return leftRes and rightRes and root.val == subRoot.val

        if not root or not subRoot: 
            return False
        elif root.val == subRoot.val:
            if recure(root, subRoot):
                return True
        
        searchLeft = self.isSubtree(root.left, subRoot)
        searchRight = self.isSubtree(root.right, subRoot)

        return searchLeft or searchRight