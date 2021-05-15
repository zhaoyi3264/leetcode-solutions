"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return
        ans = []
        for child in root.children:
            for cc in self.postorder(child):
                ans.append(cc)
        ans.append(root.val)
        return ans
