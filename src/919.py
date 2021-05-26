# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.tree = []
        self.levelorder(root)
    
    def levelorder(self, root):
        q = deque([root])
        while q:
            node = q.popleft()
            self.tree.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, v: int) -> int:
        child = TreeNode(v)
        parent = self.tree[(len(self.tree) - 1) // 2]
        self.tree.append(child)
        if len(self.tree) % 2:
            parent.right = child
        else:
            parent.left = child
        return parent.val

    def get_root(self) -> TreeNode:
        return self.tree[0]


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
