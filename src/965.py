# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, val):
        if not root:
            return True
        if root.val == val:
            return self.helper(root.left, val) and self.helper(root.right, val)
    
    def isUnivalTree(self, root: TreeNode) -> bool:
        return self.helper(root, root.val)
