# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def helper(root, mini, maxi):
            if not root:
                return maxi - mini
            mini = min(mini, root.val)
            maxi = max(maxi, root.val)
            l = helper(root.left, mini, maxi)
            r = helper(root.right, mini, maxi)
            return max(l, r)
        
        return helper(root, root.val, root.val)
