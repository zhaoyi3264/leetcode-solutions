# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        maxs = []
        if not root:
            return maxs
        q = deque([root])
        while q:
            m = float('-inf')
            for _ in range(len(q)):
                node = q.popleft()
                m = max(m, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            maxs.append(m)
        return maxs
