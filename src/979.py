# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    
    def distributeCoins(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            e = root.val + l + r - 1
            self.ans += abs(l) + abs(r)
            return e
        dfs(root)
        return self.ans
