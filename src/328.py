# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummy_o = cur_o = ListNode()
        dummy_e = cur_e = ListNode()
        i = 1
        cur = head
        while cur:
            if i % 2:
                cur_o.next = cur
                cur_o = cur_o.next
            else:
                cur_e.next = cur
                cur_e = cur_e.next
            cur = cur.next
            i += 1
        cur_e.next = None
        cur_o.next = dummy_e.next
        return dummy_o.next
