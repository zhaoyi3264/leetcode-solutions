# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def dfs(root, target):
            if root.left:
                root.left = dfs(root.left, target)
            if root.right:
                root.right = dfs(root.right, target)
            
            if not root.left and not root.right and root.val == target:
                return None    
            return root
        dummy = TreeNode(0, root)
        return dfs(dummy, target).left
