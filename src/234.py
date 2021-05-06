# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        prev = None
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        half = length // 2
        curr = head
        for _ in range(half):
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        left = prev
        right = curr if length % 2 == 0 else curr.next
        while left and right:
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        return True
