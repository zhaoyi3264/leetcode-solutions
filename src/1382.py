# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def construct(self, l):
        if not l:
            return None
        mid = len(l) // 2
        root = l[mid]
        root.left = self.construct(l[:mid])
        root.right = self.construct(l[mid+1:])
        return root
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            l.append(root)
            inorder(root.right)
        l = []
        inorder(root)
        return self.construct(l)
