# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, root, voyage):
        if not root:
            return
        if root.val != voyage[self.idx]:
            self.ans = [-1]
            return
        self.idx += 1
        if root.left and root.left.val != voyage[self.idx]:
            self.ans.append(root.val)
            self.dfs(root.right, voyage)
            self.dfs(root.left, voyage)
        else:
            self.dfs(root.left, voyage)
            self.dfs(root.right, voyage)
    
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.idx = 0
        self.ans = []
        self.dfs(root, voyage)
        return self.ans if -1 not in self.ans else [-1]
