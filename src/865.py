# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(root, d):
            if not root:
                return (root, d)
            
            l, l_d = dfs(root.left, d + 1)
            r, r_d = dfs(root.right, d + 1)
            
            if l_d > r_d:
                return (l, l_d)
            elif l_d < r_d:
                return (r, r_d)
            else:
                return (root, l_d)
            
        return dfs(root, -1)[0]
