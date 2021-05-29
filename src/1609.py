# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        q = deque([root])
        l = 0
        while q:
            p = float('inf') if l % 2 else float('-inf')
            for _ in range(len(q)):
                n = q.popleft()
                if l % 2:
                    if n and (n.val % 2 == 1 or p <= n.val):
                        return False
                else:
                    if n and (n.val % 2 == 0 or p >= n.val):
                        return False
                p = n.val
                
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            l += 1
        return True
