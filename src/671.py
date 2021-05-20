# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if root is None:
            return
        s = set()
        if root.left:
            s.update(self.helper(root.left))
        s.add(root.val)
        if root.right:
            s.update(self.helper(root.right))
        return sorted(s)
    
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        s = self.helper(root)
        return s[1] if len(s) > 1 else -1
