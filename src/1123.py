# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(root, d):
            if not root:
                return (None, d)
            d += 1
            l_n, l_d = dfs(root.left, d)
            r_n, r_d = dfs(root.right, d)
            if l_d > r_d:
                return (l_n, l_d)
            elif l_d < r_d:
                return (r_n, r_d)
            else:
                return (root, l_d)
        return dfs(root, 0)[0]
