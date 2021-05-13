# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = dummy = ListNode(next=head)
        cur = head
        go = None
        while cur:
            if cur.next and cur.next.val == cur.val:
                go = cur.next
                while go and go.val == cur.val:
                    go = go.next
                prev.next = go
                cur = go
            else:
                prev = cur
                cur = cur.next
        return dummy.next
