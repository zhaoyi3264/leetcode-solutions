# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k):
        stack = []
        while k:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop(-1)
            k -= 1
            root = node.right
        return node.val
