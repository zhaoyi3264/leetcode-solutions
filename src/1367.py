# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def check(self, head, root):
        if not head:
            return True
        elif head and root and head.val == root.val:
            return self.check(head.next, root.left) or self.check(head.next, root.right)
        else:
            return False
    
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if head and root and head.val == root.val and self.check(head, root):
            return True
        elif head and not root:
            return False
        elif not head and root:
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
