# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum = 0
    
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(root, path_sum):
            if not root:
                return
            path_sum = (path_sum << 1) + root.val
            if not root.left and not root.right:
                self.sum += path_sum
                return
            dfs(root.left, path_sum)
            dfs(root.right, path_sum)
        dfs(root, 0)
        return self.sum
