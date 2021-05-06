# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tail = list2
        while tail.next:
            tail = tail.next
        prev = None
        cur = list1
        for i in range(b+1):
            if i == a:
                prev.next = list2
            if i == b:
                tail.next = cur.next
            prev = cur
            cur = cur.next
        return list1
