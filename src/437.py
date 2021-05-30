# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        count = 0
        
        def dfs(root, path):
            if not root:
                return
            nonlocal count
            
            path = [cs + root.val for cs in path]
            path.append(root.val)
            count += path.count(targetSum)
            if root.left:
                dfs(root.left, path.copy())
            if root.right:
                dfs(root.right, path.copy())
        dfs(root, [])
        return count
