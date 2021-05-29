# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(root):
            if not root:
                return 0, []
            if not root.right and not root.left:
                return 0, [0]
            
            l, llist = dfs(root.left)
            r, rlist = dfs(root.right)
            if not root.left:
                return r, [x + 1 for x in rlist]
            if not root.right:
                return l, [x + 1 for x in llist]
            
            temp = 0
            for x in llist:
                for y in rlist:
                    temp += x + y + 2 <= distance
            return r + l + temp, [x + 1 for x in llist] + [y + 1 for y in rlist]
        
        return dfs(root)[0]
