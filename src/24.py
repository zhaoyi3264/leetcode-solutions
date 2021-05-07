# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # dummy = ListNode(next=head)
        # prev = dummy
        # cur = head
        # while cur and cur.next:
        #     next = cur.next.next
        #     prev.next = cur.next
        #     cur.next.next = cur
        #     cur.next = next
        #     prev = cur
        #     cur = next
        # return dummy.next
        cur = head
        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        return head
