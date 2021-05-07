# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        n = 0
        cur = root
        while cur:
            n += 1
            cur = cur.next
        q, r = divmod(n, k)
        sizes = [q + 1 if i < r else q for i in range(k)]
        parts = []
        cur = root
        for size in sizes:
            dummy = part = ListNode()
            for _ in range(size):
                part.next = cur
                cur = cur.next
                part = part.next
            part.next = None
            parts.append(dummy.next)
        return parts
