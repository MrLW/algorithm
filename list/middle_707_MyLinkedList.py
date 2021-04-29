class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode(-1)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        i = 0
        cur = self.head.next
        while cur:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.head.next = ListNode(val, self.head.next)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        i = 0
        cur = self.head
        while cur:
            if i == index:
                break
            i += 1
            cur = cur.next
        if cur:
            cur.next = ListNode(val, cur.next)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        i = 0
        pre = self.head
        cur = pre.next
        while cur:
            if i == index:
                break
            i += 1
            pre = cur
            cur = cur.next
        if cur:
            pre.next = cur.next


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1, 2)
obj.get(1)
obj.deleteAtIndex(0)
obj.get(1)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
