# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if not root:
            return (True, -1)
        l_b, l_h = self.helper(root.left)
        r_b, r_h = self.helper(root.right)
        return l_b and r_b and abs(l_h - r_h) < 2, max(l_h, r_h) + 1
    
    def isBalanced(self, root: TreeNode) -> bool:
        b, h = self.helper(root)
        return b
