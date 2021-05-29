# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def count(self, root):
        if not root:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)
    
    def get(self, root, target):
        if not root:
            return None
        if root.val == target:
            return root
        else:
            return self.get(root.left, target) or self.get(root.right, target)
    
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        node = self.get(root, x)
        l = self.count(node.left)
        r = self.count(node.right)
        m = n - l - r - 1
        return max(l, r, m) > n // 2
