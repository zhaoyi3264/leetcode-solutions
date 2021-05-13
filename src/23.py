# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue

class Entry():
    def __init__(self, node):
        self.node = node
        
    def has_next(self):
        return self.node.next is not None
    
    def next(self):
        self.node = self.node.next
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = cur = ListNode()
        pq = PriorityQueue()
        for node in lists:
            if node:
                pq.put(Entry(node))
        while not pq.empty():
            entry = pq.get()
            cur.next = entry.node
            cur = cur.next
            
            if entry.has_next():
                entry.next()
                pq.put(entry)
        return dummy.next
