# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root, subRoot):
        if not root and not subRoot:
            return True
        elif root and subRoot and root.val == subRoot.val:
            return self.check(root.left, subRoot.left) and self.check(root.right, subRoot.right)
        else:
            return False
    
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root and not subRoot:
            return True
        elif root and subRoot:
            if self.check(root, subRoot):
                return True
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return False
