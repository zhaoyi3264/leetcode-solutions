# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = float('-inf')
    
    def maxPathSum(self, root: TreeNode) -> int:    
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            self.ans = max(self.ans, max(l, 0) + max(r, 0) + root.val)
            return max(l, r, 0) + root.val
        dfs(root)
        return self.ans
