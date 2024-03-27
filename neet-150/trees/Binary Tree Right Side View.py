from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        que = []
        if root:
            que.append(root)

        res = []
        while que:
            level = []

            for i in range(len(que)):
                current = que.pop()
                level.append(current)

                if current.left:
                    que.append(current.left)
                if current.right:
                    que.append(current.right)
            res.append(level[-1])
        return res

                
