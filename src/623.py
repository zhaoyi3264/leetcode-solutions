# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            return TreeNode(val, root)
        
        p_l = [root]
        d = 1
        while p_l:
            d += 1
            if d == depth:
                for i, n in enumerate(p_l):
                    if n:
                        l = 2 * i
                        r = 2 * i + 1
                        n.left = TreeNode(val, left=n.left)
                        n.right = TreeNode(val, right=n.right)
                return root
            
            n_l = []
            for n in p_l:
                if n:
                    n_l.append(n.left)
                    n_l.append(n.right)
            
            p_l = n_l
