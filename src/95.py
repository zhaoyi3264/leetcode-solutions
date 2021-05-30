# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @lru_cache()
    def helper(self, n, offset):
        if n == 0:
            return [None]
        if n == 1:
            return [TreeNode(1 + offset)]
        
        ans = []
        for l in range(n):
            r = n - 1 - l
            for left in self.helper(l, offset):
                for right in self.helper(r, l + 1 + offset):
                    ans.append(TreeNode(l + 1 + offset, left, right))
        return ans
    
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.helper(n, 0)
