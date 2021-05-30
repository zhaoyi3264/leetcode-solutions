# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        a = None
        b = None
        prev = float('inf')
        last = float('-inf')
        def l_r(root):
            nonlocal a, last
            if not root:
                return
            l_r(root.left)
            if root.val < last:
                a = root
            else:
                last = root.val
            l_r(root.right)
        def r_l(root):
            nonlocal b, prev
            if not root:
                return
            r_l(root.right)
            if root.val > prev:
                b = root
            else:
                prev = root.val
            r_l(root.left)
        l_r(root)
        r_l(root)
        a.val, b.val = b.val, a.val
