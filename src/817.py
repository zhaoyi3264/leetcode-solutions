# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        ans = 0
        G_set = set(G)
        cur = head
        while cur:
            if cur.val in G_set and (not cur.next or cur.next.val not in G_set):
                ans += 1
            cur = cur.next
        return ans
