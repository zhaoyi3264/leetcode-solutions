# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        ans = 'z' * 8500
        offset = ord('a')
        def dfs(root, s):
            nonlocal ans, offset
            
            if not root:
                return
            s = chr(offset + root.val) + s
            if not root.left and not root.right:
                if s < ans:
                    ans = s
                return
            dfs(root.left, s)
            dfs(root.right, s)
        dfs(root, '')
        return ans
