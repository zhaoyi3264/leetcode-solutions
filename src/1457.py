# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        d = dict.fromkeys(range(0, 10), 0)
        def check(d):
            odd = sum(map(lambda v: v % 2 == 1, d.values()))
            return odd < 2
        
        def dfs(root, d):
            if not root:
                return
            d[root.val] += 1
            if not root.left and not root.right:
                if check(d):
                    self.ans += 1
                d[root.val] -= 1
            else:
                dfs(root.left, d)
                dfs(root.right, d)
                d[root.val] -= 1
        dfs(root, d)
        return self.ans
