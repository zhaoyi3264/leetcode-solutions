class ListNode:
    
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return str(self.val)

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dummy = ListNode()

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        cur = self.dummy.next
        i = 0
        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        next = self.dummy.next
        self.dummy.next = ListNode(val, next)
        # self.print('addhead')

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        prev = self.dummy
        cur = self.dummy.next
        while cur:
            prev = cur
            cur = cur.next
        prev.next = ListNode(val)
        # self.print('addtail')

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        i = 0
        prev = self.dummy
        cur = self.dummy.next
        while cur:
            if i == index:
                prev.next = ListNode(val, cur)
                break
            prev = cur
            cur = cur.next
            i += 1
        else:
            prev.next = ListNode(val)
        # self.print('addidx ')

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        i = 0
        prev = self.dummy
        cur = self.dummy.next
        while cur:
            if i == index:
                prev.next = cur.next
                break
            prev = cur
            cur = cur.next
            i += 1
        # self.print('delidx ')
    
    def print(self, op):
        print(op, end=': ')
        cur = self.dummy.next
        while cur:
            print(cur, end=', ')
            cur = cur.next
        print()

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
