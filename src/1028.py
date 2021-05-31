# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import re

class Solution:
    def construct(self, s, d):
        if not s:
            return None
        regex = r'(?<=\d)-{' + str(d) + '}(?=\d)'
        l = re.split(regex, s)
        root = TreeNode(int(l[0]))
        d += 1
        if len(l) > 1:
            root.left = self.construct(l[1], d)
        if len(l) > 2:
            root.right = self.construct(l[2], d)
        return root
    
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        return self.construct(traversal, 1)
