# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            s = 0
            for i in range(len(stack) - 1, -1, -1):
                s += stack[i].val
                if s == 0:
                    for _ in range(len(stack) - 1, i - 1, -1):
                        stack.pop(-1)
                    break
            cur = cur.next
            
        dummy = cur = ListNode()
        for n in stack:
            n.next = None
            cur.next = n
            cur = cur.next
        return dummy.next
