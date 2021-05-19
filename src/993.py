# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = deque([(None, 0, root)])
        x_parent = None
        y_parent = None
        x_level = 0
        y_level = 0
        
        while q:
            n = len(q)
            for i in range(n):
                node_parent, level, node = q.popleft()
                if node.val == x:
                    x_parent = node_parent
                    x_level = level
                if node.val == y:
                    y_parent = node_parent
                    y_level = level
                if x_parent and y_parent:
                    return x_parent is not y_parent and x_level == y_level
                if node.left:
                    q.append((node, level + 1, node.left))
                if node.right:
                    q.append((node, level + 1, node.right))
        return False
