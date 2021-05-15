# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = head = TreeNode()
        stack = [root]
        while stack:
            if stack[-1].left:
                stack.append(stack[-1].left)
                stack[-2].left = None    
            else:
                node = stack.pop(-1)
                head.right = node
                head = head.right
                if node.right:
                    stack.append(node.right)  
        return dummy.right
