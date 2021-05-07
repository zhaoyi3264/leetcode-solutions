"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        dummy = ptr = Node()
        
        def dfs(head):
            nonlocal ptr
            cur = head
            while cur:
                ptr.next = cur
                ptr = ptr.next
                next = cur.next
                if cur.child:
                    dfs(cur.child)
                cur = next
        dfs(head)
        
        prev = dummy
        cur = dummy.next
        while cur:
            cur.child = None
            prev.next = cur
            cur.prev = prev
            prev = cur
            cur = cur.next
        if dummy.next:
            dummy.next.prev = None
        prev.next = None
        return dummy.next
