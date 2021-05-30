# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left and root.right:
                succ = root.right
                while succ.left:
                    succ = succ.left
                root.val = succ.val
                root.right = self.deleteNode(root.right, succ.val)
            else:
                return root.left or root.right
        return root
