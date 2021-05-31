# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        res = defaultdict(list)
        q = [(root, 0)]
        min_col = max_col = 0
        while q:
            q.sort(key=lambda x: (x[1], x[0].val))
            min_col = min(min_col, q[0][1])
            max_col = max(max_col, q[-1][1])
            prev_q, q = q, []
            for node, col in prev_q:
                res[col].append(node.val)
                if node.left:
                    q.append((node.left, col - 1))
                if node.right:
                    q.append((node.right, col + 1))

        return [res[col] for col in range(min_col, max_col+1)]

