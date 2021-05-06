# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        cur = head
        ans = [0 for _ in range(n)]
        idx = 0
        while cur:
            if (not stack) or (stack and cur.val < stack[-1][0]):
                stack.append((cur.val, idx))
            else:
                while stack and cur.val > stack[-1][0]:
                    _, i = stack.pop(-1)
                    ans[i] = cur.val
                stack.append((cur.val, idx))
            idx += 1
            cur = cur.next
        return ans
