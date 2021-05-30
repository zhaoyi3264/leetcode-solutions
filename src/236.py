# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root:
                return 0
            mid = int(root == p or root == q)
            left = dfs(root.left)
            right = dfs(root.right)
            if left + mid + right >= 2:
                self.ans = root
                return 1
            return left or mid or right
        dfs(root)
        return self.ans
