# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        def dfs(root, path):
            if not root:
                return
            if not root.left and not root.right:
                path.append(str(root.val))
                paths.append('->'.join(path))
                path.pop(-1)
            else:
                path.append(str(root.val))
                dfs(root.left, path)
                dfs(root.right, path)
                path.pop(-1)
        dfs(root, [])
        return paths
