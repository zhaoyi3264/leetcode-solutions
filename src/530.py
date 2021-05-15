# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = -float('inf')
    ans = float('inf')
    
    def getMinimumDifference(self, root: TreeNode) -> int:
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.ans = min(self.ans, root.val - self.prev)
            self.prev = root.val
            inorder(root.right)
        inorder(root)
        return self.ans
