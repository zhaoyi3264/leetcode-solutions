# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        q = deque([(root, 0)])
        width = 0
        while q:
            begin = None
            for _ in range(len(q)):
                n, pos = q.popleft()
                if n:
                    if begin == None:
                        begin = pos
                    q.append((n.left, 2 * pos))
                    q.append((n.right, 2 * pos + 1))
                    width = max(width, pos - begin + 1)
        return width
