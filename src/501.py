# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = -1
    prev_count = 0
    max_count = -1
    ans = []
    
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        
        if root.val == self.prev:
            self.prev_count += 1
        else:
            self.prev_count = 1
            self.prev = root.val
        
        if self.prev_count == self.max_count:
            self.ans.append(self.prev)
        elif self.prev_count > self.max_count:
            self.ans.clear()
            self.ans.append(self.prev)
            self.max_count = self.prev_count
        
        self.inorder(root.right)
    
    def findMode(self, root: TreeNode) -> List[int]:
        self.ans.clear()
        self.inorder(root)
        return self.ans
