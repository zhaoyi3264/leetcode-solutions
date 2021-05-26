# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    d = {}
    
    def update(self, root):
        if not root:
            return 0
        l = self.update(root.left)
        r = self.update(root.right)
        s = root.val + l + r
        self.d[s] = self.d.get(s, 0) + 1
        return s
    
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        self.d = {}
        self.update(root)
        l = []
        m = -1
        for k, v in self.d.items():
            if v > m:
                l.clear()
                l.append(k)
                m = v
            elif v == m:
                l.append(k)
        return l
            
