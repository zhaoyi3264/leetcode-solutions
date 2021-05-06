# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        cur = head
        n = 0
        while cur:
            n += 1
            cur = cur.next
        if k > n // 2:
            k = n + 1 - k
        a = b = None
        cur = head
        for i in range(1, n - k + 2):
            if i == k:
                a = cur
            b = cur
            cur = cur.next
        a.val, b.val = b.val, a.val
        return head
