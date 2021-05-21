# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import lru_cache

class Solution:
    @lru_cache()
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n % 2 == 0:
            return []
        elif n == 1:
            return [TreeNode(0)]
        
        ans = []
        for l in range(1, n, 2):
            r = n - 1 - l
            for lt in self.allPossibleFBT(l):
                for rt in self.allPossibleFBT(r):
                    root = TreeNode(0, lt, rt)
                    ans.append(root)
        return ans
