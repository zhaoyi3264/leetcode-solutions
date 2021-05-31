# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxProduct(self, root: TreeNode) -> int:
        self.total = 0
        self.sub = set()
        
        def dfs(root):
            if not root:
                return 0
            self.total += root.val
            l = dfs(root.left)
            r = dfs(root.right)
            s = root.val + l + r
            self.sub.add(s)
            return s
        
        dfs(root)
        ans = -1
        for s in self.sub:
            ans = max(ans, s * (self.total - s))
        return ans % (1_000_000_007)
