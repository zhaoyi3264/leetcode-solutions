# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_leaves(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return self.get_leaves(root.left) + self.get_leaves(root.right)
    
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        l1 = self.get_leaves(root1)
        l2 = self.get_leaves(root2)
        # print(l1, l2)
        return l1 == l2
