# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                q,p = slow,head
                while q!=p:
                    q = q.next
                    p = p.next
                return q;
        return None


    def detectCycle2(self, head: ListNode) -> ListNode:
        addressSet = set()
        cur = head
        while cur:
            address = id(cur)
            if address in addressSet:
                break
            addressSet.add(address)
            cur = cur.next
        return cur
