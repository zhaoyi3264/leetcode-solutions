# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        root.val = 0
        self.s = set()
        self.helper(root)
        
    def helper(self, root):
        if not root:
            return None
        self.s.add(root.val)
        if root.left:
            root.left.val = 2 * root.val + 1
            self.s.add(root.left.val)
            self.helper(root.left)
        if root.right:
            root.right.val = 2 * root.val + 2
            self.s.add(root.right.val)
            self.helper(root.right)

    def find(self, target: int) -> bool:
        return target in self.s

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
