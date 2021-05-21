# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    good = 0
    
    def dfs(self, root, m):
        if not root:
            return
        if root.val >= m:
            self.good += 1
            m = root.val
        self.dfs(root.left, m)
        self.dfs(root.right, m)
        
    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, float('-inf'))
        return self.good
