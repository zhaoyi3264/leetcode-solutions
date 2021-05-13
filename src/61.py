# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        prev = None
        cur = head
        n = 0
        while cur:
            n += 1
            prev = cur
            cur = cur.next
        tail = prev
        tail.next = head
        
        rot = (n - k) % n
        for _ in range(rot):
            head = head.next
            tail = tail.next
        tail.next = None
        return head
