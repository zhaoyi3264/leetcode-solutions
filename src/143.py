# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cur = head
        res = []
        while cur:
            nxt = cur.next
            cur.next = None
            res.append(cur)
            cur = nxt
        length = len(res)
        if length < 2:
            return
        head.next = res[-1]
        cur = head.next
        for i in range(1, length//2):
            cur.next = res[i]
            cur.next.next = res[-1-i]
            cur = cur.next.next
        if length % 2:
            cur.next = res[length//2]
