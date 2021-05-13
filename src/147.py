# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy = ListNode(next=head)
        ptr = head
        cur = head.next
        while cur:
            val = cur.val
            if val >= ptr.val:
                ptr = ptr.next
            else:
                prev = dummy
                while prev.next.val < val:
                    prev = prev.next
                ptr.next = cur.next
                cur.next = prev.next
                prev.next = cur
            cur = ptr.next
        return dummy.next
