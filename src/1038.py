# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    s = 0
    def update(self, root):
        if not root:
            return 0
        self.update(root.right)
        self.s += root.val
        root.val = self.s
        self.update(root.left)
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.update(root)
        return root
