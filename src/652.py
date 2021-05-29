# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def preorder(root):
            if root == None:
                return '#'
            s = f'{str(root.val)} {preorder(root.left)} {preorder(root.right)}'
            if self.d[s] == 1:
                self.ans.append(root)
            self.d[s] += 1
            return s
        self.d = defaultdict(int)
        self.ans = []
        preorder(root)
        return self.ans
