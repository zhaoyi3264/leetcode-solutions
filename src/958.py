# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        q = deque([root])
        none = False
        while q:
            node = q.popleft()
            if node.left:
                if none:
                    return False
                else:
                    q.append(node.left)
            else:
                none = True
            if node.right:
                if none:
                    return False
                else:
                    q.append(node.right)
            else:
                none = True
        return True
