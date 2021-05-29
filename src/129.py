# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, s):
        if not root:
            return
        s = s * 10 + root.val
        if not root.left and not root.right:
            self.ans += s
        self.dfs(root.left, s)
        self.dfs(root.right, s)
    
    def sumNumbers(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root, 0)
        return self.ans
