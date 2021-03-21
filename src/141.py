# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        x = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                x = slow
                break
        return x is not None
        # if not x:
        #     return False
        # fast = head
        # while fast is not x:
        #     fast = fast.next
        #     slow = slow.next
        # return True
