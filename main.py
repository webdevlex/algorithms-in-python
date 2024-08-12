from collections import deque


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def preOrder(self, root):
        if not root:
            return None

        print(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        if not root:
            return None

        self.inOrder(root.left)
        print(root.val)
        self.inOrder(root.right)

    def postOrder(self, root):
        if not root:
            return None

        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.val)

    def bfs(self, root):
        q = deque([root])

        while q:
            for i in range(len(q)):
                curr = q.popleft()
                print(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

    def iterativeInOrder(self, root):
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            print(curr.val)
            curr = curr.right

    def iterativePreOrder(self, root):
        stack = []
        curr = root

        while stack or curr:
            while curr:
                print(curr.val)
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            curr = curr.right

    def iterativePostOrder(self, root):
        if not root:
            return

        stack = []
        last_visited = None

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            peek_node = stack[-1]
            if peek_node.right and last_visited != peek_node.right:
                root = peek_node.right
            else:
                print(peek_node.val)
                last_visited = stack.pop()


root = Node(11, Node(5, Node(4), Node(8)), Node(16, Node(14), Node(19)))

tree = Tree()
# tree.preOrder(root)
# tree.inOrder(root)
# tree.postOrder(root)
# tree.bfs(root)
# tree.iterativeInOrder(root)
# tree.iterativePreOrder(root)
tree.iterativePostOrder(root)
