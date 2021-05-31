# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # def inorder(root):
        #     if not root:
        #         return []
        #     return [*inorder(root.left), root.val, *inorder(root.right)]
        # res = inorder(root)
        # for i in range(1, len(res)):
        #     if res[i - 1] >= res[i]:
        #         return False
        # return True
        def validate(root, low, high):
            if not root:
                return True
            return (not root.left or validate(root.left, low, root.val)) \
                and (low < root.val < high) \
                and (not root.right or validate(root.right, root.val, high))
        return validate(root, -float('inf'), float('inf'))
