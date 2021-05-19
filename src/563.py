# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sum(self, root):
        if not root:
            return 0
        l = self.sum(root.left)
        r = self.sum(root.right)
        root.val += (l + r)
        return root.val
    
    def tilt(self, root):
        if not root:
            return
        if not root.left and not root.right:
            root.val = 0
        l = root.left.val if root.left else 0
        r = root.right.val if root.right else 0
        root.val = abs(l - r)
        
        self.tilt(root.left)
        self.tilt(root.right)
        
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.sum(root)
        self.tilt(root)
        self.sum(root)
        # print(root)
        return root.val
