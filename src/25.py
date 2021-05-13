# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = prev = ListNode()
        cur = head
        while cur:
            stack = []
            while len(stack) < k:
                stack.append(cur)
                cur = cur.next
                if not cur:
                    break
            if len(stack) < k:
                prev.next = stack[0]
                break
            
            head = tail = stack.pop(-1)
            while stack:
                tail.next = stack.pop(-1)
                tail = tail.next
            
            prev.next = head
            prev = tail
            prev.next = None
        return dummy.next
