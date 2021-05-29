# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        level, stack = 0, [(root, 1)]
        while stack:
            node, lv = stack.pop()
            if node:
                level = max(level, lv)
                stack.append((node.left, lv + 1))
                stack.append((node.right, lv + 1))
                
        rows = [[''] * ((2 ** level) - 1) for _ in range(level)]
        
        q = deque([(root, 0, 0, (2 ** level) - 2)])
        while q:
            node, i, l, r = q.popleft()
            if node:
                m = (l + r) // 2
                rows[i][m] = str(node.val)
                q.append((node.left, i + 1, l, m - 1))
                q.append((node.right, i + 1, m + 1, r))
        return rows

