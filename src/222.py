# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def left_h(root):
            height = 0
            while root:
                root = root.left
                height += 1
            return height
        
        def right_h(root):
            height = 0
            while root:
                root = root.right
                height += 1
            return height
        
        def get_nodes(root):
            l_h = left_h(root)
            r_h = right_h(root)
            if l_h == r_h:
                return 2**l_h - 1
            return get_nodes(root.left) + get_nodes(root.right) + 1
        
        return get_nodes(root)
