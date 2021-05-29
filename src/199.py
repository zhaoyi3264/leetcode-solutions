# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        view = []
        q = deque([root])
        while q:
            for _ in range(len(q)):
                last = q.popleft()
                if last.left:
                    q.append(last.left)
                if last.right:
                    q.append(last.right)
            view.append(last.val)
        return view
