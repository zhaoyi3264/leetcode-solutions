# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        i = 0
        
        while post[i] != pre[1]:
            i += 1
        i += 1
        root.left = self.constructFromPrePost(pre[1:i+1], post[:i])
        root.right = self.constructFromPrePost(pre[i+1:], post[i:-1])
        return root
