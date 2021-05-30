# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        def dfs(root, path_sum, path):
            if not root:
                return
            if not root.left and not root.right and (path_sum + root.val == targetSum):
                res.append([*path])
            if root.left:
                path.append(root.left.val)
                dfs(root.left, path_sum + root.val, path)
                path.pop(-1)
            if root.right:
                path.append(root.right.val)
                dfs(root.right, path_sum + root.val, path)
                path.pop(-1)
                
        dfs(root, 0, [root.val])
        return res
