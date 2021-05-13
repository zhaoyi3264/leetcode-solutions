# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        cur = head
        res = []
        while cur:
            nxt = cur.next
            cur.next = None
            res.append(cur)
            cur = nxt
        cur = dummy = ListNode()
        for n in sorted(res, key=lambda node: node.val):
            cur.next = n
            cur = cur.next
        return dummy.next
