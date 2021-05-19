# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def mirror(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return a.val == b.val and mirror(a.left, b.right) and mirror(a.right, b.left)
        return mirror(root, root)
