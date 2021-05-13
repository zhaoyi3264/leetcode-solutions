"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        cur = head
        while cur:
            nxt = cur.next
            cur.next = Node(cur.val, nxt)
            cur = nxt
        cur = head
        ptr = dummy = Node(0)
        while cur and cur.next:
            if cur.random:
                cur.next.random = cur.random.next
            ptr.next = cur.next
            ptr = ptr.next
            cur = cur.next.next
        return dummy.next
