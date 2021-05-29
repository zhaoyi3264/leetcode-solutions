# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import lru_cache
class Solution:
    ans = -1
    
    def dfs(self, root):
        if not root:
            return -1, -1
        l_l, l_r = self.dfs(root.left)
        r_l, r_r = self.dfs(root.right)

        self.ans = max(self.ans, l_l, l_r, r_l, r_r)
        return (l_r + 1, r_l + 1)
    
    def longestZigZag(self, root: TreeNode) -> int:
        # if not root:
        #     return 0
        # @lru_cache(512)
        # def dfs(root, direct):
        #     if not root:
        #         return 0
        #     if direct == -1:
        #         return int(root.left != None) + dfs(root.left, direct * -1)
        #     else:
        #         return int(root.right != None) + dfs(root.right, direct * -1)
        # return max(dfs(root, -1), dfs(root, 1), self.longestZigZag(root.left), self.longestZigZag(root.right))
        
        dummy = TreeNode(-1, root)
        self.dfs(dummy)
        return self.ans
