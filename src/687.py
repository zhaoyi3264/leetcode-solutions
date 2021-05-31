# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, root):
        if not root:
            return
        self.check(root, root.val)
        self.dfs(root.left)
        self.dfs(root.right)
        
    def check(self, root, p_val):
        if root and root.val == p_val:
            l = self.check(root.left, root.val)
            r = self.check(root.right, root.val)
            self.ans = max(self.ans, l + r + 1)
            return max(l, r) + 1
        else:
            return 0
    
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans - 1 if self.ans else 0
