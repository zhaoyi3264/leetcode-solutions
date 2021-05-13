# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        dummy = ListNode(next=head)
        a = dummy
        i = 1
        while i < left:
            a = a.next
            i += 1
        b = a.next
        
        prev = None
        cur = b
        while i <= right:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            i += 1
        a.next = prev
        b.next = cur
        return dummy.next
