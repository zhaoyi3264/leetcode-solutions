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
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        self.head = head
        cur = head
        n = 0
        while cur:
            n += 1
            cur = cur.next
        def build(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            left = build(l, mid - 1)
            val = self.head.val
            self.head = self.head.next
            right = build(mid + 1, r)
            return TreeNode(val, left, right)
        return build(0, n - 1)
        
