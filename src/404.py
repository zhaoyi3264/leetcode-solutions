# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def is_leaf(self, root):
        return root and not root.left and not root.right
    
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        s = root.left.val if self.is_leaf(root.left) else 0
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right) + s
