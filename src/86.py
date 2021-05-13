''# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(next=head)
        prev = sep = dummy
        cur = head
        while cur:
            if cur.val < x:
                if cur is not sep.next:
                    nxt = sep.next
                    sep.next = cur
                    prev.next = cur.next
                    cur.next = nxt
                sep = cur
            prev = cur
            cur = cur.next
        return dummy.next
